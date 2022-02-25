from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)
    
    def __str__(self):
        return self.user.get_username()
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=100, unique=False)
    Amount = models.DecimalField(max_digits=3, decimal_places=1)
    Danger = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    image = models.ImageField(max_length=255, null=True, upload_to="img/")

    ingredients = models.ManyToManyField(Ingredients, blank=True)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def get_image(self):
        if self.image:
            return 'http://localhost:8000' + self.image
        return ''
            
        
        
        