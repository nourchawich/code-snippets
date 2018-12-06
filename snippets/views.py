from django.views.generic import ListView

from .models import Snippet


class SnippetList(ListView):
    template_name = 'snippets/snippet_list.html'
    context_object_name = 'snippets'

    def get_queryset(self):
        qs = Snippet.objects.all()
        # In the case this view was triggered by a visit to /snippets/tags/TAG/
        # self.kwargs['tag'] will have the tag. We use it to filter the queryset
        if 'tag' in self.kwargs:
            qs = qs.filter(tags__contains=[self.kwargs['tag']])
        return qs.order_by('-created_at')
