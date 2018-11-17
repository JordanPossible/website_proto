from django.urls import path
from website_app import views


urlpatterns = [
    path('home/', views.index, name='index'),
    path('tarif/', views.tarif, name='tarif'),
    path('media/', views.MediaListView.as_view(), name='media'),
    path('contact/', views.contact, name='contact'),

]
