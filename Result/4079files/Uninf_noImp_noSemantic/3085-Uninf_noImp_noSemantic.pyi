from core.views import PermissionMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DeleteView, FormView
from typing import Any

class GroupSubscribe(SuccessMessageMixin, PermissionMixin, CreateView):
    permission_required: str = ...
    form_class: Any = ...
    template_name: str = ...
    success_message: str = ...
    already_subscribed_message: str = ...
    def form_valid(self, form: Any): ...
    def get_form_kwargs(self): ...
    def get_instance(self): ...
    group: Any = ...
    def get_permission_object(self): ...
    def get_success_url(self): ...
    def handle_no_permission(self): ...

class GroupUnsubscribe(PermissionMixin, DeleteView):
    permission_required: str = ...
    model: Any = ...
    template_name: str = ...
    def delete(self, *args: Any, **kwargs: Any): ...
    def get_object(self): ...
    gestalt: Any = ...
    group: Any = ...
    def get_permission_object(self): ...
    def get_success_url(self): ...

class GroupUnsubscribeConfirm(GroupUnsubscribe):
    def delete(self, *args: Any, **kwargs: Any): ...
    token: Any = ...
    gestalt: Any = ...
    group: Any = ...
    def get_permission_object(self): ...
    def has_permission(self): ...

class GroupUnsubscribeRequest(PermissionMixin, FormView):
    permission_required: str = ...
    form_class: Any = ...
    template_name: str = ...
    def form_valid(self, form: Any): ...
    group: Any = ...
    def get_permission_object(self): ...
    def get_success_url(self): ...
