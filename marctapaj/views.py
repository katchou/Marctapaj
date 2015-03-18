from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.forms.models import modelform_factory

from marctapaj.models import Bookmark, Category, Note

class IndexView(generic.ListView):
    def get_queryset(self):
        return Category.objects.all()

class DetailView(generic.DetailView):
    pass

class AddCategoryView(generic.edit.CreateView):
    model = Category

class EditCategoryView(generic.edit.UpdateView):
    model = Category

class DeleteCategoryView(generic.edit.DeleteView):
    model = Category
    template_name = 'marctapaj/confirm_delete.html'
    success_url = reverse_lazy('marctapaj:index')

class AddBookmarkView(generic.edit.CreateView):
    model = Bookmark

    def get_initial(self):
            category = get_object_or_404(Category, pk=self.request.GET.get('cat'))
            return {
                'category':category,
            }

class AddNoteView(generic.edit.CreateView):
    model = Note
    form_class = modelform_factory(Note, fields=('content',))

    def dispatch(self, *args, **kwargs):
        self.bookmark = get_object_or_404(Bookmark, pk=kwargs['bookmark_id'])
        return super(AddNoteView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.bookmark = self.bookmark
        self.object.update_date = timezone.now()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class EditNoteView(generic.edit.UpdateView):
    model = Note
    form_class = modelform_factory(Note, fields=('content',))

class DeleteNoteView(generic.edit.DeleteView):
    model = Note
    template_name = 'marctapaj/confirm_delete.html'
    success_url = reverse_lazy('marctapaj:index')

class GoToBookmark(generic.View):
    def get(self, request, *args, **kwargs):
        b = get_object_or_404(Bookmark, pk=kwargs['bookmark_id'])
        b.last_access = timezone.now()
        b.access_count += 1
        b.save()
        return HttpResponseRedirect(b.url)