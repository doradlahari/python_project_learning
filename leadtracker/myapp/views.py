from django.shortcuts import render

# Create your views here.

def sample_page(request):
    return render(request, 'sample.html')

def register_page(request):
    if request.method == "POST":
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        mobile=request.POST['mobile']
        address=request.POST['address']
        print(firstName,lastName,email,mobile,address)
    return render(request, 'register.html')