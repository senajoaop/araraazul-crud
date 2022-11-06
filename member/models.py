from django.db import models


class Member(models.Model):  
    mId = models.CharField(max_length=20)  
    mName = models.CharField(max_length=100)  
    mEmail = models.EmailField()  
    mContact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "member"
