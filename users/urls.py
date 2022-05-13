from django.urls import path
from users import views as views

urlpatterns = [

    path('', views.index),
    path('add', views.add),
    path('edit/<int:id>', views.edit),
    path('delete', views.delete),


]
