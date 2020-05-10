from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,username,email,password = None):
        if not email:
            raise ValueError("Xin nhập địa chỉ email")
        if not username:
            raise ValueError("Xin nhập tên tài khoản")
        user = self.model(
            username = username,
            email = self.normalize_email(email),
            
        )
        
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(
            username = username,
            password = password,
            email = self.normalize_email(email),
        ) 

        user.is_admin = True
        user.save(using=self._db)
       
        return user

class User(AbstractBaseUser):
    #User information
    username=models.CharField(max_length = 255,verbose_name = 'Tên Đăng Nhập',unique = True,default = '')
    email = models.EmailField(max_length = 255,unique =True)
    fullName = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 100)
    birthday = models.DateTimeField(default = timezone.now)
    address = models.TextField()
    phoneNumber = models.CharField(max_length = 11)
    #manage information
    is_active = models.BooleanField(default = True)
    is_user = models.BooleanField(default=False)
    is_staff = models.BooleanField(default = False)
    is_admin =models.BooleanField(default = False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =  ['email',]
    #method
    object = UserManager()
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def is_active(self):
        return self.is_active
    def is_user(self):
        return self.is_user

    def is_staff(self):
        return self.is_admin
    
    def is_admin(self):
        return self.is_admin
    
    