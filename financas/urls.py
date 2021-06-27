from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nat_despesas.urls', namespace='nat_despesas')),

]
