from django.db import models

# Create your models here.
class ShoppingItem(models.Model):
    item_name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Date published')
    
    def __unicode__(self):
        return "Name: " + self.item_name