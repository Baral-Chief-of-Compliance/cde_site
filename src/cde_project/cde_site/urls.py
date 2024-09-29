from django.urls import path
from . import views

app_name = "cde_site"

urlpatterns = [
    path("", views.index, name="index"),
    path("theme/<int:t_id>", views.theme_info, name="theme_info"),
    path("theme/<int:t_id>/img/<int:im_id>", views.theme_info_img, name="theme_info_img"),
    path("theme/<int:t_id>/document/<int:dm_id>", views.theme_info_document, name="theme_info_document"),
]
