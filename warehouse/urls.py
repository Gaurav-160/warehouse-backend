from django.urls import path
from warehouse import views

urlpatterns = [
    path("godowns/", views.GodownViewSet.as_view({'get': 'list'}), name='godowns'),
    path("items/", views.ItemViewSet.as_view({'get': 'list'}), name='items'),
    path("generate-fake-data/", views.generate_fake_data, name='generate-date')
]
