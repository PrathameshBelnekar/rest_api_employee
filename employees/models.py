from django.db import models




class Employee(models.Model):
    STATUS_CHOICE = [
        ("Active", 'Active'),
        ('Deactive', 'Deactive'),
    ]
    emp_name = models.CharField(max_length=255 , null = True)
    joining_date = models.DateField(null = True)
    salary = models.IntegerField(null = True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICE , default='Active', null = True)

    def __str__(self):
        return self.emp_name


