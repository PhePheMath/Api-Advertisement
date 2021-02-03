from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.username


class Advertiser(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="as_advertiser")
    twitter = models.CharField(verbose_name='TOKEN TWITTER', max_length=120)
    fcebook = models.CharField(verbose_name='TOKEN FACEBOOK', max_length=120)
    instagr = models.CharField(verbose_name='TOKEN INSTAGRAM', max_length=120)

class Personnel(models.Model):

    class Meta:
        unique_together = ('enterprise', 'user',)

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="as_personnel")
    enterprise = models.ForeignKey('enterprise.Enterprise', on_delete=models.CASCADE, related_name='workers')
    authority = models.IntegerField()

    def __str__(self):
        return f'{super(Personnel, self).__str__()} ({self.enterprise.name})'
