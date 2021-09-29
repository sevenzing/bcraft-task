from rest_framework import routers
from stats.views import StaticticViewSet
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'statistic', StaticticViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
