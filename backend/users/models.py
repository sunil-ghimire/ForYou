from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
import random
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Passion(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SexualOrientation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def upload_path(instance, filename):
    return '/'.join(['images', str(instance.email), filename])

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("agender", "Agender"),
        ("androgynous", "Androgynous"),
        ("bigender", "Bigender"),
        ("female_to_male", "Female to male"),
        ("genderfluid", "Gender fluid"),
        ("genderqueer", "Gender Queer"),
        ("male_to_female", "Male to female"),
        ("FMT", "FMT"),
        ("non-binary", "Non-binary"),
        ("pangender", "Pangender")
    )
    LOOKING_FOR_CHOICES = (
        ('long_term_partner', 'Long term partner'),
        ('short_term_partner', 'Short term partner'),
        ('friends', 'Friends'),
        ('still_figuring_out', 'Still figuring out'),
        ('not_sure', 'Not sure')
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=20)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    show_me = models.CharField(
        choices=GENDER_CHOICES, max_length=20)
    passion = models.ManyToManyField(
        Passion, related_name='passion')
    sexual_orientation = models.ManyToManyField(
        SexualOrientation, related_name='sexual_orientation')
    looking_for = models.CharField(
        choices=LOOKING_FOR_CHOICES, max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.token:
            self.token = random.randint(100000, 9999999999)
        return super(CustomUser, self).save(*args, **kwargs)