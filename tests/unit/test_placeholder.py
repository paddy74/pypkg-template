"""Placeholder tests for basic functions of a Python package"""


def test_pkgimports() -> None:
    """A trivial test to ensure the package can be imported."""
    from thispackage import _version

    assert _version.__title__
