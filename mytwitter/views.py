from django.shortcuts import render
from .models import Usertwitter
from .form import UsertwitterFrom,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required
def add_twitter(request):
    if request.method=="POST":
        form=UsertwitterFrom(request.POST,request.FILES)
        if form.is_valid():
            twitter=form.save(commit=False)
            twitter.user=request.user
            twitter.save()
            return redirect('get_list_of_twitter')
            
    else:
        form=UsertwitterFrom()
    return render(request,'twitter_form.html',{'form':form})
     

@login_required
def edit_twitter(request,id):
    twitter=get_object_or_404(Usertwitter,pk=id,user=request.user)
    if request.method=='POST':
        form=UsertwitterFrom(request.POST,request.FILES,instance=twitter)
        if form.is_valid():
            twitter=form.save(commit=False)
            twitter.user =request.user
            twitter.save()
            return redirect('get_list_of_twitter')
        else:
            form=UsertwitterFrom(instance=twitter)
        return render(request,'twitter_form.html',{'form':form})


def delete_twitter(request,id):
    twitter=get_object_or_404(Usertwitter,pk=id,user=request.user)
    if request.method=='POST':
        twitter.delete()
        return redirect("get_list_of_twitter"),
    return render(request,'twitter_delete.html',{'twitter':twitter})


def get_all_twitter(request):
    User_twitter=Usertwitter.objects.all().order_by("create_at")
    return render(request,'twitter_list.html',{'twitter':User_twitter})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect('get_list_of_twitter')  # Redirect to a valid view name
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html', {'form': form})