from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_page, name='login_app'),
    path('', views.login_page, name='login_app'),
    path('logout/', views.logout_user, name='logout_app'),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('register/', views.user_register, name='registration'),

]