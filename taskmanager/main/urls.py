
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),
    path('imported', views.imported, name='imported'),
    path('analog', views.analog, name='analog'),
    path('finalPrice', views.finalPrice, name='finalPrice'),
    path('authorisation', views.authorisation, name='authorisation'),
    path('glavnayaAuthorised', views.glavnayaAuthorised, name='glavnayaAuthorised'),
    path('history', views.history, name='history')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]