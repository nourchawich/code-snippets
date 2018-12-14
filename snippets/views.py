from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Snippet


class SnippetCreate(CreateView):
    template_name = 'snippets/snippet_form.html'
    model = Snippet
    fields = ['title', 'code', 'tags', 'published']

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.instance.user = self.request.user
        return super().form_valid(form)


class SnippetUpdate(UpdateView):
    template_name = 'snippets/snippet_form.html'
    model = Snippet
    fields = ['title', 'code', 'tags', 'published']


class SnippetDetail(DetailView):
    template_name = 'snippets/snippet_detail.html'
    model = Snippet
    context_object_name = 'snippet'


class SnippetList(ListView):
    template_name = 'snippets/snippet_list.html'
    context_object_name = 'snippets'
    paginate_by = 25  # This allows passing ?page=x to the url

    def get_queryset(self):
        qs = Snippet.objects.all()
        # In the case this view was triggered by a visit to /snippets/tags/TAG/
        # self.kwargs['tag'] will have the tag. We use it to filter the queryset
        if 'tag' in self.kwargs:
            qs = qs.filter(tags__contains=[self.kwargs['tag']])
        return qs.order_by('-created_at')
