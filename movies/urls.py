from django.urls import path
from . import views
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView




urlpatterns = [
    path('', views.ListCreateMovieAPIView.as_view(), name='get_post_movies'),
    path('<int:pk>/', views.RetrieveUpdateDestroyMovieAPIView.as_view(), name='get_delete_update_movie'),
# path('openapi/', get_schema_view(
#     title="Movie Restful Webservice",
#     description="Movie Restful Webservice Description"
# ), name='openapi-schema'),


]
