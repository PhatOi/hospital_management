from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user # current user
        if user.is_authenticated:
            if user.user_type == '1': # Admin/Manager
                if modulename == 'main_app.patient_views' or modulename == 'main_app.healthcareStaff_views':
                    return redirect(reverse('admin_home'))
            elif user.user_type == '2': #  Staff
                if modulename == 'main_app.patient_views' or modulename == 'main_app.admin_views':
                    return redirect(reverse('staff_home'))
            elif user.user_type == '3': # Patient
                if modulename == 'main_app.admin_views' or modulename == 'main_app.healthcareStaff_views':
                    return redirect(reverse('patient_home'))
            else: # none of the required user back to login page
                return redirect(reverse('login_page'))
        else:
            if request.path == reverse('login_page') or modulename == 'django.contrib.auth.views' or request.path == reverse('do_login'): # If the path is login or has anything to do with authentication, pass
                pass
            else:
                messages.error(request, "Hãy đăng nhập")
                return redirect(reverse('login_page'))