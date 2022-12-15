from django.contrib import admin
from mainapp.models import News, Course, Lesson, CourseTeacher
from django.utils.html import format_html


admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CourseTeacher)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'deleted')
    list_filter = ('deleted', 'created_at')
    ordering = ('pk',)
    list_per_page = 10
    search_fields = ('title', 'preamble', 'bode',)
    actions = ('mark_as_delete',)

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blanc">{}</a>',
            obj.title.lower().replace(' ', '-'),
            obj.title
        )

    slug.short_description = 'Слаг'

    def mark_as_delete(self, request, queryset):
        queryset.update(delered=True)

    mark_as_delete.short_description = 'Пометить удаленным'
