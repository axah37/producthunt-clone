from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=140)
	url = models.TextField()
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField()
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)
	upvote = models.ManyToManyField(User,default=None,related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss")

	def __str__(self):
		return self.title
	def summary(self):
		return self.body
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')