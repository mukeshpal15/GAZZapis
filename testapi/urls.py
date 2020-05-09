"""testapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from testapp import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from testapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
#    path('users/', views.Userpost.as_view()),
 #   path('api/userList/',UserAPIView.as_view()),
 #   path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
#    path('UpdateName/<str:pk>/', UpdateName.as_view()),
    path('Registration/',Registration),
    path('Login/', Login),
    path('ForgotPasswordUser/', ForgotPasswordUser),
 #   path('usersLogin/', usersLogin),

#    path('Userforgotpass/', Userforgotpass),
#    path('update_user_detail/<str:pk>/', update_user_detail),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
