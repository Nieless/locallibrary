from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.contrib.flatpages.models import FlatPage
from models import ExtendedFlatPage

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)






class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = ExtendedFlatPage
        fields = '__all__'

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites','image','template_name','page_type')}),
    )

    def save_model(self, request, obj, form, change):
        if request.method == "POST" and obj == None:
            image = request.FILES['image']
            ExtendedFlatPage.objects.get_or_create(title=request.POST['title'], url=request.POST['url'], template_name=request.POST['template_name'],
                content=request.POST['content'], page_type=request.POST['page_type'], image=image)
            

admin.site.unregister(FlatPage)
admin.site.register(ExtendedFlatPage, ExtendedFlatPageAdmin)