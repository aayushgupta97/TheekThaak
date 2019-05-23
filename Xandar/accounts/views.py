from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random

from django.contrib import messages

from accounts.forms import UserRegisterForm
from core.models import Customer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def user_register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                email = request.POST.get('email')
                Customer.objects.get(email=email)
                errors = form.errors
                messages.add_message(request, messages.ERROR, "Email already exists.")
                return redirect('accounts:registration')

            except Customer.DoesNotExist:
                username = form.cleaned_data['first_name'] + form.cleaned_data['last_name'] + str(random.randint(1, 100))
                username = username.lower()
                while Customer.objects.filter(username=username).exists():
                    username = form.cleaned_data['first_name'] + form.cleaned_data['last_name'] + str(random.randint(1, 100))
                form.instance.username = username
                form.save()

                messages.success(request, 'You are now registered')

                html_content = render_to_string('accounts/email_confirmation.html')

                text_content = strip_tags(html_content)

                msg = EmailMultiAlternatives('You are now registered', text_content,
                                             'contact.realestate.information@gmail.com', [form.cleaned_data['email']])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                return redirect('accounts:loginapp')

        else:
            errors = form.errors
            messages.error(request, 'Password not valid or is too common.')
            return redirect('accounts:registration')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html')


























































































#----------------------------------------Amulya-----------------------------
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            current_customer = Customer.objects.get(email=email)
            user_authenticated = authenticate(request, username=current_customer.username, password=password)
            if user_authenticated is not None:
                login(request, user_authenticated)
                return redirect('index')
            else:
                context = {'message': 'Incorrect Password'}
        except Customer.DoesNotExist:
                context = {'message': 'No such user exist'}
        return render(request, 'accounts/login.html', context=context)
    else:
        if not request.user.is_authenticated:
            context={'logged_in': False}
        else:
            context={'logged_in': True}
        return render(request, 'accounts/login.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('accounts:login_app')


















































































#--------------------------------User Aman------------------------------



































































































#-------------------------------_User Deepak-------------------------
def check_email(request):
	if request.method == 'POST':
		mail = request.POST.get('email')
		user_email = Customer.objects.filter(email=mail)
		if user_email:
			request.session['user_email'] = mail
			return redirect('password_reset')
		else:
			return redirect('accounts:loginapp')
	else:
		return render(request, 'accounts/check_mail.html')

# def reset_password(request):
# 	if request.method == 'POST':
# 		password1 = request.POST['password1']
# 		password2 = request.POST['password2']
# 		user = Customer.objects.get(username__exact=request.user.username)
        
#         if password1==password2:
#             if user.check_password(request.POST['old_password']):
# 				user.set_password(password1)
# 				user.save()
# 				return redirect('password_reset_complete')
           
#     else:
#         return render(request, 'accounts/reset_password.html')


# change :  currently changes for username ttn only. have to make dynamic for authenticated user.

# change : else : else if old password is wrong
# change : else : else if new passwords dont match


def reset_password(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = Customer.objects.get(username__exact=request.user.username)

        if password1==password2:
            if user.check_password(request.POST['old_password']):
                user.set_password(password1)
                user.save()
                return redirect('password_reset_complete')
            else:
                messages.error(request, "The old password you have entered is wrong")
                return render(request, 'accounts/reset_password.html')

        else:
            messages.error(request, "Password does not match")
            return render(request, 'accounts/reset_password.html')

    else:
        return render(request, 'accounts/reset_password.html')