"""EncodingDetect: Detects text file encodings and converts them to UTF-8 in bulk."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]