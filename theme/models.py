from django.db import models

# Create your models here.
class Theme(models.Model):
	title = models.CharField(max_length = 100)
	about = models.CharField(max_length = 200)
	theme_pictures = models.ImageField(upload_to='uploads/%Y/%m/%d/')

	def __str__(self):
		return self.title
