from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        slug = slugify(form.cleaned_data['title'])
        if self.model.objects.filter(slug=slug).exists():
            form.add_error('title', 'Пост с таким slug уже существует')
            return self.form_invalid(form=form)

        form.instance.author = self.request.user
        return super().form_valid(form)




class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'is_published',)

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_superuser \
            or self.request.user.has_perms(['blog.change_blog'])


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.is_superuser \
            or self.request.user.has_perms(['blog.delete_blog'])
