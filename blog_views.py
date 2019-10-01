from django.shortcurs import render
from .models import Entry
from django.views.generic import ListView, DetailView, View, CreateView

class HomeView(ListView):
  model = Entry
  template_name = 'entries/index.html'
  context_name = 'blog_entry'
  ordering = ['-entry_date']
  paginate_by = 3
  
 class EntryView(DetailView):
  model = Entry
  template_name = 'entries/detail.html'
  
 class EntryCreateView(CreateView):
  model = Entry
  template_name = 'entries/entry_create.html'
  fields = ['entry_title','entry_text']
  
  def form_valid(self, form):
      form.instance.entry_author = self.request.user
      return super().form_valid(form)
  
