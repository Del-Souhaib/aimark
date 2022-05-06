from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    if request.user.is_authenticated==True:
        return render(request, 'index.html')
    else:
        return redirect('/admins/login')
