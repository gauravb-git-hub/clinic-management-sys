from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/auth-app/login/')
def create_appointment(request):
    template_name = 'clinic_app/appointment_form.html'
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_app_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='/auth-app/login/')
def show_appointments(request):
    template_name = 'clinic_app/show_appointements.html'
    appointments = Appointment.objects.all() #[obj1, obj2, obj3, ..................]
    name = request.GET.get('patient_name')
    date = request.GET.get('date')
    time = request.GET.get('time')
    sort = request.GET.get('sort')
    print(name, date, time, sort)
    if name:
        #appointments = appointments.filter(patient_name= name)
        appointments = appointments.filter(patient_name__icontains = name)
    if date:
        appointments = appointments.filter(appointment_date=date)
    if time:
        appointments = appointments.filter(appointment_time=time)
    if sort:
        appointments = appointments.order_by(sort)
    
    context = {'appointments': appointments}
    return render(request, template_name, context)

@login_required(login_url='/auth-app/login/')
def update_appointment(request, pk):
    print('Dynamic part: ', pk)
    template_name = 'clinic_app/update_app.html'
    obj = get_object_or_404(Appointment, pk=pk)
    # obj = get_object_or_404(Appointement, id = 1)
    form = AppointmentForm(instance=obj)
    if request.method == "POST":
        form = AppointmentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_app_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='/auth-app/login/')
def delete_app(request, pk):
    print('DYAMIC DATA:', pk)
    template_name = 'clinic_app/delete_app.html'
    obj = get_object_or_404(Appointment, pk=pk)
    context = {'obj': obj}
    if request.method == "POST":
        obj.delete()
        return redirect('show_app_url')
    return render(request, template_name, context)





