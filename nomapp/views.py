from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate



# views.py

from django.shortcuts import render
from .models import DoctorAvailability

# nomapp/views.py
from django.shortcuts import HttpResponse
from nomapp.models import MedicalReport

# nomapp/views.py
# nomapp/views.py
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required  # Import the decorator
from nomapp.models import MedicalReport

from django.shortcuts import redirect
from django.contrib.auth.views import LoginView

def custom_login_view(request, *args, **kwargs):
    # If the user is already authenticated, redirect to the home page
    if request.user.is_authenticated:
        return redirect('home')

    # Otherwise, use the built-in LoginView for authentication
    return LoginView.as_view(template_name='authentificationn/login.html')(request, *args, **kwargs)


@login_required  # Apply the decorator to ensure the user is authenticated


def trigger_notification(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Assuming the logged-in user is the patient
        patient = request.user
        # Check if the user has 'medic' attribute
        doctor = request.user.medic if hasattr(request.user, 'medic') else None
    else:
        # If the user is not authenticated, handle it accordingly
        patient = None
        doctor = None

    # Simulate the creation of a new medical report
    report = MedicalReport.objects.create(
        patient=patient,
        doctor=doctor,
        report_date='2023-11-11',
        symptoms='Test symptoms',
        diagnosis='Test diagnosis',
        treatment='Test treatment',
    )

    return HttpResponse("Notification triggered successfully.")



def search_doctors(request):
    if request.method == 'GET':

        available_doctors = DoctorAvailability.objects.filter(monday_morning=True)

        context = {
            'available_doctors': available_doctors,
        }

        return render(request, 'search_doctors.html', context)



def Home(request):
    return render(request, 'home.html')

def Contact(request):
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message_subject = request.POST.get('message-Subject')
        u_message = request.POST.get('u-message')
        send_mail (
            message_subject,
            u_message,
            message_email,
            ['samaraouadi7@gmail.com'],  # Make sure to use a list for recipient(s)
        )

        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html')

def Services(request):
    # Add logic to retrieve and display services information
    return render(request, 'services.html')

def Doctors(request):
    # Add logic to retrieve and display information about doctors
    return render(request, 'doctors.html')

def About(request):
    # Add logic to retrieve and display information about the healthcare facility
    return render(request, 'about.html')

def Blog(request):
    # Add logic to retrieve and display blog posts
    return render(request, 'blog.html')
# nomapp/views.py


# nomapp/views.py




from django.shortcuts import render, redirect


from .forms import SignupForm




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:    
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


# views.py

from django.shortcuts import render
from .models import DoctorAvailability
# views.py
from django.shortcuts import render
from .models import DoctorAvailability

# views.py
from django.shortcuts import render
from .models import DoctorAvailability

# Dans votre vue (views.py)
def search_doctors(request):
    if request.method == 'POST':
        monday_morning = request.POST.get('monday_morning', False) == 'on'
        monday_afternoon = request.POST.get('monday_afternoon', False) == 'on'

        print(f"Searching for doctors: Monday Morning={monday_morning}, Monday Afternoon={monday_afternoon}")

        available_doctors = DoctorAvailability.objects.filter(monday_morning=monday_morning, monday_afternoon=monday_afternoon)

        context = {
            'available_doctors': available_doctors,
        }

        return render(request, 'search_doctors.html', context)
    else:
        return render(request, 'search_form.html')




