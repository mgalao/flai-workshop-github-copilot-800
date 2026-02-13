"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import (
    api_root,
    UserViewSet,
    TeamViewSet,
    ActivityViewSet,
    LeaderboardViewSet,
    WorkoutViewSet
)
import os

# Set up the router for REST API endpoints
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

# Get the base URL for the API based on environment
# REST API endpoint format: https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
# Example: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    BASE_URL = f"https://{codespace_name}-8000.app.github.dev"
else:
    BASE_URL = "http://localhost:8000"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('', api_root, name='home'),
]
