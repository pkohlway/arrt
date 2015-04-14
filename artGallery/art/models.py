from django.db import models

# Create your models here.
class art_item(models.Model):
	item_name = models.CharField(max_length=40)
	item_type = models.CharField(max_length=40)
	price = models.FloatField()
	quantity = models.CharField(max_length=10)
	image = models.CharField(max_length=100)

	def __str__(self):
		return self.item_name