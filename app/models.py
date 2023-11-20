from django.db import models


class Todolist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def __str__(self):
        return (f"{self.item}")
