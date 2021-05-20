from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from events import views as views_events
from .models import Event, Employee, EventHandler
#from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import EventForm
# Create your views here.


# def home(request):
#     return HttpResponse('EVENTS')


def account(request):
    return HttpResponse('Money money')


def dashboard(request):
    event_list = Event.objects.all()

    total_events = event_list.count()
    draft = event_list.filter(status='Draft').count()
    ongoing = event_list.filter(status='Ongoing').count()
    finished = event_list.filter(status='Finished').count()

    page_num = request.GET.get('page',1)

    paginator = Paginator(event_list, 2)

    try:
        events = paginator.page(page_num)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    context ={
        'events': events,
        'total' : total_events,
        'draft' : draft,
        'ongoing' : ongoing,
        'finished' : finished 
    }

    return render(request,template_name='events/home.html',context=context)

def create_event(request):

    form = EventForm()
    if request.method == 'POST':
 
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={
        'form':form

    }

    return render(request, template_name ='events/event_form.html', context=context)


def update_event(request,pk):

    event = Event.objects.get(id=pk)
    form = EventForm(instance=event)

    if request.method == 'POST':
 
        form = EventForm(request.POST,instance=event)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={
        'form':form
    }

    return render(request, template_name = 'events/event_form.html', context=context)


def event_detail(request,pk):
    event = Event.objects.get(id=pk)

    context ={
    'event':event
    }

    return render(request, template_name = 'events/event.html', context = context)