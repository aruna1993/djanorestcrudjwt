
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# urls
urlpatterns = [
path('openapi/', get_schema_view(
    title="Movie Restful Webservice",
    description="Movie Restful Webservice Description"
), name='openapi-schema'),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
