from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_group', views.create_group, name='create_group'),
    
    path('emaildashboard', views.emaildashboard, name='emaildashboard'),
    path('mailsent', views.mailsent, name='mailsent'),
    path('email_list_page', views.email_list_page, name='email_list_page'),
    path('editEmailList/<pk>', views.editEmailList, name='editEmailList'),
    path('deleteEmailList/<pk>', views.deleteEmailList, name='deleteEmailList'),
]
