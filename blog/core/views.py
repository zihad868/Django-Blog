from django.shortcuts import render, redirect
from item.models import Category, Item
from . forms import SignupForm

def index(request):
    item = Item.objects.filter(is_sold=False)[0:6]
    category = Category.objects.all()
    
    return render(request, 'core/index.html', {
        'items': item,
        'categories': category
    })


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login')
            
    return render(request,'core/signup.html', {
        'form': form
    })
    
    
def login(request):
    return render(request, 'core/login.html')