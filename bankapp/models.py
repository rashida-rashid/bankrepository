from django.db import models

# Create your models here.
class Districts(models.Model):
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return self.district_name


class Branches(models.Model):
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Form(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=100)
    phoneNo = models.IntegerField()
    emailId = models.EmailField()
    address = models.TextField(max_length=300)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE,default = True)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE,default = True)
    accountType = models.TextField(max_length=250)
    materials = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
