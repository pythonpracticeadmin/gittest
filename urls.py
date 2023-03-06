from django.contrib import admin
from django.urls import path
from men import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", views.menhome),
    path("form/", views.men_form),
    path("data/", views.mendata),
    path("update/<id>/", views.men_update),
    path("delete/<id>/", views.men_delete),
    path("api/", views.menapi_view.as_view()),
    path("api/put/<int:pk>", views.updatedeleteapi.as_view()),
]
