# django imports
from django.conf.urls import url, include
# rest framework
from rest_framework import routers
# local imports
from rent.api import views


# registering routers
router = routers.DefaultRouter()
router.register('properties', views.PropertyViewSet)


app_name='rent_api'
urlpatterns = [
    url(r'^', include(router.urls)),
]
