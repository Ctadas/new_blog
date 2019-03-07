# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class Theme(models.Model):
	title = models.CharField('标题',max_length = 100)
	about = models.CharField('主题描述',max_length = 200)
	theme_pictures = models.ImageField(upload_to='uploads/%Y/%m/%d/',verbose_name='主题图片')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '主题管理'
		verbose_name_plural = "主题管理"
