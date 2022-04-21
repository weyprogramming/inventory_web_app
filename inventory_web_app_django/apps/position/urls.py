from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PositionItemViewSet, PositionViewSet, PositionDetailViewset

router = DefaultRouter()
router.register("positions", PositionViewSet, basename="positions")
router.register("position-items", PositionItemViewSet, basename="position-items")
router.register("position-details", PositionDetailViewset, basename="position-details")

urlpatterns = [
    path('', include(router.urls))
]