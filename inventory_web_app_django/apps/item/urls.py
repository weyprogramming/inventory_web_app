from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ItemViewset, ItemSearchViewset

router = DefaultRouter()
router.register("items", ItemViewset, basename="items")

urlpatterns = [
    path('', include(router.urls)),
    path('item-search/', ItemSearchViewset.as_view({'get':'list'}), name="itemSearch")
]