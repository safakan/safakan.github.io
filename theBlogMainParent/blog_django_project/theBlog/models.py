from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField


# locate the images used in the posts
def get_upload_location_post_images(instance, filename):
    return f'blog_images/posts/{instance.id}/{filename}'


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    



class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownxField()
    created_at = models.DateTimeField(default=timezone.now, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to=get_upload_location_post_images, null=True, blank=True)
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    


