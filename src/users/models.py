from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    
    name = CharField(_('Name Of User'), blank=True, max_length=200)
    stripe_customer_id = CharField(max_length=50)

    # username = None
    # email = models.EmailField(unique=True, max_length=255)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    


    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

   
