from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Achuu_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followd_by",
        symmetrical = False, 
        blank = True
    )
    #galleryID = models.IntegerField(blank=True, null=True)
    #userID
    
    

    
    
