from mypy_repro.utils import NestedDict, parse


def f(x: str, result: NestedDict) -> None:
    assert parse(x) == result
