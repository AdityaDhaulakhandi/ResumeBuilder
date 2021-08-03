from django.urls import path
from . import views


urlpatterns = [
    path('',views.ResumeListView.as_view(),name='resume-home'),   
    path('about/',views.about,name='resume-about'), 
    path('contact/',views.contact,name='resume-contact'), 
    
    path('user/<str:username>/',views.UserResumeView.as_view(),name='user-resume'),
    path('resume/<int:pk>/',views.ResumeDetailView.as_view(template_name='resume/detail.html'),name='resume-detail'),
    path('resume/create/',views.ResumeCreateView.as_view(template_name='resume/resume-form.html'),name='resume-create'),
    path('resume/<int:pk>/update/',views.ResumeUpdateView.as_view(template_name='resume/resume-form.html'),name='resume-update'),
    path('resume/<int:pk>/delete/',views.ResumeDeleteView.as_view(template_name='resume/resume-delete.html'),name='resume-delete'),
    ]