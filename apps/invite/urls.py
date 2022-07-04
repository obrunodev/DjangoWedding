from django.urls import path

from .views import invite

app_name = 'invite'
urlpatterns = [
    path('', invite.index, name='index'),
    path('confirm/<int:guest_id>/', invite.confirm, name='confirm'),
]
