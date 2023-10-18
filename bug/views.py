from django.views import generic

from django.urls import reverse_lazy

from .models import Bug

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "bug/index.html"

class BugCreateView(generic.CreateView):
    model = Bug
    template_name = "bug/add_bug.html"
    fields = ["description", "bug_type", "report_date", "status"]
    success_url = reverse_lazy("bug:bug_list")

class BugDetailView(generic.DetailView):
    model = Bug
    context_object_name = "bug_detail"
    template_name = "bug/bug_detail.html"

class BugListView(generic.ListView):
    model = Bug
    context_object_name = "bug_list"
    template_name = "bug/bug_list.html"