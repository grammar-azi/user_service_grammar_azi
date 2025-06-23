import logging
from rest_framework.views import APIView, Response, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from users.serializers.password import ResetPasswordSendCodeSerializer
from users.models import DailyMessage

__all__ = ["ResetPasswordSendCodeView"]

logger = logging.getLogger(__name__) 


class ResetPasswordSendCodeView(APIView):
    """
    View to handle password reset requests by sending a reset code to the user's email.
    """

    @swagger_auto_schema(
        request_body=ResetPasswordSendCodeSerializer,
        tags=["Password"],
        operation_summary="Send password reset code",
        operation_description="Sends a verification code to the user's email address to initiate the password reset process.",
        responses={
            200: openapi.Response(description="Password reset code sent successfully."),
            400: openapi.Response(description="Invalid email or validation error."),
        },
    )
    def post(self, request) -> Response:
        """
        Handle POST request to send a password reset code to the provided email.

        Args:
            request (Request): The request object containing the email for password reset.

        Returns:
            Response: A Response object containing the result of the password reset request.
        """
        logger.info("Password reset request received for email: %s", request.data.get("email"))

        email = request.data.get("email")

        serializer = ResetPasswordSendCodeSerializer(data=request.data)

        if serializer.is_valid():
            message_response = DailyMessage.send_message(email)

            if message_response != "Message sent successfully!":
                return Response(
                    {"error": message_response},
                    status=status.HTTP_429_TOO_MANY_REQUESTS
                )

            response_data = serializer.save()
            logger.info("Password reset code sent successfully to email: %s", request.data.get("email"))
            return Response(response_data, status=status.HTTP_200_OK)

        logger.warning("Password reset failed: %s", serializer.errors)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
