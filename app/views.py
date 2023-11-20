from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todolist
from .forms import ItemForm
from django.shortcuts import get_object_or_404
from django.urls import reverse


def home(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Have Been Added!",
                             extra_tags="added_item")
            return redirect('home')
        else:
            messages.success(request, "Error Input..",
                             extra_tags="error_item")
            return redirect('home')
    else:
        data = {
            'items': Todolist.objects.all(),
            'form': ItemForm(request.POST),
        }
        return render(request, 'home.html', data)


def delete_item(request, id_item):
    Todolist.objects.get(id=id_item).delete()
    messages.success(request, "Item Deleted Successfully..",
                     extra_tags="deleted_item")
    return redirect('home')


def update_item(request, id_item):
    current_item = Todolist.objects.get(id=id_item)
    form = ItemForm(request.POST or None, instance=current_item)
    data = {
        'items': Todolist.objects.all(),
        'form': form,
        'single_item': Todolist.objects.get(id=id_item),
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Item Have Been Updated!",
                             extra_tags="added_item")
            return redirect('home')
        else:
            messages.success(request, "Error Input..",
                             extra_tags="error_item")
            return redirect('home')
    else:
        return render(request, 'home.html', data)


def progress_item(request, id_item):
    todolist_item = get_object_or_404(Todolist, id=id_item)
    todolist_item.status = not todolist_item.status
    todolist_item.save()
    messages.success(request, "Progress Have Been Updated!",
                     extra_tags="added_item")
    return redirect('home')
