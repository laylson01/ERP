from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("ERP/", include("ERP.urls")),
    path("admin/", admin.site.urls),
]