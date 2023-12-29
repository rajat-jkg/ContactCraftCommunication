from django.urls import path
from . import views





password_resert_patterns = [
  path('reset-password/', views.PasswordReset.as_view(), name ='reset_password'),
  path('reset-password-sent/', views.PasswordResetDone.as_view(), name ='password_reset_done'),
  path('reset/<uidb64>/<token>', views.PasswordResetConfirm.as_view(), name ='password_reset_confirm'),
  path('reset-password-complete/', views.PasswordResetComplete.as_view(), name ='password_reset_complete'),
]




urlpatterns = [
    
    path('', views.home, name='home'),
    path('login/', views.loginView.as_view(), name='login'),
    path('register/', views.registerView.as_view(), name='register'),
    path('account/', views.account, name='account'),
    path('account/update', views.update_user, name='profile-update'),
    path('logout/', views.Logout.as_view(), name= 'logout'),
    path('change-password/', views.UpdatePassword.as_view(), name= 'change-password'),


    path('accounts/login/', views.loginView.as_view(), name='login-2'),
    path('accounts/profile/', views.account, name='account-2'),

    
    
] + password_resert_patterns

