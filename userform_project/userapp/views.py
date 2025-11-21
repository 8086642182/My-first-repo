from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

@login_required
def form_list(request):
    people = Person.objects.filter(user=request.user)
    return render(request, 'userapp/form_list.html', {'people': people})

@login_required
def form_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            person.save()
            return redirect('form_list')
    else:
        form = PersonForm()
    return render(request, 'userapp/form_create.html', {'form': form})

@login_required
def form_edit(request, pk):
    person = get_object_or_404(Person, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('form_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'userapp/form_edit.html', {'form': form})

@login_required
def form_delete(request, pk):
    person = get_object_or_404(Person, pk=pk, user=request.user)
    if request.method == 'POST':
        person.delete()
        return redirect('form_list')
    return render(request, 'userapp/form_delete.html', {'person': person})



