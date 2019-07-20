from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=255)
    staff_only = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
