from typing import Callable, Tuple, Any, Type


def error_wrapper(
        func: Callable,
        pass_exceptions: Tuple[Type[Exception]] = None,
        retry_exceptions: Tuple[Type[Exception]] = None,
        delays: list = None,
        *args,
        **kwargs
) -> Any: ...


def error_handler(
        pass_exceptions: Tuple[Type[Exception]] = None,
        retry_exceptions: Tuple[Type[Exception]] = None,
        delays: list = None,
) -> Any: ...
