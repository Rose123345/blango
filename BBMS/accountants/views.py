from django.shortcuts import render

# Create your views here.
def accountant_dashboard(request):
    return render(request, 'accountants/dashboard.html')