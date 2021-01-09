"""{{cookiecutter.project_name}} definition."""
from pkg_resources import get_distribution, DistributionNotFound

__all__ = ["__version__"]

try:
    __version__ = get_distribution('{{cookiecutter.package_name}}').version
except DistributionNotFound:  # pragma: no cover
    __version__ = '(local)'
