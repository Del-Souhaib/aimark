import datetime

import cv2
from django.contrib.auth.models import User
from django.core.files.storage import Storage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.templatetags.static import static

from marks.forms import MarkForm
from marks.models import *

import cv2 as cv


def home(request):
    if request.user.is_authenticated == True:
        print(cv.__version__)
        return render(request, 'index.html')
    else:
        return redirect('/admins/login')


def index(request):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    data = Mark.objects.all()
    return render(request, 'mark/index.html', {'data': data})


def add(request):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    if request.method == 'POST':
        form = MarkForm(request.POST, request.FILES)
        # form.user=request.user.id
        # form.created_at=datetime.date.today()
        if form.is_valid():
            mark = Mark(user=User.objects.get(id=request.user.id), name=form.cleaned_data['title']
                        , desctiption=form.cleaned_data['desctiption'], image=form.cleaned_data['image']
                        , gravity=form.cleaned_data['gravity'] * 10, created_at=datetime.today())
            mark.save()
            return redirect('/admins/marks/edit/' + str(mark.id))
        else:
            return render(request, 'mark/add.html', {'form': form})

    else:
        form = MarkForm()
        return render(request, 'mark/add.html', {'form': form})


def edit(request, id):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    mark = Mark.objects.get(id=id)
    if request.method == 'POST':
        form = MarkForm(request.POST, request.FILES)
        if form.is_valid():
            # mark.user = request.user.id
            mark.name = form.cleaned_data['title']
            mark.desctiption = form.cleaned_data['desctiption']
            if form.cleaned_data['image']:
                mark.image = form.cleaned_data['image']

            mark.gravity = form.cleaned_data['gravity'] * 10
            mark.save()

            return redirect('/admins/marks/')
        else:
            return render(request, 'mark/edit.html', {'form': form})

    else:
        form = MarkForm(initial={
            'id': mark.id,
            'user': mark.user,
            'title': mark.name,
            'desctiption': mark.desctiption,
            'image': mark.image,
            'gravity': mark.gravity / 10,
            'created_at': mark.created_at,
        })
        points = Point.objects.filter(mark=id)

        return render(request, 'mark/edit.html', {'form': form, 'points': points})


def delete(request):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    if request.method == 'POST':
        mark = Mark.objects.get(id=request.POST['markid'])
        mark.delete()
    return redirect('/admins/marks/')


def addpoint(request, id):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    if request.method == 'POST':
        # HttpResponse(request.POST['x'])
        point = Point(mark=Mark.objects.get(id=id), num=request.POST['count'], x=request.POST['x']
                      , y=request.POST['y'])
        point.save()
        return HttpResponse('good')
    else:
        return redirect('/admins/marks/')


def deletepoint(request, id):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    if request.method == 'POST':
        # HttpResponse(request.POST['x'])
        Point.objects.filter(mark=id).delete()
        return redirect('/admins/marks/edit/'+str(id))
