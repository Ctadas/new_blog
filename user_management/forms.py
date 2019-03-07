from django import forms
from user_management.models import UserManagement
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
	user_name = forms.CharField(
		widget = forms.TextInput(
			attrs = {'required':True,'class':'form-control','placeholder':'请输入用户名'}
			)
		)
	password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {'required':True,'class':'form-control','placeholder':'请输入密码'}
			)
		)

	def clean(self):
		cleaned_data = self.cleaned_data
		user_name = cleaned_data['user_name']
		password = cleaned_data['password']

		user = UserManagement.objects.filter(username = user_name)

		if user.exists():
			user = UserManagement.objects.get(username = user_name)
			if not check_password(password,user.password):
				raise forms.ValidationError("密码错误！！")
		else:
			raise forms.ValidationError("用户名不存在！！")

		return cleaned_data

class RegistrationForm(forms.Form):
	user_name = forms.CharField(
		widget = forms.TextInput(
			attrs = {'required':True,'class':'form-control','placeholder':'请输入用户名'}
			)
		)
	password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {'required':True,'class':'form-control','placeholder':'请输入密码'}
			)
		)
	confirm_password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {'required':True,'class':'form-control','placeholder':'请再次输入密码'}
			)
		)
	
	def clean(self):
		cleaned_data = self.cleaned_data
		user_name = cleaned_data['user_name']
		password = cleaned_data['password']
		confirm_password = cleaned_data['confirm_password']

		user = UserManagement.objects.filter(username = user_name)

		if user.exists():
			raise forms.ValidationError("该用户已存在！！")

		if password != confirm_password:
			raise forms.ValidationError("两次密码不一致，请重新输入！！")

		return cleaned_data

class InformationModificationForm(forms.Form):
	email = forms.EmailField(
		required = False,
		widget = forms.EmailInput(
			attrs = {'class':'form-control','placeholder':'请输入邮箱（非必填）'}
			)
		)

	head_portrait = forms.ImageField(
		required = False,
		widget = forms.ClearableFileInput(
			attrs = {'class':'img_upload'}
			)
		)