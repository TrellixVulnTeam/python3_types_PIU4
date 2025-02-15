from typing import Any

def shortcut_manager(mocker: Any): ...
def task_button(mocker: Any): ...
def subject(mocker: Any, shortcut_manager: Any, task_button: Any): ...
def test_interface_compliance(subject: Any) -> None: ...
def test_module(graph: Any) -> None: ...

class TestInitialize:
    def test_should_initialize_shortcuts_and_session_buttons(self, subject: Any, task_button: Any, shortcut_manager: Any) -> None: ...

class TestRun:
    def test_should_call_gtk_main(self, mocker: Any, subject: Any) -> None: ...

class TestHide:
    def test_should_minimize_when_none_tray_plugin_is_enabled(self, subject: Any) -> None: ...
    def test_should_hide_in_tray_when_a_tray_plugin_is_enabled(self, subject: Any) -> None: ...

class TestQuit:
    def test_should_quit_when_timer_is_not_running(self, mocker: Any, subject: Any) -> None: ...
    def test_should_hide_when_timer_is_running(self, subject: Any, mocker: Any) -> None: ...

class TestShow:
    def test_should_present_window(self, subject: Any, mocker: Any) -> None: ...
