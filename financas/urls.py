from core import urls as core_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('natdespesas/', include('nat_despesas.urls', namespace='nat_despesas')),
    path('fornecedores/', include('fornecedores.urls', namespace='fornecedores')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
