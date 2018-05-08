from django.shortcuts import render
from myapp.models import Customer
from myapp.forms import CarForm, RentForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        formset = CarForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    formset = CarForm()
    return render(request, 'home.html', {'formset': formset})

def rent(request):
    formset = RentForm()
    if request.method == 'POST':
        formset = RentForm(request.POST, request.FILES)
        if formset.is_valid():
            obj = formset.save(commit=False)
            customer = Customer.objects.get(user=request.user)
            obj.customer = customer
            obj.save()
    return render(request, 'home.html', {'formset': formset})