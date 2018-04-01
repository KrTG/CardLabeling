from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:card_num>', views.card, name='card'),
    path('done', views.done, name='done'),
]