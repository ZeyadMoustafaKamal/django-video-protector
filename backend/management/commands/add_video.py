from django.core.management import BaseCommand
from django.core.files import File
from backend.models import Lesson

import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = "video.mp4"
        if not os.path.exists(path):
            self.stderr.write(self.style.ERROR("file {} not found".format(path)))
        with open(path, "rb") as f:
            Lesson.objects.create(
                title="test", video=File(f, name=os.path.basename(path))
            )
            self.stdout.write(self.style.SUCCESS("created successfully"))
