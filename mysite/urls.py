"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from password_generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generated_password/', views.generated_password),
    path('about/', views.about)
#   path('generated_password/', views.password, name='password') - In order to change the url name
# there are 2 ways. One way is to change evrything to generate_passsword. Or keep name as password
# and call the same from views.py    
#In home.html<! -- <form action="password"> Only passowrd also can be used and 
#name can be mentioned in urls. -->
]

