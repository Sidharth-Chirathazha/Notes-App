from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Note
        fields = ['note_title', 'note_content']
        widgets = {
            'note_title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter note title'}),
            'note_content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Enter note content', 'rows': 5}),
        }

    def clean_note_title(self):
        note_title = self.cleaned_data['note_title']
        if not note_title.strip():
            raise forms.ValidationError("Note title cannot be empty.")
        if Note.objects.filter(note_title=note_title, user=self.user).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A note with this title already exists.")
        return note_title
    
    def clean_note_content(self):
        note_content = self.cleaned_data['note_content']
        if not note_content.strip():
            raise forms.ValidationError("Note content cannot be empty.")
        return note_content