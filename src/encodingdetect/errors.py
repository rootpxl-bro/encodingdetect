"""Typed exceptions for EncodingDetect."""


class encodingdetectError(Exception):
 """Base error for the whole package."""

 exit_code = 1


class ConfigurationError(encodingdetectError):
 """Raised when configuration is invalid or missing."""

 exit_code = 2


class ValidationError(encodingdetectError):
 """Raised when input data fails validation."""

 exit_code = 3


class NotFoundError(encodingdetectError):
 """Raised when a requested resource does not exist."""

 exit_code = 4


class ConflictError(encodingdetectError):
 """Raised when an operation conflicts with existing state."""

 exit_code = 5


class RateLimitError(encodingdetectError):
 """Raised when a rate limit is exceeded."""

 exit_code = 6


class TimeoutError(encodingdetectError):
 """Raised when an operation takes too long."""

 exit_code = 7


class UnsupportedError(encodingdetectError):
 """Raised for unsupported inputs or platforms."""

 exit_code = 8


class StateError(encodingdetectError):
 """Raised when internal state is inconsistent."""

 exit_code = 9


def guard(condition, message, exc=ValidationError):
 """Raise exc(message) when condition is False."""
 if not condition:
 raise exc(message)