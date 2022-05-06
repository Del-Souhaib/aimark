from django.urls import path
from marks import views as views

urlpatterns = [

    path('', views.index),
    path('add', views.add),
    path('update', views.update),
    path('delete', views.delete)

]
