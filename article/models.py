from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_delete
from django.dispatch import receiver
from lxml import etree
from django.conf import settings
import os

# Create your models here.
class Article_type(models.Model):
	type_name = models.CharField(unique=True,max_length = 100)

	def __str__(self):
		return self.type_name

class Article(models.Model):
	tpye = models.ForeignKey(Article_type, on_delete=models.CASCADE)
	title = models.CharField(max_length = 100)
	content = RichTextUploadingField()
	release_time = models.DateField(auto_now_add = True)
	show_pictures = models.ImageField(upload_to='uploads/%Y/%m/%d/')
	visits = models.IntegerField(default = 0)

	def __str__(self):
		return self.title

@receiver(post_delete, sender=Article)
def delete_upload_files(sender, instance, **kwargs):
	del_url = []
	print(instance.show_pictures)
	file_url = os.path.join(settings.MEDIA_ROOT, str(instance.show_pictures))	
	content_html = etree.HTML(instance.content)
	content_img_src = content_html.xpath('//img/@src')
	for img_src in content_img_src:
		img_src = os.path.join(settings.BASE_DIR, img_src[1:])
		del_url.append(os.path.join(settings.BASE_DIR, img_src).replace('\\','/'))
	del_url.append(file_url.replace('\\','/'))
	for durl in del_url:
		if os.path.isfile(durl):
			os.remove(durl)

	del_empty_dir(settings.MEDIA_ROOT)

def del_empty_dir(dir):
	if os.path.isdir(dir):
		for item in os.listdir(dir):
			del_empty_dir(os.path.join(dir,item))

		if not os.listdir(dir):
			os.rmdir(dir)