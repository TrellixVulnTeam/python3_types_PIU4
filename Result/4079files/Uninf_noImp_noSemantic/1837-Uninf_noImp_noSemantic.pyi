from vodmanagement.utils import *
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from typing import Any

class VideoFormatFilter(SimpleListFilter):
    title: str = ...
    parameter_name: str = ...
    def lookups(self, request: Any, model_admin: Any): ...
    def queryset(self, request: Any, queryset: Any): ...

class VodModelAdmin(admin.ModelAdmin):
    list_display: Any = ...
    list_display_links: Any = ...
    list_editable: Any = ...
    list_filter: Any = ...
    search_fields: Any = ...
    actions: Any = ...
    form: Any = ...
    fieldsets: Any = ...
    change_form_template: str = ...
    add_form_template: str = ...
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None: ...
    def delete_model(self, request: Any, object: Any) -> None: ...
    def delete_hard(self, request: Any, queryset: Any) -> None: ...
    def copy_objects(self, request: Any, queryset: Any) -> None: ...
    def activate_vod(self, request: Any, queryset: Any) -> None: ...
    def deactivate_vod(self, request: Any, queryset: Any) -> None: ...
    def clear_view_count(self, request: Any, queryset: Any) -> None: ...
    def backup(self, request: Any, queryset: Any): ...
    def backup_all(self, request: Any, queryset: Any): ...
    def transcoding(self, request: Any, queryset: Any) -> None: ...

class VideoCategoryModelAdmin(admin.ModelAdmin):
    list_display: Any = ...
    list_editable: Any = ...
    search_fields: Any = ...
    filter_horizontal: Any = ...
    ordering: Any = ...
    form: Any = ...
    fieldsets: Any = ...
    def category_description(self, obj: Any): ...

class LinkModelAdmin(admin.ModelAdmin):
    list_display: Any = ...
    list_editable: Any = ...

class MultipleUploadModelAdmin(admin.ModelAdmin):
    form: Any = ...
    change_form_template: str = ...
    add_form_template: str = ...

class RestoreModelAdmin(admin.ModelAdmin):
    form: Any = ...
    change_form_template: str = ...
    add_form_template: str = ...
