from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=20)
    image=models.ImageField(upload_to='project/images/')
    url=models.URLField(blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title