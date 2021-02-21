from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('list/', views.UserList.as_view()),
    path('login/', views.login_view),
    path('set-csrf/', views.login_set_cookie, name='Set-CSRF'),
    path('logout/', views.logout_view),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]
