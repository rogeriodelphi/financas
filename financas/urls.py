from apps.core import urls as core_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# if settings.DEBUG:
#     import debug_toolbar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urls)),
    path('natdespesas/', include('apps.nat_despesas.urls', namespace='nat_despesas')),
    path('fornecedores/', include('apps.fornecedores.urls', namespace='fornecedores')),
    path('despesas/', include('apps.despesas.urls', namespace='despesas')),
    # path('__debug__/', include(debug_toolbar.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
