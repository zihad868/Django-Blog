from django.shortcuts import render, get_object_or_404, redirect
from . models import Item
from . forms import NewItemForm
from django.contrib.auth.decorators import login_required

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False)
    
    return render(request, "item/detail.html", {
        'item': item,
        'related_items': related_items
    })


@login_required
def newItem(request):
    form = NewItemForm()
    
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('Item:detail', pk=item.id)
    
    return render(request, 'item/newItem.html', {
        'form': form,
        'title': 'new-item'
    })
    