
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import registration, Patient, Doctor, Appointment, Medicine, MedicalReport, Billing
from django.contrib import messages
from .forms import RegisterForm, PatientForm, DoctorForm, AppointmentForm, MedicineForm, MedicalReportForm, BillingForm

 
def register(request):
    form = RegisterForm()

    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully")
            return redirect('login')
    return render(request, 'register.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = registration.objects.filter(
            username__iexact=username,
            password=password
        ).first()

        if user:
            request.session['user'] = user.username
            request.session['role'] = user.role
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def home(request):
    if 'user' not in request.session:
        return redirect('login')

    context = {
        'name': request.session['user'],
        'role': request.session['role'],
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
        'appointment_count': Appointment.objects.count(),
        'medicine_count': Medicine.objects.count(),
        'billing_count' : Billing.objects.count(),
        'recent_appointments': Appointment.objects.order_by('-id')[:5],
    }

    return render(request, 'home.html', context)

def logout(request):
    request.session.flush()
    return redirect('login')


def add_patient(request):
    if request.session.get('role') not in ['Admin','Receptionist']:
        return redirect('home')
    form = PatientForm()

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient Added Successfully")
            return redirect('add_patient')

    return render(request, 'add_patient.html', {'form': form})


def view_patient(request):
    search = request.GET.get('search')
    if search:
        patients = Patient.objects.filter(patient_name__icontains=search)
    else:
        patients = Patient.objects.all()
    return render(request, 'view_patient.html', {
        'patients': patients,
        'role': request.session.get('role')
    })


def edit_patient(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    patient = Patient.objects.get(id=id)

    form = PatientForm(instance=patient)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            messages.success(request, "Patient Updated Successfully")
            return redirect('view_patient')

    return render(request, 'edit_patient.html', {'form': form})

def delete_patient(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    patient = Patient.objects.get(id = id)
    patient.delete()
    messages.success(request, "patient deleted successfully")
    return redirect('view_patient')


def add_doctor(request):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    form = DoctorForm()

    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully")
            return redirect('add_doctor')

    return render(request, 'add_doctor.html', {'form': form})

def view_doctor(request):
    search = request.GET.get('search')
    if search:
        doctors = Doctor.objects.filter(doctor_name__icontains=search)
    else:
        doctors = Doctor.objects.all()
    return render(request, 'view_doctor.html',{
        'doctors': doctors,
        'role': request.session.get('role')
    })
  

def edit_doctor(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    doctor = Doctor.objects.get(id=id)

    form = DoctorForm(instance=doctor)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)

        if form.is_valid():
            form.save()
            messages.success(request, "Doctor Updated Successfully")
            return redirect('view_doctor')

    return render(request, 'edit_doctor.html', {'form': form})

     
def delete_doctor(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    messages.success(request, "Doctor Deleted Successfully")
    return redirect('view_doctor')


def add_appointment(request):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Appointment Booked Successfully")
            return redirect('add_appointment')

    return render(request, 'add_appointment.html', {'form': form})

def view_appointment(request):
    search = request.GET.get('search')
    if search:
        appointments = Appointment.objects.filter(
            Q(patient__patient_name__icontains=search) |
            Q(doctor__doctor_name__icontains=search)
        )
    else:
        appointments = Appointment.objects.all()

    return render(request, 'view_appointment.html', {
        'appointments': appointments,
        'role': request.session.get('role')

    })

def edit_appointment(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    appointment = Appointment.objects.get(id=id)

    form = AppointmentForm(instance=appointment)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            messages.success(request, "Appointment Updated Successfully")
            return redirect('view_appointment')

    return render(request, 'edit_appointment.html', {'form': form})

def delete_appointment(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    messages.success(request, "Appointment Deleted Successfully")
    return redirect('view_appointment')

def add_medicine(request):
    form = MedicineForm()
    if request.session.get('role') != 'Admin':
        return redirect('home')

    if request.method == "POST":
        form = MedicineForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Medicine Added Successfully")
            return redirect('add_medicine')

    return render(request, 'add_medicine.html', {'form': form})


def view_medicine(request):
    if request.session.get('role') != 'Admin': 
        return redirect('home')
    search = request.GET.get('search')
    if search:
        medicines = Medicine.objects.filter(medicine_name__icontains=search)
    else:
        medicines = Medicine.objects.all()
    return render(request, 'view_medicine.html', {
        'medicines': medicines
    })


def edit_medicine(request, id):
    if request.session.get('role') != 'Admin': 
        return redirect('home')
    medicine = Medicine.objects.get(id=id)

    form = MedicineForm(instance=medicine)

    if request.method == "POST":
        form = MedicineForm(request.POST, instance=medicine)

        if form.is_valid():
            form.save()
            messages.success(request, "Medicine Updated Successfully")
            return redirect('view_medicine')

    return render(request, 'edit_medicine.html', {'form': form})

def delete_medicine(request, id):
    if request.session.get('role') != 'Admin': 
        return redirect('home')
    medicine = Medicine.objects.get(id=id)
    medicine.delete()

    messages.success(request, "Medicine Deleted Successfully")
    return redirect('view_medicine')

def add_medical_report(request, id):
    if request.session.get('role') not in ['Admin', 'Doctor']:
        return redirect('home')
    patient = Patient.objects.get(id=id)

    form = MedicalReportForm()

    if request.method == "POST":
        form = MedicalReportForm(request.POST, request.FILES)

        if form.is_valid():
            report = form.save(commit=False)
            report.patient = patient
            report.save()

            messages.success(request, "Medical Report Uploaded Successfully")

            return redirect('patient_reports', id=patient.id)

    return render(request, 'add_medical_report.html', {
        'form': form,
        'patient': patient
    })

def patient_reports(request, id):
    if request.session.get('role') not in ['Admin', 'Doctor']:
        return redirect('home')

    patient = Patient.objects.get(id=id)

    reports = MedicalReport.objects.filter(patient=patient)

    return render(request, 'patient_reports.html', {
        'patient': patient,
        'reports': reports
    })


def delete_medical_report(request, id):
    if request.session.get('role') not in ['Admin', 'Doctor']:
        return redirect('home')

    report = MedicalReport.objects.get(id=id)

    patient_id = report.patient.id

    report.delete()

    messages.success(request, "Medical Report Deleted Successfully")

    return redirect('patient_reports', id=patient_id)


def add_billing(request):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')

    form = BillingForm()

    if request.method == "POST":

        form = BillingForm(request.POST)

        if form.is_valid():
            bill = form.save(commit=False)

            bill.total_amount = bill.consultation_fee + bill.medicine_cost

            bill.save()

            messages.success(request, "Bill Added Successfully")

            return redirect('add_billing')

    return render(request, 'add_billing.html', {'form': form})



def view_billing(request):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')

    bills = Billing.objects.all().order_by('-id')

    return render(request, 'view_billing.html', {
        'bills': bills
    })


def delete_billing(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')

    bill = Billing.objects.get(id=id)

    bill.delete()

    messages.success(request, "Bill Deleted Successfully")

    return redirect('view_billing')

def billing_receipt(request, id):
    if request.session.get('role') not in ['Admin', 'Receptionist']:
        return redirect('home')

    bill = Billing.objects.get(id=id)

    return render(request, 'billing_receipt.html', {
        'bill': bill
    })