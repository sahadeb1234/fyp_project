from app import urls
from django.urls import path
from .import views
urlpatterns = [
  
   
   
   
    path('addshow/', views.addshow, name="addshow"),
    path('Category/', views.Categ, name="Category"),
    path('deletebycat/<int:id>/', views.delete_data, name="deletecat"),
    path('Cat/<int:id>/', views.update, name="updatecat"),
    path('Your-business/', views.adbus, name="Your-business"),
    # path('<int:pk>', views.CandidateView.as_view(), name='candidate')
    
]

     