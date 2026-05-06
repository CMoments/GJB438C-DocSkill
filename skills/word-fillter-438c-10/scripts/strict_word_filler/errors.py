class StrictTemplateError(RuntimeError):
    """Raised when the template does not match the expected structure."""


class StrictDataError(RuntimeError):
    """Raised when the input JSON data is incomplete or unsupported."""
