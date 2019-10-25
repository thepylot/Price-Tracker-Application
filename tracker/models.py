from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=600)
    requested_price = models.IntegerField(default=0)
    last_price = models.IntegerField(null=True, blank=True)
    discount_price = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
