from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager )



# Custom User Manager 
class CustomUserManager( BaseUserManager):
    def create_user( self, firstname, lastname, email, password ):
        user = self.model( firstname = firstname, lastname = lastname , email = self.normalize_email( email) )
        user.set_password( password)
        user.save( using = self._db )

        return user 

    def create_superuser( self, firstname, lastname, email, password):
        user = self.create_user( firstname, lastname, email, password)
        user.is_admin = True
        user.save()

        return user 



# User model
class User( AbstractBaseUser):
    firstname = models.CharField( max_length= 25, blank = False )
    lastname = models.CharField( max_length= 25, blank = False)
    email = models.EmailField( max_length= 255, unique= True, primary_key= True)
    date_joined = models.DateTimeField( auto_now  = True)
    last_modified = models.DateTimeField( auto_now= True)
    is_admin = models.BooleanField( default= False)
    




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'firstname', 'lastname', 'password']

    objects = CustomUserManager()

    def get_full_name( self):
        return self.firstname + ' ' + self.lastname


    def __str__(self):
        return self.get_full_name()

    @property
    def is_staff( self):
        return self.is_admin

    def has_perm( self, perm ):
        return True

    def has_module_perms( self, perm, app_label = None):
        return True


