from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

# Custom Imports
from . import views

app_name = 'general'
urlpatterns = (    
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServiceView.as_view(), name='services'),
    path('services/<pk>', views.ServiceDetailView.as_view(), name='service-details'),
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/ajax/', views.contactSubmit.as_view(), name='contact_ajax'),


    


)
   