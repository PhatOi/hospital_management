from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientProfileForm, RegisterForm, FeedbackForm 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import Profile, Feedback, MedicalDate  
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login_user.html', {'form': form})

@login_required 
def logout_view(request):
        logout(request)
        return redirect('login')



@login_required
def create_profile(request):
    if Profile.objects.filter(user=request.user).exists():
        # Nếu đã có, chuyển hướng đến trang chỉnh sửa hoặc xóa hồ sơ cũ
        return HttpResponse('Bạn đã tạo hồ sơ trước đó')
    else:
        # Nếu chưa, hiển thị form tạo hồ sơ mới
        if request.method == 'POST':
            form = PatientProfileForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('homepage')
        else:
            form = PatientProfileForm()
        return render(request, 'create_profile.html', {'form': form})
    '''
    if request.method == 'POST':
        form = PatientProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('homepage')
    else:
        form = PatientProfileForm()
    return render(request, 'create_profile.html', {'form': form})
'''

@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        return render(request, 'view_profile.html', {'profile': profile})
    except Profile.DoesNotExist:
        messages.error(request, 'Bạn chưa điền thông tin')
        return HttpResponse('Bạn chưa điền thông tin')
        
#def view_profile(request, pk):
 #   profile = get_object_or_404(Profile, id = pk)
  #  return render(request, 'view_profile.html', {'profile': profile})
# Create your views here.

@login_required

def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = PatientProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required 
def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.feedback = request.user
            feedback.save()
            return redirect('homepage')
    else:
        form = FeedbackForm()
    return render(request, 'send_feedback.html', {'form': form})

def view_feedback(request):
    feedbacks = Feedback.objects.all()
    return render (request, 'view_feedback.html', {'feedbacks': feedbacks})

@login_required
def medical_history(request):
    medical_dates = MedicalDate.objects.filter(patient = request.user)
    return render(request, 'view_medical_history.html', {'medical_dates' : medical_dates})