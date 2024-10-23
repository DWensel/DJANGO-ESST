from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # The empty path here means the default homepage will be the url without any added path. i.e. LocalHost
    # path('authorized', views.AuthoerizedView.as_view()), # Our system doesn't really need this as we aren't going to the view?
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout',views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
