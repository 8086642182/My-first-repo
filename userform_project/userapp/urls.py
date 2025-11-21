from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),
    path('list/', views.form_list, name='form_list'),
    path('create/', views.form_create, name='form_create'),
    path('edit/<int:pk>/', views.form_edit, name='form_edit'),
    path('delete/<int:pk>/', views.form_delete, name='form_delete'),
]
