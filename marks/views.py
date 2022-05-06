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
    data = Mark.objects.all()
    return render(request, 'mark/index.html', {'data': data})


def add(request):
    if request.method == 'POST':
        form = MarkForm(request.POST, request.FILES)
        # form.user=request.user.id
        # form.created_at=datetime.date.today()
        if form.is_valid():
            mark = Mark(user=request.user.id, name=form.cleaned_data['title']
                        , desctiption=form.cleaned_data['desctiption'], image=form.cleaned_data['image']
                        , gravity=form.cleaned_data['gravity'] * 10, created_at=datetime.datetime.today())
            mark.save()
            return redirect('/admins/marks/edit/' + str(mark.id))
        else:
            return render(request, 'mark/add.html', {'form': form})

    else:
        form = MarkForm()
        return render(request, 'mark/add.html', {'form': form})


def edit(request, id):
    mark = Mark.objects.get(id=id)
    if request.method == 'POST':
        form = MarkForm(request.POST, request.FILES)
        if form.is_valid():
            mark.user = request.user.id
            mark.name = form.cleaned_data['title']
            mark.desctiption = form.cleaned_data['desctiption']
            mark.image = form.cleaned_data['image']
            mark.gravity = form.cleaned_data['gravity'] * 10
            mark.created_at = datetime.datetime.today()
            mark.save()
            return redirect('/admins/marks/edit/' + str(mark.id))
        else:
            return render(request, 'mark/edit.html', {'form': form})

    else:
        form = MarkForm(initial={
            'id': mark.id,
            'user': mark.user,
            'title': mark.name,
            'desctiption': mark.desctiption,
            'image': mark.image,
            'gravity': mark.gravity/10,
            'created_at': mark.created_at,
        })
        # form.name.initial = mark.title
        # form.user.initial = mark.user
        # form.desctiption.initial = mark.desctiption
        # form.image.initial = mark.image
        # form.gravity.initial = mark.gravity
        # form.created_at.initial = mark.created_at

        return render(request, 'mark/edit.html', {'form': form})


def delete(request):
    if request.method == 'POST':
        return HttpResponse('ff')
    else:
        return render(request, 'mark/index.html')


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
