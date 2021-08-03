from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Resume(models.Model):
      owner= models.ForeignKey(User, on_delete=models.CASCADE)
      title=models.CharField(max_length=50,default='Resume')
      education=models.TextField(blank=False)
      profession=models.CharField(max_length=100,default='Engineer')
      skills=models.TextField(blank=False)
      experience=models.TextField(blank=True)
      project=models.TextField(blank=True)
      date=models.DateTimeField(default=timezone.now)
      contact=models.TextField(blank=True)

      def __str__(self):
          return self.owner.username

      def get_absolute_url(self):
          return reverse("resume-detail", kwargs={"pk": self.pk})
          