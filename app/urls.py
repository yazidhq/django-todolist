from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete_item/<int:id_item>', views.delete_item, name="delete_item"),
    path('update_item/<int:id_item>', views.update_item, name="update_item"),
    path('progress_item/<int:id_item>', views.progress_item, name="progress_item")
]
