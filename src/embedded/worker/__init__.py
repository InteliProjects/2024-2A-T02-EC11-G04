# Package metadata
__version__ = "1.0.0"
__author__ = "greentech"


# Packge modules, submodules and functions importing
from .worker import Worker


# Defined importing for '*' wildcard
__all__ = ["Worker"]