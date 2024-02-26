from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.contrib.auth import authenticate, login, logout

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})


def admin(request):
    return redirect('/admin/')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_event')  # Redirect to the 'add_event' page upon successful login
    return render(request, 'admin_login.html')


def custom_logout(request):
    logout(request)
    return redirect('event_list')  # Redirect to the 'event_list' page after logout