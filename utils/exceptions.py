from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            "error": {
                "message": response.data.get("detail", "An error occurred."),
                "status_code": response.status_code,
            }
        }
        return Response(custom_response, status=response.status_code)

    return Response(
        {"error": {"message": "Internal Server Error", "status_code": 500}},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
