from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    LogBookListView,
    LogBookDetailView,
    LogBookCreateView,
    LogBookDeleteView,
    LogBookUpdateView,
    LogDetailView,
    LogCreateView,
    LogUpdateView,
    LogDeleteView
    
)
from .import views



urlpatterns = [
   path('', views.LogBookListView.as_view(),name='log-view'),
   path('<int:pk>/',views.LogBookDetailView.as_view(),name='log-detail'),
   path('new/', LogBookCreateView.as_view(),name='log-create'),
    path('<int:pk>/update/', views.LogBookUpdateView.as_view(),name='log-update'),
    path('<int:pk>/delete/', views.LogBookDeleteView.as_view(),name='log-delete'),
    path('submission/<int:pk>/', views.LogDetailView.as_view(),name='log-submission'),
     path('<int:pk>/new/', LogCreateView.as_view(),name='log-submit'),
      path('submission/<int:pk>/update/', views.LogUpdateView.as_view(),name='log-change'),
      path('submission/<int:pk>/delete/', views.LogDeleteView.as_view(),name='submission-delete'),
    



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)