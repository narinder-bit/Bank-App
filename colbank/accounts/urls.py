"""colbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.home, name='home.list'),
    path('dashboard/', views.dash_board, name='dash-board'),
     path('deposit/', views.DepositCreateView.as_view(), name='deposit.create'),
     path('about/', views.about, name='about'),
<<<<<<< HEAD
<<<<<<< HEAD
=======
     path('withdrawal/', views.WithdrawalCreateView.as_view(), name='withdrawal.create'),
     path('transfer/', views.WithdrawalCreateView.as_view(), name='transfer.create'),
 
>>>>>>> 15035425b68f54c45486bad6bf4749255f02e16e
=======
     path('withdrawal/', views.WithdrawalCreateView.as_view(), name='withdrawal.create'),
     path('transfer/', views.WithdrawalCreateView.as_view(), name='transfer.create'),
 
>>>>>>> 15035425b68f54c45486bad6bf4749255f02e16e
]
