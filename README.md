# 🏥 Hospital Management System

A web-based Hospital Management System built using **Python and Django**. The system helps hospital staff manage patients, doctors, appointments, medicines, medical reports, and billing through a centralized interface.

The application also includes **role-based access control** for Admin, Doctor, and Receptionist users.

---

## 📌 Features

### 🔐 Authentication & Role-Based Access

- Secure login system
- Role-based access for:
  - Admin
  - Doctor
  - Receptionist
- Public registration is restricted
- Only Admin can register new staff accounts
- Role-based access to system features and actions
- Logout functionality

### 🏠 Dashboard

- Centralized dashboard
- Displays system information based on user access
- Shows counts of patients, doctors, appointments, pharmacy, and billing
- Shows recent appointments
- Quick access to available features

### 👤 Patient Management

- Add patients
- View patient details
- Edit patient information
- Delete patients
- Search patients by name
- View patient medical records

### 👨‍⚕️ Doctor Management

- Add doctors
- View doctor details
- Edit doctor information
- Delete doctors
- Search doctors by name
- Role-based restrictions for doctor management actions

### 📅 Appointment Management

- Book appointments
- View appointments
- Edit appointments
- Delete appointments
- Search appointments by patient or doctor
- Appointment status management:
  - Confirmed
  - Pending
  - Cancelled
- Appointment clash checking

### 💊 Medicine Management

- Add medicines
- View medicines
- Edit medicine details
- Delete medicines
- Search medicines by name

### 📄 Medical Reports

- Add medical reports for patients
- Upload medical report files
- View patient medical records
- View and download reports
- Delete reports
- Access reports through the patient records section
- Role-based access to medical reports

### 🧾 Billing

- Generate bills
- View billing records
- Generate billing receipts
- Delete billing records

---

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

## 📂 Project Structure

```text
Hospital-Management-System/
│
├── config/                 # Django project configuration
├── projectapp/             # Main application
│   └── migrations/         # Database migrations
├── static/                 # Static files
│   └── assets/
├── templates/              # HTML templates
├── media/                  # Uploaded medical reports
├── screenshots/            # README screenshots
├── manage.py
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

```bash
git clone https://github.com/agnavarghese404-max/Hospital_managment_system.git
cd Hospital_managment_system
python -m venv env
env\Scripts\activate
pip install django
cd config
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📸 Screenshots

### Admin Dashboard
![Admin Dashboard](screenshots/admin1.png)

### Doctor Dashboard
![Doctor Dashboard](screenshots/doctot.png)

### Receptionist Dashboard
![Receptionist Dashboard](screenshots/receptionist.png)

### Patient List
![Patient List](screenshots/screenshot2.png)

### Doctor List
![Doctor List](screenshots/screenshot3.png)

### Appointment List
![Appointment List](screenshots/screenshot4.png)

### Medicine List
![Medicine List](screenshots/screenshot5.png)

### Billing Records
![Billing Records](screenshots/screenshot6.png)

### Add Patient
![Add Patient](screenshots/screenshot7.png)

### Add Doctor
![Add Doctor](screenshots/screenshot8.png)

### Book Appointment
![Book Appointment](screenshots/screenshot9.png)

### Add Medicine
![Add Medicine](screenshots/screenshot10.png)

### Add Billing
![Add Billing](screenshots/screenshot11.png)

### Patient Medical Records
![Patient Medical Records](screenshots/screenshot12.png)

### Register Staff (Admin only)
![Register Staff](screenshots/screenshot13.png)

---

## 🎯 Future Improvements

- Online payment for billing
- Laboratory module
- Prescription management
- Email notifications
- PDF report generation
- Filters for appointments by date or status
- Patient login portal
- REST API using Django REST Framework