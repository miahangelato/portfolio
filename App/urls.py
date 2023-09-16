from django.urls import path

from App import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.projects, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('contact_messages/', views.contact_list_view, name='contact_list_view'),
    path('contact_messages/<int:id>/', views.contact_detail_view, name='contact_detail_view'),
    ]