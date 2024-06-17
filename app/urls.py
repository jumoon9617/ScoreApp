from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'Player', PlayerViewSet)
router.register(r'Score', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls))
]