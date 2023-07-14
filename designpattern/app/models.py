from django.db import models
import uuid
# Create your models here.
def generate_car_model_id():
    # Generate a unique ID and return the first 5 characters
    return str(uuid.uuid4())[:5]

class Car(models.Model):

    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} ({self.color})"
    
class CarModel(models.Model):
    car_model_id = models.CharField(max_length=5, default=generate_car_model_id)
    car_name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car,on_delete=models.CASCADE)
    car_details =  models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.car_name} ({self.car_id})"
    


    