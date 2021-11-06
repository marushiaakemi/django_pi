from  django.urls import path
from . import views

app_name = "aplicacao"

urlpatterns = [
    path("", views.PostListView.as_view(), name='list'),
    path("/<slug:slug>", views.PostDetailView.as_view(), name="detail"),
    path("/formulario/", views.form_django, name="form_django"),
    path("/formulario/update/<int:pessoa_id>/", views.update, name="update_pessoa" ),
    path("/formulario/delete/<int:pessoa_id>/", views.delete_view, name="delete_pessoa")
]