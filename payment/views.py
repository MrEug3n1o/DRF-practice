from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.telegram import send_tg_message


class SuccessView(APIView):
    def get(self, request):
        # send_tg_message("Payment Success")
        return Response({"status": "payment successful"})

class CancelView(APIView):
    def get(self, request):
        return Response({"status": "payment canceled"})
