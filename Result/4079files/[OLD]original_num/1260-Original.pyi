# (generated with --quick)

import method_proxy
import queue
from typing import Any, Callable, NoReturn, Type
import unittest.case

MethodWrapperProxy: Type[method_proxy.MethodWrapperProxy]
Queue: Type[queue.Queue]
logger: logging.Logger
logging: module
threading: module
unittest: module

class ActiveObjectProxy(method_proxy.MethodWrapperProxy):
    __doc__: str
    actor: Any
    def __init__(self, actor, delegate) -> None: ...
    @staticmethod
    def enqueue(proxy, target, name, method) -> Callable: ...

class ActiveObjectProxyTest(unittest.case.TestCase):
    def test_actor_thread_terminates(self) -> None: ...
    def test_proxy_methods_execute(self) -> None: ...
    def test_proxy_methods_execute_on_thread(self) -> None: ...

class Actor(threading.Thread):
    __doc__: str
    _commands: queue.Queue[nothing]
    _must_stop: bool
    exception_handler: Any
    def __init__(self) -> None: ...
    def enqueue(self, method, args = ..., kwargs = ...) -> None: ...
    def run(self) -> NoReturn: ...
    def stop(self, *args, **kwargs) -> None: ...

class ActorTest(unittest.case.TestCase):
    nice: bool
    def play_nice(self) -> None: ...
    def produce_exception(self, handler = ...) -> None: ...
    def raise_hell(self, e) -> NoReturn: ...
    def test_actor_continues_running_on_exception_with_handler(self) -> None: ...
    def test_actor_continues_running_on_exception_without_handler(self) -> None: ...

class DoitBackgroundTask:
    called: bool
    def doit(self) -> None: ...
    def test_thread(self, t, test) -> None: ...

def command(method) -> Callable: ...