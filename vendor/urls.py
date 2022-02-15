from app import urls
from django.urls import path
from .import views
urlpatterns = [
    path('registers/',views.createUser,name="registers"),
    path('verify/',views.verifyUser,name="verify"),
    path('loginn/',views.login_function,name="loginn"),
    path('success/',views.success,name="success"),
    path('logout/',views.logout_function,name='logout'),
    path('addshow/', views.addshow, name="addshow")
]

     