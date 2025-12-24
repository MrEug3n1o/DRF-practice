from rest_framework.views import APIView
from rest_framework.response import Response


class SuccessView(APIView):
    def get(self, request):
        return Response({"status": "payment successful"})

class CancelView(APIView):
    def get(self, request):
        return Response({"status": "payment canceled"})
