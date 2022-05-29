from django.urls import path
from OnTime import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.main, name="main"),
    path("status/", views.status, name="status"),
    path("scan/", views.scan, name="scan"),
    path("scanfunc/", views.scanfunc, name="scanfunc"),
    path("profiles/", views.profiles, name="profiles"),
    path("profiles/add_profile/", views.add_profile, name="add_profile"),
    path("profiles/delete_profile/<int:id>", views.delete_prof, name="delete_prof"),
    path("profiles/edit_prof/<int:id>", views.edit_prof, name="edit_prof"),
    path("profiles/edit_prof/", views.edit_prof2, name="edit_prof2"),
    path("status/clear_hist/", views.clear_hist, name="clear_hist"),
    path("status/reset/", views.reset, name="reset"),
    path("ajax/", views.ajax, name="ajax")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

