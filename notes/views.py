from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView
from .models import Notes
from .forms import NotesForm

class NotesCreateView(CreateView):
    model = Notes # so the endpoint understands what its regarding to
    form_class = NotesForm # Fields of the model that the user is allowed to fill, now inside of a forms.py file
    success_url = '/smart/notes' # Redirect them to the list so they can see the note they just created in the list

class NotesListView(ListView):
    model = Notes
    context_object_name ="notes" # Default is objects but we called it 'notes'
    # This class view works without this explicit template name as we followed the default naming convention, but this is how we would specify if we didn't
    template_name = "notes/notes_list.html" 

# These class base views handle exceptions so we don't need to handle that complexity
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# This is an example of our old function detail view and the added complexity versus the class based view
"""
def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})
"""