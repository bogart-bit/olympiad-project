from django.contrib import admin
from django.urls import path
from tasks.models import Task, Formula
from tasks.admin_import import import_tasks_view, import_formulas_view


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('year', 'grade', 'condition_short', 'correct_answer')
    list_filter = ('year', 'grade')
    search_fields = ('condition', 'correct_answer')
    change_list_template = 'admin/task_changelist.html'

    def condition_short(self, obj):
        return obj.condition[:80] + '...' if len(obj.condition) > 80 else obj.condition
    condition_short.short_description = 'Условие'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('import/', self.admin_site.admin_view(import_tasks_view), name='import_tasks'),
        ]
        return custom + urls


@admin.register(Formula)
class FormulaAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'grade', 'order')
    list_filter = ('year', 'grade')
    search_fields = ('title', 'content')
    change_list_template = 'admin/formula_changelist.html'

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('import/', self.admin_site.admin_view(import_formulas_view), name='import_formulas'),
        ]
        return custom + urls