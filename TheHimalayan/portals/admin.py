from django.contrib import admin
from portals.models import Post,PoliticalNewsPost,SportsNewsPost,InternationalNewsPost,ScienceNewsPost,BreakingNewsPost

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','body','publish','created','updated','status']
    list_filter=('status','created','publish')
    search_fields=('title','body')
    #raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish']
    prepopulated_fields={'slug':('title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(PoliticalNewsPost,PostAdmin)
admin.site.register(SportsNewsPost,PostAdmin)
admin.site.register(InternationalNewsPost,PostAdmin)
admin.site.register(ScienceNewsPost,PostAdmin)
admin.site.register(BreakingNewsPost,PostAdmin)