from django.conf.urls import url

from rent import views

app_name = 'rent'
urlpatterns = [
    url(
        r'^home/$',
        views.get_homepage,
        name='homepage',
    ),
    url(
        r'^add-property/$',
        views.AddProperty.as_view(),
        name='add_property',
    ),
    url(
        r'^rented-properties/$',
        views.ListRentedProperties.as_view(),
        name='list_rented_properties',
    ),
    url(
        r'^vacant-properties/$',
        views.ListVacantProperties.as_view(),
        name='vacant_properties',
    ),
]
