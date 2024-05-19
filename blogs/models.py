from django.db import models
from django.urls import reverse
from users.models import Users


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )
    body = models.TextField()

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
