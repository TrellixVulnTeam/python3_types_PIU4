from django.contrib.auth import views as auth_views
from typing import Any

def get_user_login_form(): ...
def password_management_enabled(): ...
def password_reset_enabled(): ...
def account(request: Any): ...
def change_password(request: Any): ...
def change_email(request: Any): ...

class PasswordResetEnabledViewMixin:
    def dispatch(self, *args: Any, **kwargs: Any): ...

class PasswordResetView(PasswordResetEnabledViewMixin, auth_views.PasswordResetView):
    template_name: str = ...
    email_template_name: str = ...
    subject_template_name: str = ...
    form_class: Any = ...
    success_url: Any = ...

class PasswordResetDoneView(PasswordResetEnabledViewMixin, auth_views.PasswordResetDoneView):
    template_name: str = ...

class PasswordResetConfirmView(PasswordResetEnabledViewMixin, auth_views.PasswordResetConfirmView):
    template_name: str = ...
    success_url: Any = ...

class PasswordResetCompleteView(PasswordResetEnabledViewMixin, auth_views.PasswordResetCompleteView):
    template_name: str = ...

def notification_preferences(request: Any): ...
def language_preferences(request: Any): ...
def current_time_zone(request: Any): ...
def change_avatar(request: Any): ...

class LoginView(auth_views.LoginView):
    template_name: str = ...
    def get_success_url(self): ...
    def get(self, *args: Any, **kwargs: Any): ...
    def get_form_class(self): ...
    def get_context_data(self, **kwargs: Any): ...

class LogoutView(auth_views.LogoutView):
    next_page: str = ...
    def dispatch(self, request: Any, *args: Any, **kwargs: Any): ...
