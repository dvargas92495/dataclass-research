from dataclasses import dataclass

from vargas import vargas


@dataclass
class A:
    foo: str


@vargas
class B:
    foo: str


A(foo="")

B(foo="")  # type: ignore[call-arg]
