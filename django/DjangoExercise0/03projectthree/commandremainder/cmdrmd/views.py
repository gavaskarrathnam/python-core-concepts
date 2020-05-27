from django.views.generic import ListView

from .models import CmdRemainder
import request

# Create your views here.
class HomePage(ListView):
    model = CmdRemainder
    template_name = "list.html"