from django.urls import include, path
from django.contrib import admin
from server.api import views

urlpatterns = [
    path('', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('markers/', views.handle_markers_request, name='handle-markers-request'),
    path('markers/<int:pk>', views.handle_markers_request, name='handle-markers-request'),
]