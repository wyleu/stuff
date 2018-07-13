from django.db import models
import uuid


class Base(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    z = models.IntegerField(default=0)
    r = models.FloatField(default=1.0)
    g = models.FloatField(default=1.0)
    b = models.FloatField(default=1.0)



class Node(Base):
    class Meta:
        ordering = ['modified']


