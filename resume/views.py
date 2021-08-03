from .models import Resume
from django.shortcuts import render, get_object_or_404
from account.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
app_name='resume'

def about(request):
      return render(request,'resume/about.html',{})

def contact(request):
      return render(request,'resume/contact.html',{})

class ResumeListView(ListView):
      model=Resume
      template_name='resume/home.html'
      ordering=['date']
      context_object_name='resumes'      

class ResumeDetailView(DetailView):
      model=Resume
      context_object_name='resume'


class UserResumeView(ListView):
      model=Resume
      template_name='resume/user-resume.html'
      ordering=['-date']  
      context_object_name='resumes'

      def get_queryset(self):
            user=get_object_or_404(User, username=self.kwargs.get('username'))
            return Resume.objects.filter(owner=user).order_by('-date') 


class ResumeCreateView(LoginRequiredMixin, CreateView):
      model=Resume
      fields=[
            'title',
            'profession',
            'education',
            'skills',
            'experience',
            'contact'
            ]

      def form_valid(self, form):
            form.instance.owner=self.request.user
            return super().form_valid(form)


class ResumeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
      model=Resume
      fields=[
            'title',
            'profession',
            'education',
            'skills',
            'experience',
            'contact'
            ]

      def form_valid(self, form):
            form.instance.owner=self.request.user
            return super().form_valid(form)
      
      def test_func(self):
            resume=self.get_object()
            if self.request.user == resume.owner:
                  return True
            return False 


class ResumeDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
      model=Resume

      def test_func(self):
            post=self.get_object()
            if self.request.user== post.owner:
                  return True
            return False
      success_url='/'       
      