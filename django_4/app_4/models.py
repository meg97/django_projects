from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICE = (
    (0, "New"),
    (1, "Doing"),
    (2, "Done"),
)


class NewTask(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICE, default="0")
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name