from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):

    APPROVED = (
        ('NO','NO'),
        ('YES', 'YES')
    )

    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    skills = models.ManyToManyField(Skills, blank=True)
    approved = models.CharField(max_length=200, choices=APPROVED, default= APPROVED[0])

    def __str__(self):
        return self.name


class Event(models.Model):

    STATUS = (
        ('Draft','Draft'),
        ('Ongoing', 'Ongoing'),   
        ('Finished', 'Finished')
    )

    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True, blank = True)
    principal = models.CharField(max_length=200, null=True, blank = True)
    status = models.CharField(max_length=200, choices=STATUS, null=True)
    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    cmph = models.FloatField(null=True, blank=True) #default for EventHandler
    hpd = models.FloatField(null=True, blank=True) #default for EventHandler
    dcfe = models.FloatField(null=True, blank=True) #default for EventHandler
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name



class EventHandler(models.Model):

    employee = models.ForeignKey(Employee, null = True ,on_delete = models.SET_NULL)
    event = models.ForeignKey(Event, null = True, on_delete = models.SET_NULL)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    cpmh = models.FloatField(null = True)
    hpd = models.FloatField(null = True) 
    dcfe = models.FloatField(null = True)
    emp_hours = models.FloatField(null = True)
    addition = models.FloatField(null=True, blank=True)