from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = 'index.html'

class ContactusPage(TemplateView):
    template_name = 'contactus.html'

class AboutusPage(TemplateView):
    template_name = 'aboutus.html'
