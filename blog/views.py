from django.shortcuts import render
from blog.forms import blogForm

# Create your views here.



def index(request):
    form = blogForm()
    if request.method=="POST":
        form = blogForm(request.POST)
        
        if form.is_valid():
            form.save()
            print("Info mation saved successful")
        
    return render(request, "index.html", {"form":form})
        
