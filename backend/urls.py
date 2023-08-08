from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/<str:public_id>', views.protected_video, name='video'),
    path('<int:lesson_id>', views.index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
