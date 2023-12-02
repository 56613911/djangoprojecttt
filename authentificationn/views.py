# nomapp/views.py
from .forms import CustomAuthenticationForm
 
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, CustomAuthenticationForm  
# authentificationn/views.py
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'authentificationn/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        # Redirect logic here
        return 'home'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentificationn/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        print("POST request received")
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            print("Form is valid")
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                print("User is not None")
                login(request, user)
                return redirect('home')  # Adjust this URL
        else:
            print(form.errors) 
            print("Form errors")  # Add this line to print form errors for debugging
    else:
        form = CustomAuthenticationForm()

    return render(request, 'authentificationn/login.html', {'form': form})




from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')
