import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from marks.forms import MarkForm
from marks.models import Mark


def home(request):
    if request.user.is_authenticated == True:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def index(request):
    return render(request, 'mark/index.html')


def add(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            Mark.objects.create(user=request.user.id, name=form.cleaned_data['name']
                                , desctiption=form.cleaned_data['desctiption'], image=form.cleaned_data['image']
                                , gravity=form.cleaned_data['gravity'], created_at=datetime.datetime.today())
            return redirect('/admins/marks')
        else:
            return render(request, 'mark/add.html', {'form': form})

    else:
        form = MarkForm()
        return render(request, 'mark/add.html', {'form': form})


def update(request):
    if request.method == 'POST':
        return HttpResponse('ff')
    else:
        return render(request, 'mark/update.html')


def delete(request):
    if request.method == 'POST':
        return HttpResponse('ff')
    else:
        return render(request, 'mark/index.html')
