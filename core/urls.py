from django.urls import path

from .views import index, charts, tables, forms
# from .views import dashboard
# from .views import home

urlpatterns = [
    path('', index, name="index"),
    path('charts/', charts, name="charts"),
    path('tables/', tables, name="tables"),
    path('forms', forms, name='forms'),
    # path('', index, name="demo_2/index"),
    # path('home/', home, name="home"),
    # path('dashboard/', dashboard, name="dashboard"),
]
