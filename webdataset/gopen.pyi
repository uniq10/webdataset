from typing import Any, Optional

info: Any

class Pipe:
    ignore_errors: Any = ...
    ignore_status: Any = ...
    timeout: Any = ...
    args: Any = ...
    proc: Any = ...
    stream: Any = ...
    status: Any = ...
    def __init__(self, *args: Any, mode: Optional[Any] = ..., timeout: float = ..., ignore_errors: bool = ..., ignore_status: Any = ..., **kw: Any) -> None: ...
    def check_status(self) -> None: ...
    def handle_status(self) -> None: ...
    def read(self, *args: Any, **kw: Any): ...
    def write(self, *args: Any, **kw: Any): ...
    def readLine(self, *args: Any, **kw: Any): ...
    def close(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, etype: Any, value: Any, traceback: Any) -> None: ...

def set_options(obj: Any, timeout: Optional[Any] = ..., ignore_errors: Optional[Any] = ..., ignore_status: Optional[Any] = ..., handler: Optional[Any] = ...): ...
def gopen_file(url: Any, mode: str = ..., bufsize: int = ...): ...
def gopen_pipe(url: Any, mode: str = ..., bufsize: int = ...): ...
def gopen_curl(url: Any, mode: str = ..., bufsize: int = ...): ...
def gopen_error(url: Any, *args: Any, **kw: Any) -> None: ...

gopen_schemes: Any

def gopen(url: Any, mode: str = ..., bufsize: int = ..., **kw: Any): ...
def reader(url: Any, **kw: Any): ...