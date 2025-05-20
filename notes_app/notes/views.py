from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .models import Note
from .forms import NoteForm


@login_required
@never_cache
def notes_view(request):
    notes = Note.objects.filter(user=request.user).order_by('-last_update')
    form = NoteForm()
    return render(request, 'notes.html', {'notes': notes, 'form': form})

@login_required
@never_cache
def note_detail_view(request, note_id):
    note = get_object_or_404(Note, note_id=note_id, user=request.user)
    form = NoteForm(instance=note)
    return render(request, 'note_detail.html', {'note': note, 'form': form})

@login_required
@never_cache
def add_note_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, user=request.user)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Note added successfully.')
            return redirect('notes')
        else:
            messages.error(request, 'Error adding note.')
    return redirect('notes')

@login_required
@never_cache
def edit_note_view(request, note_id):
    note = get_object_or_404(Note, note_id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully.')
            return redirect('note_detail', note_id=note_id)
        else:
            messages.error(request, 'Error updating note.')
    return redirect('note_detail', note_id=note_id)


@login_required
@never_cache
def delete_note_view(request, note_id):
    note = get_object_or_404(Note, note_id=note_id, user=request.user)
    note.delete()
    messages.success(request, 'Note deleted successfully.')
    return redirect('notes')