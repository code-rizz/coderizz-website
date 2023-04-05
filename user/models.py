from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
import uuid
from django.utils import timezone
from .managers import CustomUserManager
from django.core.validators import RegexValidator

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    # These fields tie to the roles!
    ADMIN = 1
    MANAGER = 2
    MEMBER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (MEMBER, 'Member')
    )
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    phone_number = models.IntegerField( unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid Phone_number')],default=0)
    reginster_number = models.IntegerField( unique=True, validators=[RegexValidator(regex='^\d{12}$', message='Length has to be 12', code='Invalid Register_number')],default=0)
    department = models.CharField(max_length=30, blank=True)
    year_of_passing = models.IntegerField( validators=[RegexValidator(regex='^\d{4}$', message='Length has to be 4', code='Invalid Register_number')],default=2024)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Register(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    phone_number = models.IntegerField( unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid Phone_number')])
    reginster_number = models.IntegerField( unique=True, validators=[RegexValidator(regex='^\d{12}$', message='Length has to be 12', code='Invalid Register_number')])
    department = models.CharField(max_length=30, blank=True)
    year_of_passing = models.IntegerField( validators=[RegexValidator(regex='^\d{4}$', message='Length has to be 4', code='Invalid Register_number')])