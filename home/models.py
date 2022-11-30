from django.db import models

# Custom model number 1


class Newsletter(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
