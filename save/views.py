from django.shortcuts import render, redirect
from .models import List, Items
from .forms import ListForm, ItemsForm

# Create your views here.
def list_list(request):
    lists = List.objects.all()
    return render(request, 'save/list_list.html', {'lists': lists})

def list_detail(request, pk):
    # adding an underscore to avoid issues with a key word/function.
    _list = List.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            # item is created in the code but not saved in the database yet.
            item = form.save(commit=False)
            # this associates the item with a list.
            item.lists_id = pk
            # this save commits it to the database.
            item.save()
            return redirect('list_detail', pk=pk)
    else:
        form = ItemsForm()
    return render(request, 'save/list_detail.html', {'list': _list, 'form': form})

def list_create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            _list = form.save()
            return redirect('list_detail', pk=_list.pk)
    else:
        form = ListForm()
    return render(request, 'save/list_form.html', {'form': form})

def list_update(request, pk):
    _list = List.objects.get(pk=pk)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=_list)
        if form.is_valid():
            _list = form.save()
            return redirect('list_detail', pk=_list.pk)
    else:
        form = ListForm(instance=_list)
    return render(request, 'save/list_form.html', {'form': form})

def list_delete(request, pk):
    List.objects.get(pk=pk).delete()
    return redirect('list_list')

def item_list(request):
    items = Items.objects.all()
    return render(request, 'save/items_list.html', {'items': items})

def item_detail(request, pk):
    item = Items.objects.get(pk=pk)
    return render(request, 'save/item_detail.html', {'item': item})

def item_update(request, pk):
    item = Items.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            _list = item.lists_id
            return redirect('list_detail', pk=_list)
    else:
        form = ItemsForm(instance=item)
    return render(request, 'save/item_form.html', {'form': form})

def item_delete(request, pk):
    Items.objects.get(pk=pk).delete()
    _list = Items.lists_id
    return redirect('list_detail', pk=_list)