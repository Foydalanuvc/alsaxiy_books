from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserModel(AbstractUser):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, _('Male')), (GENDER_FEMALE, _('Female'))]
    user_image = models.ImageField(upload_to='users/')
    id_card = models.CharField(max_length=10)
    birth_day = models.DateField()
    phone = models.CharField(max_length=13)
    location_work = models.CharField(max_length=255, null=True, blank=True)
    address_work = models.CharField(max_length=255, null=True, blank=True)
    gander = models.SmallIntegerField(choices=GENDER_CHOICES)  #--> yani faqat shu qiymatlardan bittasini qabul qila oladi boshqa qiymat qabul qilomidi


