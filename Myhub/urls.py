"""
URL configuration for BluescriptsStudentBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# import blueapp
from Myhub import views



# urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path('', blueapp.view.index),
    # path('firstp', views.firstpage, name='firstpage'),
    # path('math/', views.Math, name='MathPage'),
    # # path('english/', views.English),
    # path('user/', userview.Login),
    # path('Sign_up/', userview.Sign_up),
    # path('forget_p/', userview.forget_password),
    # path('home/', onehealthview.Homepage, name='HomePage'),
    # path('about/', onehealthview.About, name='About'),
    # path('contact/', onehealthview.Contact, name='Contact'),
    # path('', onehealthview.one_health_view, name='one_health_url'),
    # path('appointment_scheduled',onehealthview.appointment_created_view, name='appointment_created_url'),
   
urlpatterns = [
    path('home/', views.Home, name='homepage'),
    path('signup/', views.Signup, name='signuppage'),
    path('login/', views.Login, name='loginpage'),
    path('logout/', views.Logout, name='logout'),
    # dynamic
    path('product/<str:num>', views.product, name='productpage'),
    path('blog/<str:id>', views.eachBlog, name='blog'),
    path('create/', views.createBlog, name='createblog'),
    path('edit/<str:id>', views.editBlog, name='edit'),
    path('todo/', views.MyTodo, name='todo'),
    path('todo/<str:id>', views.eachTodo, name='todo'),
 ]


   


