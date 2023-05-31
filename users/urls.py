from django.urls import path 
from . import views 

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('profilepage', views.profilepage, name='profilepage'),
    path('profileedit/<pk>', views.profileedit, name='profileedit'),
]
