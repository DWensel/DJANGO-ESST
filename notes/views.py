from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NotesForm

# Only needs the model and success url (and in our case the template name), then a URL path
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html' # notes/notes_confirm_delete.html is expected but we can pass our own if we don't want to rename our template


# The update view is a copy of the createview, just needs its own URL path
class NotesUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes # so the endpoint understands what its regarding to
    form_class = NotesForm # Fields of the model that the user is allowed to fill, now inside of a forms.py file
    success_url = '/smart/notes' # Redirect them to the list so they can see the note they just created in the list

    def form_valid(self, form):
        self.object = form.save(commit=False) # First get the object
        self.object.user = self.request.user # Fill the object, in this case the user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name ="notes" # Default is objects but we called it 'notes'
    # This class view works without this explicit template name as we followed the default naming convention, but this is how we would specify if we didn't
    template_name = "notes/notes_list.html" 
    login_url ="/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

# These class base views handle exceptions so we don't need to handle that complexity
class NotesDetailView(LoginRequiredMixin, DetailView):
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