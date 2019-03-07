from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
def upload_to(instance, filename):
	return '/'.join(['head_portrait', instance.username ,filename])

class UserManagement(AbstractUser):
	head_portrait = models.ImageField(upload_to = upload_to,blank = True,verbose_name = "用户头像",default="head_portrait/common/avatar.png")

	class Meta:
		verbose_name = '用户管理'
		verbose_name_plural = "用户管理"
