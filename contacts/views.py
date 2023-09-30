from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url = 'login')
def contacts(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        message = message
        message_body = 'Name: ' + firstname + '' + lastname + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        
        send_mail(
            message,
            message_body,
            settings.EMAIL_HOST_USER,
            ['ezemosesjohn21997@gmail.com'],
            fail_silently=False
        )
        message ="Hello!, We've received your message. We would get back to you shortly!"
        return render(request, 'movies/contact.html', {'message': message})
    return render(request, 'movies/contact.html')