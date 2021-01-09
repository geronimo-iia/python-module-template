"""Test unit for module version."""


def test_version_is_defined():
    from  {{cookiecutter.package_name}} import __version__

    assert __version__
