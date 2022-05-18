"""aimark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from marks import views as adminviews
from api import views as apiviews

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
# router.register(r'api/marks', apiviews.MarkViewSet, basename="perform_create")
# router.register(r'api/users', apiviews.UserViewSet)

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  path('admins/', include('authenticate.urls')),
                  path('admins/marks/', include('marks.urls')),
                  path('admins/users/', include('users.urls')),

                  path('api/marks/', include('api.urls')),

                  path('admins/', adminviews.home),

                  path('api-auth/', include('rest_framework.urls')),

                  path('', include(router.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
