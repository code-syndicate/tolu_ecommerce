from django.urls import path
from .import views 


urlpatterns = [
    path( '', views.HomePageView.as_view() , name = 'homepageview'),
    path( 'login/', views.LoginView.as_view(), name = 'loginview'),
    path( 'sign_up/' , views.SignUpView, name = 'signup', ),

]