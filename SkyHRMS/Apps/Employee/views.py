from django.shortcuts import render
from django.views import View

# Create your views here.
class Dashboard(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)