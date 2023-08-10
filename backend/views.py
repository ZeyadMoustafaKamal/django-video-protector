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
    video_token.delete()
    response = HttpResponse(lesson.video.read(), content_type="video/mp4")
    response["Content-Disposition"] = f'inline; filename="{lesson.title}.mp4"'
    return response


def index(request, lesson_id):
    context = {}
    lesson = get_object_or_404(Lesson, id=lesson_id)
    token = VideoToken(lesson=lesson) # I named it video in the models by mistake
    token.save()
    context['lesson'] = lesson
    context['token'] = token
    return render(request, 'index.html', context)