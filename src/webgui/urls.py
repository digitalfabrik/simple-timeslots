from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>', views.event, name='event'),
    path('cancel/<str:token>', views.cancel, name='cancel'),
    path('cancel/confirm/<str:token>', views.cancel, name='cancel_confirm')
]
