from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse
from .models import Lesson, VideoToken

def protected_video(request, public_id):
    token = request.GET.get('token')
    try:
        video_token = VideoToken.objects.get(token=token)
    except VideoToken.DoesNotExist:
        return HttpResponseForbidden()
    lesson = get_object_or_404(Lesson, public_id=public_id)
    if not video_token in lesson.tokens.all():
        return HttpResponseForbidden()
    """
    Here I have a problem , the iframes sends two requests one for the HTML page and one for the video itself
    and in the case I didnt know exactly how to make a way to delete the tokens or how to make a way to mark the token as not_valid
    but I discovered a way that may help . I will check if it used and delete it but after returning the video itself
    so it will work like this

    the iframe sends the first request -> I mark the token as used=True -> the iframe sends the second request -> I return the video and delete the token
    I am sure that there is a better like to make a counter for how many times the token is used 
    but I really think that this way will will be good and enough .
    """
    if video_token.used:
        video_token.delete()
    else:
        video_token.used = True
        video_token.save()
    response = HttpResponse(lesson.video.read(), content_type="video/mp4")
    response["Content-Disposition"] = f'inline; filename="{lesson.title}.mp4"'
    return response


def index(request, lesson_id):
    context = {}
    lesson = get_object_or_404(Lesson, id=lesson_id)
    token = VideoToken(video=lesson) # I named it video in the models by mistake
    token.save()
    context['lesson'] = lesson
    context['token'] = token
    return render(request, 'index.html', context)