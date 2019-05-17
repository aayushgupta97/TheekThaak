from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
def login_page(request):
    return render(request, 'accounts/login.html')




































































































































































































































































































def check_email(request):
	if request.method == 'POST':
		mail = request.POST.get('email')
		user_email = User.objects.filter(email=mail)

		if user_email:
			request.session['user_email'] = mail
			return redirect('password_reset')
		else:
			return redirect('loginapp')
	else: 
		return render(request, 'accounts/check_mail.html')