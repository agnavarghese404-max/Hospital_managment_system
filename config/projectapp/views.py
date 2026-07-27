
from django.shortcuts import render,redirect
from .models import registration, Patient, Doctor, Appointment, Medicine
from django.contrib import messages
from .forms import RegisterForm, PatientForm, DoctorForm, AppointmentForm, MedicineForm

 
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
            username=username,
            password=password
        ).first()

        if user:
            request.session['user'] = user.username
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'login.html')

def home(request):
    if 'user' not in request.session:
        return redirect('login')
    
    return render(request, 'home.html',{
        'name' : request.session['user']
    })

def logout(request):
    request.session.flush()
    return redirect('login')


def add_patient(request):
    form = PatientForm()

    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient Added Successfully")
            return redirect('add_patient')

    return render(request, 'add_patient.html', {'form': form})
def view_patient(request):
    patients = Patient.objects.all()

    return render(request, 'view_patient.html', {
        'patients': patients
    })

def edit_patient(request, id):
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
    patient = patient.objects.get(id = id)
    patient.delete()
    messages.success(request, "patient deleted successfully")
    return redirect('view_patient')


def add_doctor(request):
    form = DoctorForm()

    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully")
            return redirect('add_doctor')

    return render(request, 'add_doctor.html', {'form': form})

def view_doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'view_doctor.html',{
        'doctors': doctors
    })
  

def edit_doctor(request, id):
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
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    messages.success(request, "Doctor Deleted Successfully")
    return redirect('view_doctor')


def add_appointment(request):
    form = AppointmentForm()

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Appointment Booked Successfully")
            return redirect('add_appointment')

    return render(request, 'add_appointment.html', {'form': form})

def view_appointment(request):
    appointments = Appointment.objects.all()

    return render(request, 'view_appointment.html', {
        'appointments': appointments
    })

def edit_appointment(request, id):
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
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    messages.success(request, "Appointment Deleted Successfully")
    return redirect('view_appointment')

def add_medicine(request):
    form = MedicineForm()

    if request.method == "POST":
        form = MedicineForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Medicine Added Successfully")
            return redirect('add_medicine')

    return render(request, 'add_medicine.html', {'form': form})


def view_medicine(request):
    medicines = Medicine.objects.all()

    return render(request, 'view_medicine.html', {
        'medicines': medicines
    })

def edit_medicine(request, id):
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
    medicine = Medicine.objects.get(id=id)
    medicine.delete()

    messages.success(request, "Medicine Deleted Successfully")
    return redirect('view_medicine')