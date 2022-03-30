from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, UserRegistrationView,
    UserResetPasswordView, UserPasswordResetDoneView,
    UserPasswordResetConfirmView, UserPasswordResetCompleteView,
)



app_name = 'accounts'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

    path('reset/', UserResetPasswordView.as_view(), name='reset_password'),
    path('reset-done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('confirm/complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
