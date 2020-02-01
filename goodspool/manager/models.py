from django.db import models

# Create your models here.

class Trip(models.Model):

    transporter_id = ForeignKey(#, on_delete = models.CASCADE)
    start = TextField() 
    route = TextField() 
    destination = TextField() 
    trip_date = DateField()
    start_time = DateTimeField()


    