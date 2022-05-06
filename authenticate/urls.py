from django.urls import path
from authenticate import views as authviews

urlpatterns = [

    path('login', authviews.loginauth),
    path('loginclick', authviews.loginclick),
    path('logoutclick', authviews.logoutclick)

]
