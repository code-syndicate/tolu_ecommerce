from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from products.models import ProductCategory, Product
from django.http import HttpResponse


class HomePageView(View):
    def get(self, request):
        categories = ProductCategory.objects.order_by("?")[:6]
        categories_1 = categories[:3]
        categories_2 = categories[3:]
        products = Product.objects.order_by("?")[:18]
        context = {
            'categories_1': categories_1,
            'categories_2': categories_2,
            'products': products,
        }
        return render(request, 'logistics/index.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'logistics/login.html')


class SignUpView(View):
    def post(self, request):
        data = request.POST
        fname = data.get('firstname', None)
        lname = data.get('lastname', None)
        email = data.get('email', None)
        password1 = data.get('password1', None)
        password2 = data.get('password2', None)

        # if not ( fname and lname and email and pa
        if not (password1 and password2 and password1 == password2):
            context = {
                'message': "Password fields do not match"
            }
            return render(request, 'logistics/login.html', context)

        new_user = get_user_model().objects.create(
            firstname=fname, lastname=lname, email=email)
        new_user.set_password(password)
        return redirect('/login')

        # return render(request, 'logistics/signup.html')
