from django.urls import path

from .views import user_logout

app_name = 'apps.accounts'

urlpatterns = [
    path('sair/', user_logout, name='user_logout'),
]