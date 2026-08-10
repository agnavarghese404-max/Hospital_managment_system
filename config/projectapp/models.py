from django.db import models

ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Receptionist', 'Receptionist'),
        ('Doctor', 'Doctor'),
        ]
# Create your models here.
class registration(models.Model):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Receptionist'
    )

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
    STATUS_CHOICES = [
    ('Confirmed', 'Confirmed'),
    ('Pending', 'Pending'),
    ('Cancelled', 'Cancelled'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

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

class MedicalReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    report_title = models.CharField(max_length=100)
    report_type = models.CharField(max_length=50)
    report_file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.report_title


class Billing(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    medicine_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    bill_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Bill - {self.patient.patient_name}"