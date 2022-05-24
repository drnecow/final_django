"""final_exam URL Configuration

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
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from main.views import BookViewSet, JournalViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # Paths to obtain, refresh and verify JSON web token for JWT authorization
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('books/', BookViewSet.as_view({'post': 'create'})),
    path('books/<int:book_id>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('journals/', JournalViewSet.as_view({'post': 'create'})),
    path('journals/<int:journal_id>/', JournalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
