from django import forms
from .models import registration
class RegisterForm(forms.ModelForm):
    class Meta:
        model = registration
        fields=['username','email','password','role']

    def clean_username(self):
        username=self.cleaned_data['username']
        if registration.objects.filter(username=username) .exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if registration.objects.filter(email=email) .exists():
            raise forms.ValidationError("Email already exists")
        return email


from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

from .models import Doctor
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }

from .models import Medicine
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
from .models import MedicalReport
class MedicalReportForm(forms.ModelForm):

    class Meta:
        model = MedicalReport
        fields = [
            'report_title',
            'report_type',
            'report_file'
        ]

from .models import Billing
class BillingForm(forms.ModelForm):

    class Meta:
        model = Billing
        exclude = ['total_amount', 'bill_date']