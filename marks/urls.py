from django.urls import path
from marks import views as views

urlpatterns = [

    path('', views.index),
    path('add', views.add),
    path('edit/<int:id>', views.edit),
    path('delete', views.delete),
    path('search', views.search),

    path('points/add/<int:id>', views.addpoint),
    path('points/delete/<int:id>', views.deletepoint),

]
