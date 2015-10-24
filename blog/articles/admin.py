from django.contrib import admin

# Register your models here.

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','date')
    list_filter = ['date']
    search_fields = ['title']

    def get_search_results(self, request, queryset, search_term):
        print("search overide")
        queryset, use_distinct = super().get_search_results(request,queryset,search_term)
        return queryset,True

admin.site.register(Article,ArticleAdmin)

