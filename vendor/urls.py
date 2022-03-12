from app import urls
from django.urls import path
from .import views
urlpatterns = [
  
   
   
   
    path('addshow/', views.addshow, name="addshow"),
    path('Category/', views.Categ, name="Category"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('<int:id>/', views.update, name="update")
    
]

     