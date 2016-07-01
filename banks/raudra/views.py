from serializers import *
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import generics
from django.conf import settings
from django.core.mail import send_mail

class CareerView(APIView):

    def post(self, request):
        import pdb;pdb.set_trace()
        req_data = request.data
        serializer = CareerSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            #send mail

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestimonialView(generics.ListAPIView):

    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class SubscribeView(APIView):

    def send_mail(self, data):
        send_mail("Ravindra Babu Ravula", "Thanks For Subscribing Updates. Soon You will get new updates regarding courses",
                  settings.EMAIL_HOST_USER, [data.get('email'),])

    def post(self, request):
        req_data = request.data
        serializer = SubscribeSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            #send mail
            self.send_mail(serializer.data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
