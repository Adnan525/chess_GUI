from _typeshed import Incomplete

from .context import Context as _Context

class AsyncContext(_Context):
    def __init__(self, *args, loop: Incomplete | None = None, use_task_factory: bool = True, **kwargs) -> None: ...
    def clear_trace_entities(self) -> None: ...

class TaskLocalStorage:
    def __init__(self, loop: Incomplete | None = None) -> None: ...
    def __setattr__(self, name: str, value) -> None: ...
    def __getattribute__(self, item: str): ...
    def clear(self) -> None: ...

def task_factory(loop, coro): ...
