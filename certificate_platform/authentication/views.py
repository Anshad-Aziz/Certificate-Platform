from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser
from django.core.exceptions import ValidationError

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'authentication/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            try:
                user = CustomUser.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    company_name=company_name,
                    phone_number=phone_number,
                    is_company_admin=True
                )
                login(request, user)
                return redirect('dashboard:dashboard')
            except ValidationError as e:
                messages.error(request, str(e))
    
    return render(request, 'authentication/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # For now, display a message; email functionality can be added later
            messages.success(request, 'Password reset instructions have been sent to your email.')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Please enter a valid email address.')
    else:
        form = PasswordResetForm()
    
    return render(request, 'authentication/password_reset.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.phone_number = request.POST.get('phone_number', user.phone_number)
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('authentication:profile')
    
    return render(request, 'authentication/profile.html', {'user': request.user})

@login_required
def company_profile_view(request):
    if request.method == 'POST':
        user = request.user
        user.company_name = request.POST.get('company_name', user.company_name)
        user.save()
        messages.success(request, 'Company profile updated successfully.')
        return redirect('authentication:company_profile')
    
    return render(request, 'authentication/company_profile.html', {'user': request.user})