from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # ================= WELCOME (PUBLIC) =================
    path('', views.welcome_view, name='welcome'),   # 👈 Render root URL
    path('welcome/', views.welcome_view, name='welcome'),

    # ================= AUTH =================
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # 🔐 Forgot Password Flow
    path(
        'forgot-password/',
        auth_views.PasswordResetView.as_view(
            template_name='diary/forgot_password.html'
        ),
        name='forgot_password'
    ),

    path(
        'reset-password-sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='diary/reset_sent.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='diary/reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='diary/reset_complete.html'
        ),
        name='password_reset_complete'
    ),

    # ================= DIARY (PROTECTED) =================
    path('home/', views.diary_home, name='diary_home'),
    path('create/', views.diary_create, name='diary_create'),
    path('diary/<int:diary_id>/', views.diary_detail, name='diary_detail'),
    path('edit/<int:diary_id>/', views.diary_edit, name='diary_edit'),
    path('delete/<int:diary_id>/', views.diary_delete, name='diary_delete'),
]
