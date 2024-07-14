from django.db import models
from datetime import date

# Create your models here.

class Coil(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    length = models.FloatField()
    width = models.FloatField()
    thickness = models.FloatField()
    net_weight = models.FloatField()
    wasted = models.FloatField()
    actions = models.ManyToManyField('CoilActionSlit', related_name='coils', blank=True)

class Coil_Action_Slit(models.Model): # if this action done then you cant do any other action because it uses the entire length of the coil
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    items = models.IntegerField() # this is inputed
    length = models.FloatField() # As per the coil's length, it should inherit it
    width = models.FloatField() # As per the coil's thickness, there's an associated width
    used = models.FloatField() # length
    date = models.DateField(default=date.today)  
    # based of the thichkness, theres a certain number of slitted items. But, to calculate the wasted length, then its the length/width rounded down, then that number should be compared to the number of items, if it's less, then multiple the difference by the width and add the extra remainder length, if its not less then only put the extra remainder length  

class Coil_Action_SC52(models.Model):
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    items = models.IntegerField() # this is inputed
    length = 1220 # by default
    width = 52 # by default
    used = models.FloatField() # length * width * items
    date = models.DateField(default=date.today) 
    # after the coil is used up fully, it adds all the used lengths, and if they're not as long as the coil lengths, then the extra coil was wasted

class Coil_Action_SC92(models.Model):
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    items = models.IntegerField() # this is inputed
    length = 1220 # by default
    width = 92 # by default
    used = models.FloatField() # length * width * items
    date = models.DateField(default=date.today) 
    # after the coil is used up fully, it adds all the used lengths, and if they're not as long as the coil lengths, then the extra coil was wasted

class Coil_Action_Perforat(models.Model):
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    items = models.IntegerField() # this is inputed
    length = models.FloatField() # this is inputed
    width = 1220 # by default
    used = models.FloatField() # length * width * items
    date = models.DateField(default=date.today) 

class Coil_Action_Sheet(models.Model):
    coil = models.ForeignKey(Coil, on_delete=models.CASCADE)
    items = models.IntegerField() # this is inputed
    length = models.FloatField() # this is inputed
    width = models.FloatField() # this is inputed
    used = models.FloatField() # length * width * items
    date = models.DateField(default=date.today) 