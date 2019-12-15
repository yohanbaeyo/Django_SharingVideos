from django.db import models
from hitcount.models import HitCountMixin

# Create your models here.
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user, filename)

class Video(models.Model, HitCountMixin):
    title = models.CharField(max_length=20)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=user_directory_path, default="no_image.png")
    videoURL = models.CharField(blank=True, null=True, max_length=50)
    videoFile = models.FileField(blank=True, null=True)
    user = models.TextField(blank=True)
    publishedDate = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return "["+str(self.pk)+"]"+str(self.title)