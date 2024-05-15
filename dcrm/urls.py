from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
  
]