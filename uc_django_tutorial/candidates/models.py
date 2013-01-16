from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=120)
    about = models.TextField()

    def __unicode__(self):
        return self.name
