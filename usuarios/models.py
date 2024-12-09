from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):

    telefono = models.CharField(max_length=10, blank=True, null=True)
    # class Meta:
    #     verbose_name = _("customuser")
    #     verbose_name_plural = _("customusers")

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("customuser_detail", kwargs={"pk": self.pk})
