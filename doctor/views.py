from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Appointment
# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = "index.html"
    
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully!")

class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self,request):
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        message=request.POST.get("request")

        appointment=Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )
        appointment.save()

        messages.add_message(request,messages.SUCCESS,f"Thanks {fname} for making an appointment")
        return HttpResponseRedirect(request.path)

class ManageAppointmentTemplateView(TemplateView):
    template_name = "manage-appointments.html"
    login_required=True






