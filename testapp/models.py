from django.db import models


# Create your models here.
class ParentModel(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return "%s" % self.name


class ChildClass(models.Model):

    name = models.CharField(max_length=20)
    parent = models.ForeignKey(ParentModel)

    def __unicode__(self):
        return "%s" % self.name