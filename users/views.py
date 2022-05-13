from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from users.forms import UserForm


def index(request):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    data = User.objects.all()
    return render(request, 'user/index.html', {'data': data})


def add(request):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        # form.user=request.user.id
        # form.created_at=datetime.date.today()
        if form.is_valid():

            user = User(username=form.cleaned_data['username']
                        , email=form.cleaned_data['email'], password=form.cleaned_data['password']
                        , date_joined=datetime.today())
            user.save()
            return redirect('/admins/users/')
        else:
            return render(request, 'user/add.html', {'form': form})

    else:
        form = UserForm()
        return render(request, 'user/add.html', {'form': form})


def edit(request, id):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # mark.user = request.user.id
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            if form.cleaned_data['password']:
                user.password = form.cleaned_data['password']

            user.save()

            return redirect('/admins/users/')
        else:
            return render(request, 'user/edit.html', {'form': form})

    else:
        form = UserForm(initial={
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })

        return render(request, 'user/edit.html', {'form': form})


def delete(request):
    if request.user.is_authenticated == False:
        return redirect('/admins/login')

    if request.method == 'POST':
        user = User.objects.get(id=request.POST['userid'])
        user.delete()
    return redirect('/admins/users/')

