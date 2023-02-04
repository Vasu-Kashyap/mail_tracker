from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse
from PIL import Image


# Create your views here.
# def send(request):
#     try:
#         send_mail(subject, message, settings.EMAIL_HOST_USER, ['vasukashyap01@gmail.com'])
#     except BadHeaderError:
#         return HttpResponse('Invalid header found.')
#     return redirect("index")


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email_address']
        subject = request.POST['subject']
        message = request.POST['message']

        body = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        ins = mail_track.objects.create(sender_email=settings.EMAIL_HOST_USER, receiver_email='vasukashyap01@gmail.com')
        url = 'https://0ea9-2405-201-4007-8030-84c-7667-14a1-c97d.in.ngrok.io'+reverse("image_load", kwargs={'id': ins.id})
        message = '<img src=' + url + 'height="0px" width="0px"/>'.join(body.values())
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['vasukashyap01@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("index")

    form = ContactForm()
    return render(request, "contact.html", {'form': form})


def image_load(request, id):
    inst = mail_track.objects.get(id=id)
    inst.is_opened = True
    inst.counter += 1
    inst.save()
    print("\nImage Loaded\n")
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response
