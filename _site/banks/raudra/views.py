from serializers import *
from rest_framework.views import APIView, status
from rest_framework.response import Response


class CareerView(APIView):

    def post(self, request):
        req_data = request.data
        serializer = CareerSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            #send mail

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
