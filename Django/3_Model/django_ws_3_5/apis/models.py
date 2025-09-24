from django.db import models
from django.core.validators import URLValidator, MinLengthValidator


class APIInfo(models.Model):
    name = models.TextField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(
        validators=[
            URLValidator(),
            MinLengthValidator(15)],
        max_length=60)
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True, null=True)