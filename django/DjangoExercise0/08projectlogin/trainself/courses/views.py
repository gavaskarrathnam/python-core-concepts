from django.views.generic import ListView, DetailView

from .models import OpenSourceCourses

# Create your views here.
class OpenSource(ListView):
     model = OpenSourceCourses
     template_name = 'opensource.html'

class CourseDetail(DetailView):
     model = OpenSourceCourses
     template_name = 'coursedetail.html'
     context_object_name = 'cDetail'