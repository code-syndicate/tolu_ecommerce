from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from products.models import ProductCategory,Product

class HomePageView(View):
    def get(self, request):
        categories = ProductCategory.objects.order_by("?")[:6]
        categories_1 = categories[:3]
        categories_2 = categories[3:]
        products = Product.objects.order_by("?")[:18]
        context = { 
            'categories_1' : categories_1,
            'categories_2' : categories_2,
            'products' : products,
        }
        return render( request, 'logistics/home.html', context )


