from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'get_vocabulary', 'get_products', 'author')

    def get_vocabulary(self, obj):
        return "\n".join([p.vocabulary for p in obj.project.all()])

    def get_products(self, obj):
        return "\n".join([p.product for p in obj.project.all()])


admin.site.register(Project, ProjectAdmin)
