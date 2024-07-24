from django.db import models

# Create your models here.
class Tapic(models.Model):
    """Stores the title of the topic the user is learning about """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_add_now=True)
     
    def __str__(self):
        """Return a string representation of the model"""
        return self.text




