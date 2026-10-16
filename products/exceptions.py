
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Let DRF determine the appropriate HTTP status and error.
    response = exception_handler(exc, context)

    # Return None if DRF cannot handle the exception.
    if response is None:
        return None

    original_data = response.data

    # Errors such as 405 and 401 commonly contain "detail".
    if isinstance(original_data, dict) and "detail" in original_data:
        message = str(original_data["detail"])
        errors = None
    else:
        message = (
            "Validation failed."
            if response.status_code == 400
            else "Request could not be processed."
        )
        errors = original_data

    # Normalize the API error structure.
    response.data = {
        "status": "error",
        "message": message,
    }

    if errors is not None:
        response.data["errors"] = errors

    return response
