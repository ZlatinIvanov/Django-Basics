from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("ExamPrep.web.urls")),
    path("albums/", include("ExamPrep.albums.urls")),
    path("profiles/", include("ExamPrep.profiles.urls"))
]
