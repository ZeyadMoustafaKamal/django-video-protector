from django.db import models
from django.urls import reverse

import random
import string


def get_random_id():
    return "".join([random.choice(string.ascii_letters) for _ in range(25)])


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="videos")
    public_id = models.CharField(
        max_length=50, null=True
    )  # the public ID of the video that every user can see

    def save(self, *args, **kwargs):
        if not self.public_id:
            self.public_id = get_random_id()
            self.save()
        return super().save(*args, **kwargs)

    def get_protected_url(self):
        return reverse("video", kwargs={"public_id": self.public_id})


class VideoToken(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="tokens")
    token = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_id()  # I shouldn't use random here but I will use it just to make it as simple as pissible
            self.save()
        return super().save(*args, **kwargs)
