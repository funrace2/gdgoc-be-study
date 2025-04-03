from rest_framework.views import APIView
from rest_framework.response import Response

class PostRetrieveUpdate(APIView):
    def get(self, request):
        return Response({"hello": "world"}, status=200)