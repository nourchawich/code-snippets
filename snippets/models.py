from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse

TAG_MAX_LEN = 30
SNIPPET_MAX_TAGS = 5


class Snippet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, db_index=True)
    code = models.TextField()
    tags = ArrayField(models.CharField(max_length=TAG_MAX_LEN), size=SNIPPET_MAX_TAGS)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f'{self.id}: "{self.title}" by {self.user}'

    def get_absolute_url(self):
        """Returns snippet url to be used as redirect url for UpdateView"""
        return reverse('snippets:detail', kwargs={'pk': self.pk})
