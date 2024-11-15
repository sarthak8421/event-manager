from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from django.http import HttpResponse

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        Event.objects.create(title=title, description=description, date=date, time=time, location=location)
        return redirect('event_list')
    return render(request, 'events/event_form.html')

def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.date = request.POST['date']
        event.time = request.POST['time']
        event.location = request.POST['location']
        event.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'event': event})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')
