from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='images_created'
    )
    title = models.CharField(
        max_length=200
    )
    slug = models.SlugField(
        max_length=200,
        blank=True
    )
    url = models.URLField()
    image = models.ImageField(
        upload_to='images/%Y/%m/%d/'
    )
    description = models.TextField(
        blank=True
    )
    created = models.DateField(
        auto_now=True,
        db_index=True
    )
    user_like = models.ManyToManyField(
        User,
        blank=True,
        related_name='images_liked'
    )

    total_likes = models.PositiveIntegerField(
        db_index=True,
        default=0
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'images:detail',
            args=[
                self.id,
                self.slug
            ]
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)