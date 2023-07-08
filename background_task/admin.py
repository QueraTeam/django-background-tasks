from django.contrib import admin
from background_task.models import Task
from background_task.models import CompletedTask


@admin.action(description="priority += 1")
def inc_priority(modeladmin, request, queryset):
    for obj in queryset:
        obj.priority += 1
        obj.save()


@admin.action(description="priority -= 1")
def dec_priority(modeladmin, request, queryset):
    for obj in queryset:
        obj.priority -= 1
        obj.save()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    display_filter = ["task_name"]
    search_fields = [
        "task_name",
        "task_params",
    ]
    list_display = [
        "task_name",
        "task_params",
        "run_at",
        "priority",
        "attempts",
        "has_error",
        "locked_by",
        "locked_by_pid_running",
    ]
    actions = [inc_priority, dec_priority]


@admin.register(CompletedTask)
class CompletedTaskAdmin(admin.ModelAdmin):
    display_filter = ["task_name"]
    search_fields = [
        "task_name",
        "task_params",
    ]
    list_display = [
        "task_name",
        "task_params",
        "run_at",
        "priority",
        "attempts",
        "has_error",
        "locked_by",
        "locked_by_pid_running",
    ]
