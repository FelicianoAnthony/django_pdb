from django.db import models
from django.contrib.auth.models import User


def upload_status_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
	pass


class StatusManager(models.Manager):
	def get_queryset(self):
		return StatusQuerySet(self.model, using=self.db)



class Status(models.Model):
	name = models.CharField(max_length=10)
	content = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.content)[:50]


	class Meta:
		verbose_name = 'Status post'
		verbose_name_plural = 'Status posts'