from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _

# Create your models here.
"""class User(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 300, unique=True)
    contact = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    dob = models.DateField()                                              #YYYY-MM-DD
    address = models.TextField()
    password = models.CharField(max_length=150, default="")

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".strip()"""

class User(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 300, unique=True)
    contact = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    dob = models.DateField()                                              #YYYY-MM-DD
    address = models.TextField()
    password = models.CharField(max_length=150)

    USERNAME_FIELD = 'contact'  # Set 'contact' as the username field
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".strip()

class Admin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100, blank=True)
    year_of_passing = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"{self.degree} from {self.university} (Year: {self.year_of_passing})"