from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from main_app.models import CustomUser
from datetime import datetime, timedelta
import json
from .models import *
from .form import *


def patient_home(request):
    return render(request, 'patient_template/patient_home.html')


def patient_profile(request):
    patient =  get_object_or_404(Patient, admin=request.user)
    form = PatientForm(request.POST or None, request.FILES or None, instance=patient)
    if request.method == "POST":
        if form.is_valid():
            try:
                user = CustomUser.objects.get(id=patient.admin.id)
                user.first_name = form.cleaned_data.get("first_name") 
                user.last_name = form.cleaned_data.get("last_name")
                user.email = form.cleaned_data.get("email") 
                password = form.cleaned_data.get("password") or None
                if password != None:
                    user.set_password(password)   
                       
                user.save()
                form.save()
                messages.success(request, "Cập nhật thành công")
                return HttpResponseRedirect(reverse("patient_profile"))
            except:
                messages.error(request, "Cập nhật thất bại")
                return HttpResponseRedirect(reverse("patient_profile"))
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
            
    return render(request,"patient_template/patient_profile.html", {'form': form}) 


def test_result(request):
    test_result = get_object_or_404(TestResult, patient=request.user.patient) 
    if test_result.test_day == None:
        test_result = None
    return render(request,"patient_template/test_result.html", {'test_result': test_result}) 


def medical_history(request):
    history = MedicalHistory.objects.filter(patient=request.user.patient).order_by('-date')
    schedules = TreatmentSchedule.objects.filter(patient=request.user.patient)
    progress = 0
    count = 0
    for schedule in schedules:
       progress += schedule.get_progress()
       count += 1 
    if count == 0:
        progress = 0
    else:
        progress = progress / count
    return render(request, 'patient_template/medical_history.html', {'history': history, 'progress': round(progress/count, 2)})




def patient_feedback(request):
    form = FeedbackPatientForm(request.POST or None, request.FILES or None)
    patient = get_object_or_404(Patient, admin_id=request.user.id)
    feedbacks = FeedbackPatient.objects.filter(patient=patient)

    if request.method == 'POST':
        if form.is_valid():
            try:
                fb = form.save(commit=False)
                fb.patient = patient
                if not fb.rating:
                    fb.rating = 0
                fb.save()
                messages.success(request, "Phản hồi đã được gửi")
                return HttpResponseRedirect(reverse('patient_feedback'))
            except:
                messages.error(request, "Gửi phản hồi không thành công")
        else:
            messages.error(request, "Hãy đáp ứng mọi yêu cầu")
    return render(request, "patient_template/patient_feedback.html", {'form': form, 'feedbacks': feedbacks})

def patient_calendar(request):
    events = TreatmentSchedule.objects.filter(patient=request.user.patient).order_by('start_date')

    # collect all event by days
    event_dict = {}
    for event in events:
        
        current_date = event.start_date.date()
        real_date_now = timezone.now().date()

        if (event.end_date.date() - current_date) <= timedelta(days=1) and event.label == 'Cuộc hẹn' and current_date >= real_date_now:
            if current_date not in event_dict:
                event_dict[current_date] = []
            event_dict[current_date].append(event)
            continue   

        while current_date <= event.end_date.date():
            if current_date >= real_date_now:
                if current_date not in event_dict:
                    event_dict[current_date] = []
                event_dict[current_date].append(event)

            current_date += timedelta(days=1)

    event_dict = dict(sorted(event_dict.items()))

    return render(request, 'patient_template/works.html', {'event_dict': event_dict})


@csrf_exempt
def check_email_exist(request):
    body = json.loads(request.body)

    user = CustomUser.objects.filter(email=body['email']).exists()
    if user:
        return JsonResponse("True", safe=False)
    
    return JsonResponse("False", safe=False)