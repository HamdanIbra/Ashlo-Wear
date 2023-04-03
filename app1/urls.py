from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),  # main pageeeee
    
    path('', views.log),
    path('login', views.login),
    path('register', views.register),
    path('registration', views.registration),
]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.index),
#     path('signup',views.signup),
#     path('signin',views.signin),
#     path('success',views.success),
#     path('logout',views.logout)
# ]