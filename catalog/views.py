from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, ExtendedFlatPage, UserProfile
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from .forms import BookForm, BookSearchForm


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_visits': num_visits},
    )


class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['author_list'] = Author.objects.all()
        return context


class BookCreate(generic.CreateView):
    model = Book
    template_name = 'catalog/book_add.html'
    form_class = BookForm


class BookDetailView(generic.DetailView):
    model = Book


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'catalog/book_add.html'
    form_class = BookForm
    success_url = reverse_lazy('book-list')


class BookDelete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class BookSearchView(generic.FormView):
    form_class = BookSearchForm
    template_name = 'catalog/book_list.html'

    # def post(self, request, *args, **kwargs):
    #     return


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


DEFAULT_TEMPLATE = 'flatpages/default.html'


def flatpage(request, url):
    if not url.startswith('/'):
        url = '/' + url
    site_id = get_current_site(request).id
    try:
        f = get_object_or_404(ExtendedFlatPage, url=url, sites=site_id)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            f = get_object_or_404(ExtendedFlatPage, url=url, sites=site_id)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_flatpage(request, f)


@csrf_protect
def render_flatpage(request, f):
    if f.registration_required and not request.user.is_authenticated:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.path)
    if f.template_name:
        template = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        template = loader.get_template(DEFAULT_TEMPLATE)
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)

    response = HttpResponse(template.render({'flatpage': f}, request))
    return response


class AuthorBookCreate(generic.CreateView):
    model = 'Author'
    form_class = BookForm
    template_name = 'author_books.html'


class UserProfile(generic.DetailView):
    model = UserProfile
