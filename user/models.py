from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils.translation import ugettext_lazy as _
class UserManager(BaseUserManager):
    def create_user(self,username, email,fullName, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))
        email = self.normalize_email(email)
       
        user = self.model(username = username,email=email,fullName=fullName, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username, email,fullName, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, email,fullName, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    #User information
    username=models.CharField(max_length = 255,unique = True,default = '')
    email = models.EmailField(max_length = 255,unique =True)
    fullName = models.CharField(max_length = 255,verbose_name = 'Họ Tên')
    gender = models.CharField(max_length = 100)
    birthday = models.DateField(null=True, blank=True)
    address = models.TextField()
    phoneNumber = models.CharField(max_length = 11)
    image=models.FileField(default='default-picture.png')
    description = models.TextField(default='')
    #manage information
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =  ['email','fullName']
    #method
    object = UserManager()
    def __str__(self):
        return ''+self.username 
   
    