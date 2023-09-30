from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method  == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('home')
        else:
            error_message = 'Invalid credentials! login with correct details.'
            return render(request, 'auth/login.html', {'error_message': error_message})
    return render(request, 'auth/login.html')

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                error_message = 'Username already exists, signup with correct details'
                return render(request, 'auth/signup.html', {'error_message': error_message})
            else: 
                if User.objects.filter(email=email).exists():
                    error_message = 'Email already exists, signup with correct details'
                    return render(request, 'auth/signup.html', {'error_message': error_message})
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    user.save()
                    messages.success(request, 'account created successfully')
                    return redirect('login')    
        else:
            error_message = 'Passwords do not match, signup with correct details'
            return render(request, 'auth/signup.html', {'error_message': error_message})
    return render(request, 'auth/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
