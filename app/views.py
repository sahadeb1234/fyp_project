
from urllib import request
from django import views
from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .forms import *
from .forms import CustomerRegistrationForm, CustomerLoginForm,  CheckoutForm,  PasswordForgotForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from .utils import password_reset_token
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import *
import requests
from django.http import JsonResponse
from Shopmandus.settings import EMAIL_HOST_USER
from vendor.forms import productaddForm

from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required






# Create your views here.

class EcomMixin(object):
    def dispatch(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            if request.user.is_authenticated and request.user.customer:
                cart_obj.customer = request.user.customer
                cart_obj.save()
        return super().dispatch(request, *args, **kwargs)
def vendor(request):
   
    return render(request, 'app/vendor.html')

class ProductView(View):
    def get(self, request):
        brand = Brand.objects.all()
        brandID= request.GET.get('brand') 
       
        category = Category.objects.all()  
        categoryID = request.GET.get('category')  
        storage = Storage.objects.all() 
        storageID = request.GET.get('storage')  
        if categoryID:
             product = Product.objects.filter(category=categoryID)
        elif brandID:
               product = Product.objects.filter(brand=brandID)
        # elif storageID:
        #        product = Product.objects.filter(storage=storageID)

        elif storageID:
               product = Product.objects.filter(storage=storageID)

        else:
            product = Product.objects.all()
            paginator = Paginator(product,12)
            page_number = self.request.GET.get('page')
            product = paginator.get_page(page_number)

        return render(request, 'app/index.html', {'brand':brand,'product': product,'category':category, 'storage':storage})
        



class ProductDetailView(EcomMixin,View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.view_count +=1
        product.save()
        return render(request, 'app/productdetail.html', {'product':product})


class AddToCartView(EcomMixin, TemplateView):
    template_name = "app/addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get product id from requested url
        product_id = self.kwargs['pro_id']
        # get product
        product_obj = Product.objects.get(id=product_id)

        # check if cart exists
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(
                product=product_obj)

            # item already exists in cart
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
            # new item is added in cart
            else:
                cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()

        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save()
            

        return context

class MyCartView(EcomMixin,TemplateView):
    template_name = "app/Mycart.html"
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart

        return context

class ManageCartView(EcomMixin,View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs["cp_id"]
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart

        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()

        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect("mycart")



class EmptyCartView(EcomMixin,View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartproduct_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect("mycart")




    


class CheckoutView( SuccessMessageMixin,CreateView):
    template_name = "app/Checkout.html"
    form_class = CheckoutForm
    success_url = reverse_lazy("/")
 
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.customer:
            pass
        else:
            return redirect("/customerlogin/?next=/checkout/")
        return super().dispatch(request, *args, **kwargs)

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context['cart'] = cart_obj
        return context
    success_message = 'Employee successful created'
          
 
    def form_valid(self, form):
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.discount = 0
            form.instance.total = cart_obj.total
            form.instance.order_status = "Order Received"
            # form.instance.seller = request.user
            # form.instance.seller = self.request.user
            
            del self.request.session['cart_id']
            pm = form.cleaned_data.get("payment_method")
            order = form.save()
            if pm == "Khalti":
                return redirect(reverse("khaltirequest") + "?o_id=" + str(order.id))
           
        else:
            return redirect("/")
        return super().form_valid(form)

class KhaltiVerifyView(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get("token")
        amount = request.GET.get("amount")
        o_id = request.GET.get("order_id")
        print(token, amount, o_id)

        url = "https://khalti.com/api/v2/payment/verify/"
        payload = {
            "token": token,
            "amount": amount
        }
        headers = {
            "Authorization": "test_secret_key_876e15ef7ce44e42bf5cbd7bb39f22f5"
        }

        order_obj = Order.objects.get(id=o_id)

        response = requests.post(url, payload, headers=headers)
        resp_dict = response.json()
        if resp_dict.get("idx"):
            success = True
            order_obj.payment_completed = True
            order_obj.save()
        else:
            success = False
        data = {
            "success": success
        }
        return JsonResponse(data)


# class EsewaRequestView(View):
#     def get(self, request, *args, **kwargs):
#         o_id = request.GET.get("o_id")
#         order = Order.objects.get(id=o_id)
#         context = {
#             "order": order
#         }
#         return render(request, "esewarequest.html", context)











class CustomerRegistrationView(CreateView):
    template_name = "app/customerregistration.html"
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user   
        login(self.request, user)
        subject = "welcome to Shopmandu"
        message = f"Hi {user.username}, Thank you for Register in shopmandu."
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject,message,email_form,recipient_list)
        return super().form_valid(form)
    

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url
        

class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class CustomerLoginView(FormView):
    template_name = "app/login.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("index")

    # form_valid method is a type of post method and is available in createview formview and updateview
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Customer.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    def get_success_url(self):
        if "next" in self.request.GET:
            next_url = self.request.GET.get("next")
            return next_url
        else:
            return self.success_url

class CustomerProfileView(TemplateView):
    template_name = "app/Profile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        context['customer'] = customer
        orders = Order.objects.filter(cart__customer=customer).order_by("-id")
        context["orders"] = orders
        return context

class PasswordForgotView(FormView):
    template_name = "app/forgotpassword.html"
    form_class = PasswordForgotForm
    success_url = "/forgot-password/?m=s"

    def form_valid(self, form):
        # get email from user
        email = form.cleaned_data.get("email")
        # get current host ip/domain
        url = self.request.META['HTTP_HOST']
        # get customer and then user
        customer = Customer.objects.get(user__email=email)
        user = customer.user
        # send mail to the user with email
        text_content = 'Please Click the link below to reset your password. '
        html_content = url + "/password-reset/" + email + \
            "/" + password_reset_token.make_token(user) + "/"
        send_mail(
            'Password Reset Link | Submandu',
            text_content + html_content,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return super().form_valid(form)

class PasswordResetView(FormView):
    template_name = "app/passwordreset.html"
    form_class = PasswordResetForm
    success_url = "/login/"

    def dispatch(self, request, *args, **kwargs):
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        token = self.kwargs.get("token")
        if user is not None and password_reset_token.check_token(user, token):
            pass
        else:
            return redirect(reverse("ecomapp:passworforgot") + "?m=e")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        password = form.cleaned_data['new_password']
        email = self.kwargs.get("email")
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return super().form_valid(form)


class SearchView(TemplateView):
    template_name = "app/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Product.objects.filter(
            Q(title__icontains=kw) | Q(description__icontains=kw) | Q(return_policy__icontains=kw))
        print(results)
        context["results"] = results
        return context

class KhaltiRequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)
        context = {
            "order": order
        }
        return render(request, "app/khaltirequest.html", context)


class CustomerOrderDetailView(DetailView):
    template_name = "app/customerorderdetail.html"
    model = Order
    context_object_name = "ord_obj"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Customer.objects.filter(user=request.user).exists():
            order_id = self.kwargs["pk"]
            order = Order.objects.get(id=order_id)
            if request.user.customer != order.cart.customer:
                return redirect("customerprofile")
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

class AdminLoginView(FormView):
    template_name = "app/vendor/login.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy("success")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
        return super().form_valid(form)
        
class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)

class AdminHomeView(AdminRequiredMixin, TemplateView):
    template_name = "app/vendor/Order.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pendingorders"] = Order.objects.filter(
            order_status="Order Received").order_by("-id")
        return context

class AdminOrderDetailView(AdminRequiredMixin, DetailView):
    template_name = "app/vendor/adminorderdetail.html"
    model = Order
    context_object_name = "ord_obj"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["allstatus"] = ORDER_STATUS
        return context






@login_required
def success(request):
    
            product = Product.objects.filter(user=request.user)
            count = len(product)
            order = Order.objects.filter()  
            order = order.count()

            category = Category.objects.all()
          
           
            
            return render(request,'app/vendor/success.html', {'products':product, 'count':count,'orders':order, 'category':category})


def delete_data(request, id):
    if request.method =='POST':
        pi = Product.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/success/')


# def update_data(request, id):
#     if request.method == 'POST':
#         pi = Product.objects.get(pk=id)
#         fm = productaddForm(request.POST, instance=pi)
#         if fm.is_valid():
#             fm.save()
#         else:
#          pi = Product.objects.get(pk=id)
#          fm = productaddForm(instance=pi)
#     return render(request,'app/vendor/update.html',{'form':fm})


def  updatedata(request, id):
    if request.method == 'POST':
        pis = Product.objects.get(pk=id)
        fm = productaddForm(request.POST, instance=pis)
        if fm.is_valid():
         fm.save()
    else:
        pis = Product.objects.get(pk=id)
        fm = productaddForm(instance=pis)
    return render(request, 'app/vendor/update.html', {'form':fm})



#         @login_required
# def success(request):
    
#             product = Product.objects.filter(user=request.user)
#             count = len(product)
#             # order = request.GET.get('cart')

#             # order = Order.objects.get(ordered_by=order)

#             # order = order.count()
#             return render(request,'app/vendor/success.html', {'products':product, 'count':count,'orders':order})


class AdminOrderStatuChangeView(AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        order_id = self.kwargs["pk"]
        order_obj = Order.objects.get(id=order_id)
        new_status = request.POST.get("status")
        order_obj.order_status = new_status
        order_obj.save()
        return redirect(reverse_lazy("adminorderdetail", kwargs={"pk": order_id}))

def add_wishlist(request):
	pid=request.GET['product']
	product=Product.objects.get(pk=pid)
	data={}
	checkw=Wishlist.objects.filter(product=product,user=request.user).count()
	if checkw > 0:
		data={
			'bool':False
		}
	else:
		wishlist=Wishlist.objects.create(
			product=product,
			user=request.user
		)
		data={
			'bool':True
		}
	return JsonResponse(data)


def my_wishlist(request):
	wlist=Wishlist.objects.filter(user=request.user)
	return render(request, 'app/wishlist.html',{'wlist':wlist})


def delete_wishlist(request, id):
    if request.method =='POST':
        Pii = Wishlist.objects.get(pk=id)
        Pii.delete()
        return HttpResponseRedirect('/my_wishlist/')