from django.shortcuts import render,redirect
from . models import Customer,Images
from django.contrib import messages
from . forms import SignupForm,LoginForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']

            user=Customer.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Email Already Exists")
                return redirect('/sup')
            elif password!=cpassword:
                messages.warning(request,"PASSWORD AND CONFIRMPASSWORD DOES NOT MATCH")
                return redirect('/sup')
            else:
                tab=Customer(Name=name,Age=age,Email=email,Password=password)
                tab.save()
                messages.success(request,"DATA SAVES SUCCESSFULLY")
                return redirect('/')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})


def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']

            user=Customer.objects.get(Email=email)
            if not user:
                messages.warning(request,"USER DOES NOT EXIST")
                return redirect('/log')
            elif password!=user.Password:
                messages.warning(request,"WRONG PASSWORD")
                return redirect('/log')
            else:
                messages.success(request,"LOGGED IN SUCCESSFULLY")
                return redirect('/')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})

def gallery(request):
    igs=Images.objects.all()
    return render(request,'gallery.html',{'igs':igs})

def detail(request,id):
    data=Images.objects.get(id=id)
    return render(request,'details.html',{'data':data})
