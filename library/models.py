from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.core.exceptions import ValidationError

class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id


class Book(models.Model):
    catchoice= [
        ('music', 'Music'),
        ('philosophy', 'Philosophy'),
        ('religion', 'Religion'),
        ('business', 'Business'),
        ('history', 'History'),
        ('science', 'Science'),
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('romance', 'Romance'),
        ('health','Health')
        ]
    name=models.CharField(max_length=30)
    SrNo=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    copies = models.IntegerField(default=1)

    def clean(self):
        if self.copies > 10:
            raise ValidationError('A book can have only up to 10 copies.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    class Meta:
        unique_together = [['name', 'SrNo']]
    def __str__(self):
        return str(self.name)+"["+str(self.SrNo)+']'


def get_expiry():
    return datetime.today() + timedelta(days=30)
class IssuedBook(models.Model):
    enrollment=models.CharField(max_length=30)
    SrNo=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment
