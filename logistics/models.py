import uuid
from products.models import Product
from django.db import models
from django.contrib.auth import get_user_model

# Cart Model
class Cart( models.Model ):
    owner = models.OneToOneField( get_user_model(), related_name = "cart", on_delete = models.CASCADE )
    cart_id = models.UUIDField( default= uuid.uuid4, unique= True, primary_key= True)

# Cart Item Model 
class CartItem( models.Model):
    product = models.ForeignKey( Product, on_delete = models.SET_NULL, null = True )
    amount = models.PositiveIntegerField( default =  1)
    cart = models.ForeignKey( Cart, related_name= 'items', on_delete = models.CASCADE )

    def __str__(self):
        return self.product.product_name + " in cart - " + str(self.cart.cart_id)
    
    @property
    def price( self):
        return self.Product.price_per_unit * self.amount   

