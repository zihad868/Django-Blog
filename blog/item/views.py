from django.shortcuts import render, get_object_or_404, redirect
from . models import Item
from . forms import NewItemForm, EditItemForm
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
    
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('Item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/newItem.html', {
        'form': form,
        'title': 'Edit item',
    })