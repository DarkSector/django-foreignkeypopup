from django.views.generic import CreateView, UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from models import ParentModel, ChildClass
from forms import ChildForm


# Create your views here.
class ParentCreateView(CreateView):
    model = ParentModel
    template_name = 'parent_create_view.html'
    fields = ['name']


class ChildCreateView(CreateView):
    model = ChildClass
    template_name = 'child_create_view.html'
    form_class = ChildForm
    success_url = reverse_lazy('child_list_view')


class ChildListView(ListView):
    model = ChildClass
    template_name = 'child_list_view.html'

