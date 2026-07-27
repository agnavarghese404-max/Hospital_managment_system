from django.db import models


# Create your models here.
class registration(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.doctor_name



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.patient} - {self.doctor}"


class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.medicine_name
