from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
# Create your views here.
def all_notes(request):
    all_notes=Note.objects.all()
    context={
        'all_notes':all_notes
    }
    return render(request,'notes.html',context)

def details(request,slug):
    note=Note.objects.get(slug=slug)
    context={
    'note':note
    }
    return render(request,'details.html',context)

def add_note(request):

    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/notes')
    else :form=NoteForm()

    context={
        'form':form,
    }
    return render(request,'add.html',context)

def edit_note(request,slug):
    note=get_object_or_404(Note,slug=slug)
    if request.method=='POST':
        form=NoteForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=request.user
            new_form.save()
            return redirect('/notes')
    else :form=NoteForm(instance=note)

    context={
        'form':form,
    }
    return render(request,'edit.html',context)
