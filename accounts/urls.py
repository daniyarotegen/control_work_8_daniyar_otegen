from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import UserUpdateView, UserProfileView, RegisterView, CurrentUserProfileView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('user/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('user/', CurrentUserProfileView.as_view(), name='current_user_profile'),
    path('user/<int:user_id>/', UserProfileView.as_view(), name='user_profile'),
    path('user/update/', UserUpdateView.as_view(), name='user_update'),
    path('register/', RegisterView.as_view(), name='register'),
]
