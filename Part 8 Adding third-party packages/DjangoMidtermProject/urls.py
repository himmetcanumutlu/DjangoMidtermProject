from django.contrib import admin
from django.urls import include, path  # include'u buraya ekliyoruz

urlpatterns = [
    path("polls/", include("polls.urls")), # polls'u patrona tanıtıyoruz
    path("admin/", admin.site.urls),
]