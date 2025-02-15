from django.db import models
from typing import Any

class Registration(models.Model):
    first_name: Any = ...
    last_name: Any = ...
    email: Any = ...
    phone_number: Any = ...
    submitted: Any = ...
    validated: Any = ...
    class Meta:
        ordering: Any = ...
        verbose_name: str = ...
        verbose_name_plural: str = ...
    @staticmethod
    def has_read_permission(request: Any): ...
    def has_object_read_permission(self, request: Any): ...
    @staticmethod
    def has_create_permission(request: Any): ...
    @property
    def full_name(self): ...
    def __str__(self): ...
