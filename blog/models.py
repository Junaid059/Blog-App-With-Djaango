from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class PostObjects(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    excerpt = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True)
    published_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='Published')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1,related_name='posts')   
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  
    objects = models.Manager() # The default manager.
    postobjects = PostObjects() # Our custom manager.

    class Meta:
        ordering =['-published_at']

    def __str__(self):
        return self.title    