from django.db import models
from django.contrib.auth.models import User

class Zone(models.Model):
    name = models.CharField(max_length = 64)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Sub_Zone(models.Model):
    owner = models.ForeignKey(User)
    prefix = models.CharField(max_length = 32)
    super_zone = models.ForeignKey(Zone)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        if self.prefix == '@':
            return str(self.super_zone)
        return self.prefix + '.' + str(self.super_zone)

class Record_Type(models.Model):
    name = models.CharField(max_length = 8)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Record(models.Model):
    prefix = models.CharField(max_length = 32)
    type = models.ForeignKey(Record_Type)
    zone = models.ForeignKey(Sub_Zone)
    context = models.CharField(max_length = 128)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        if self.prefix == '@':
            return str(self.zone) + ' ' + str(self.type) + ' ' + self.context
        return self.prefix + '.' + str(self.zone) + ' ' + str(self.type) + ' ' + self.context

