from django.db import models

from pyuploadcare.dj import FileField


class Candidate(models.Model):
    name = models.CharField(max_length=120)
    about = models.TextField()

    resume = FileField(blank=True, null=True)

    def __unicode__(self):
        return self.name
