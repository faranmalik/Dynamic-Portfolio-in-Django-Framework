from django.contrib import admin
from .models import Header, Education, Skill, Experience, Project, Contact


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'title_line', 'profile_image')


admin.site.register(Header, HeaderAdmin)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contact)
