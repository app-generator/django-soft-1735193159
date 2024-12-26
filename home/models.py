# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Testmodel(models.Model):

    #__Testmodel_FIELDS__
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True, default=timezone.now)
    amount = models.IntegerField(null=True, blank=True)

    #__Testmodel_FIELDS__END

    class Meta:
        verbose_name        = _("Testmodel")
        verbose_name_plural = _("Testmodel")


class Test2Model(models.Model):

    #__Test2Model_FIELDS__
    test = models.ForeignKey(TestModel, on_delete=models.CASCADE)
    desc = models.TextField(max_length=255, null=True, blank=True)

    #__Test2Model_FIELDS__END

    class Meta:
        verbose_name        = _("Test2Model")
        verbose_name_plural = _("Test2Model")



#__MODELS__END
