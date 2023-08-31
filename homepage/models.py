from django.db import models

# Create your models here.
class FileUpload(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgFile = models.ImageField(null=True, upload_to='uploads/', blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
