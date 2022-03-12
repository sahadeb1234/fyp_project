
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from app.views import AddToCartView
from app.views import MyCartView
from app.views import ManageCartView
from app.views import EmptyCartView
from app.views import CheckoutView
from app.views import  CustomerRegistrationView
from app.views import  CustomerLogoutView
from app.views import  CustomerLoginView
from app.views import  CustomerProfileView
from app.views import   PasswordForgotView
from app.views import   PasswordResetView
from app.views import    SearchView 
from app.views import   KhaltiRequestView
from app.views import   KhaltiVerifyView 
from app.views import   CustomerOrderDetailView
from app.views import AdminLoginView  
from app.views import  AdminHomeView
from app.views import AdminOrderDetailView  





urlpatterns = [
     path('', views.ProductView.as_view(), name="index"),
     path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name="product-detail"),
     path('search/', SearchView.as_view(), name="search"),
     path("add-to-cart-<int:pro_id>/", AddToCartView.as_view(), name="addtocart"),
     path("my-cart/", MyCartView.as_view(), name="mycart"),
     path("manage-cart/<int:cp_id>/", ManageCartView.as_view(), name="managecart"),
     path("empty-cart/", EmptyCartView.as_view(), name="emptycart"),
     path("checkout/", CheckoutView.as_view(), name="checkout"),
     path("register/",
         CustomerRegistrationView.as_view(), name="customerregistration"),
     path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
     path("login/", CustomerLoginView.as_view(), name="customerlogin"),
     path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
     path("forgot-password/", PasswordForgotView.as_view(), name="passworforgot"),
     path("password-reset/<email>/<token>/",
         PasswordResetView.as_view(), name="passwordreset"),
    path("khalti-request/", KhaltiRequestView.as_view(), name="khaltirequest"),
    path("khalti-verify/", KhaltiVerifyView.as_view(), name="khaltiverify"),
    path('grow-your-business/', views.vendor, name='grow-your-business'),
    path("profile/order-<int:pk>/", CustomerOrderDetailView.as_view(),
         name="customerorderdetail"),
    path("admin-login/", AdminLoginView.as_view(), name="adminlogin"),
    path('success/',views.success,name="success"),
    path("admin-home/", AdminHomeView.as_view(), name="adminhome"),
    path("admin-order/<int:pk>/", AdminOrderDetailView.as_view(),
         name="adminorderdetail"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata")

   
     




    



     
     




   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)