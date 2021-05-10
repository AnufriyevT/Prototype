from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'vocabulary', 'products', 'author')

    def vocabulary(self, obj):
        return "\n".join([vocabulary.term for vocabulary in obj.vocabulary.all()])

    def products(self, obj):
        return "\n".join([product.name for product in obj.product.all()])


admin.site.register(Project, ProjectAdmin)
