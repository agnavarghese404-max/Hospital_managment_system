from django.contrib import admin
from .models import registration, Patient, Doctor, Appointment, Medicine

admin.site.register(registration)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Medicine)