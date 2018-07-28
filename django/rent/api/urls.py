from django.conf.urls import url, include

from rest_framework import routers

from rent.api import views


router = routers.DefaultRouter()
router.register('properties', views.PropertyViewSet)


app_name='rent_api'
urlpatterns = [
    url(r'^', include(router.urls)),
]
