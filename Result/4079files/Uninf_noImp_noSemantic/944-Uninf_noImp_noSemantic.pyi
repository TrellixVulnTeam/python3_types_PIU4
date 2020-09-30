from django.contrib import admin
from typing import Any

class Person(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Recipient(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Volunteer(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...
    def Nombre(self, obj: Any): ...
    def Apellidos(self, obj: Any): ...

class Custodian(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Project(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Group(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Event(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Enrolment(admin.ModelAdmin):
    search_fields: Any = ...
    list_display: Any = ...

class Membership(admin.ModelAdmin):
    list_display: Any = ...

class Member(admin.ModelAdmin):
    list_display: Any = ...