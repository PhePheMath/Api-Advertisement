from django.db import models


class Promotion(models.Model):
    product = models.ForeignKey(to='enterprise.Product', on_delete=models.CASCADE)
    value = models.FloatField()
    goal = models.IntegerField()
    ignore_negative = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} por R$ {self.value}; Meta {self.goal} likes'

class Posts(models.Model):
    promotion = models.ForeignKey(to='financial.Promotion', on_delete=models.CASCADE)
    advertiser = models.ForeignKey(to='personnel.Advertiser', on_delete=models.CASCADE)
