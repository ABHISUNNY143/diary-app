from django.urls import path
from . import views

urlpatterns = [
    # AUTH
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('logout/', views.logout_view, name='logout'),

    # DIARY
    path('home/', views.diary_home, name='diary_home'),
    path('create/', views.diary_create, name='diary_create'),
    path('diary/<int:diary_id>/', views.diary_detail, name='diary_detail'),


path('edit/<int:diary_id>/', views.diary_edit, name='diary_edit'),
path('delete/<int:diary_id>/', views.diary_delete, name='diary_delete'),
]
