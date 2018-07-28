from django.conf.urls import url

from rent import views

app_name = 'rent'
urlpatterns = [
    url(
        r'^vacant-properties/$',
        views.ListVacantProperties.as_view(),
        name='vacant_properties',
    ),
]
