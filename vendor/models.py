from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.


STATE_CHOICE = (
    ('Province No. 1', 'Province No. 1'),
    ('Madhesh Province', 'Madhesh Province'),
    ('Bagmati Province', 'Bagmati Province'),
    ('Gandaki Province', 'Gandaki Province'),
    ('Lumbini Province', '	Lumbini Province'),
    ('Karnali Province', 'Karnali Province'),
     ('Sudurpashchim Province', 'Sudurpashchim Province'),
)
class Resume(models.Model):
    companyName = models.CharField(max_length=100)
    company_register_number= models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    businesstype= models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="products")
    company_register_document = models.FileField(upload_to="document")




