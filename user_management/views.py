from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from user_management.forms import LoginForm,RegistrationForm,InformationModificationForm
from django.contrib.auth.hashers import make_password,check_password
from user_management.models import UserManagement

@login_required
def personal_information_modification(request):
	return_content = {}
	return_content['form'] = InformationModificationForm
	
	if request.method == "POST":
		form = InformationModificationForm(request.POST,request.FILES)
		if form.is_valid():
			email = form.cleaned_data['email']
			head_portrait = form.cleaned_data['head_portrait']

			user_name = request.user
			user = UserManagement.objects.get(username = user_name)

			if email:
				user.email = email
			if head_portrait:
				user.head_portrait = head_portrait

			user.save()
			return redirect('index')

	return render(request,'user_management/personal_information_modification.html',return_content)

# Create your views here.
def user_login(request):
	next_url = request.GET.get('next', '')
	return_content = {}
	return_content['form'] = LoginForm
	return_content['type'] = 'login'
	return_content['next_url'] = next_url
	if request.method == "POST":
		next_url = request.POST.get('next', '')
		form = LoginForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data['user_name']
			password = form.cleaned_data['password']
			user = authenticate(request, username=user_name, password=password)
			# user = UserManagement.objects.get(username = user_name)

			login(request, user)
			if next_url:
				return redirect(next_url)
			else:
				return redirect('index')
		else:
			return_content['form'] = form
			return render(request,'user_management/login_registration.html',return_content)

	return render(request,'user_management/login_registration.html',return_content)

def user_registration(request):
	return_content = {}
	return_content['form'] = RegistrationForm
	return_content['type'] = 'registration'
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user_name = form.cleaned_data['user_name']
			password = form.cleaned_data['password']
			# password = make_password(password)
			user = UserManagement.objects.create_user(username = user_name,password = password)
			login(request, user)
			return redirect('index')
		else:
			return_content['form'] = form
			return render(request,'user_management/login_registration.html',return_content)

	return render(request,'user_management/login_registration.html',return_content)

@login_required
def user_logout(request):
	logout(request)
	return redirect('index')