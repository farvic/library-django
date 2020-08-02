from django.shortcuts import render

# Create your views here.

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author

#* class BookListView(generic.ListView):
# *   model = Book
# your own name for the list as a template variable
# *   context_object_name = 'my_book_list'
 # Get 5 books containing the title war
# *   queryset = Book.objects.filter(title__icontains='war')[:5]
# Specify your own template name/location
# *   template_name = 'books/my_arbitrary_template_name_list.html'

    #* def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #*     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #*     context['some_data'] = 'This is just some data'
    #*     return context

# * How to implement the function-based view for resource no found
# def book_detail_view(request, primary_key):
#     try:
#         book = Book.objects.get(pk=primary_key)
#     except Book.DoesNotExist:
#         raise Http404('Book does not exist')
    
#     return render(request, 'catalog/book_detail.html', context={'book': book})
