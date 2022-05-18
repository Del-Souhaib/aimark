from django.urls import path
from api import views as views

urlpatterns = [

    path('', views.index),
    path('add', views.add),
    path('<int:id>', views.specific),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('search', views.search),
    #
    path('points/add', views.addpoint),
    path('points/delete/<int:id>', views.deletepoint),

]
