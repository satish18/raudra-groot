from serializers import *
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import generics
from django.conf import settings
from django.core.mail import send_mail
# from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class CareerView(APIView):

    def send_mail_to_user(self, data):
        from_ = settings.EMAIL_HOST_USER
        to_ = (data.get('email'),)
        subject = "Ravindra Babu Ravula"
        body = "<html><h4>Hi, "+ data.get('first_name')+"</h2><br><p>Thanks For applying .</p></html>"
        send_mail(subject, body, from_, to_)

    def get_body_content(self, data):
        body = '<html><body>'
        body += '<table><tr><td>Name</td><td>'+data.get('first_name') + data.get('last_name')+'</td></tr>'
        body += "<tr><td>Email</td><td>"+data.get('email')+"</td></tr>"
        body += "<tr><td>Mobile</td><td>"+data.get('mobile')+"</td></tr>"
        body += "<tr><td>College</td><td>"+data.get('college')+"</td></tr>"
        body += "<tr><td>University</td></td>"+data.get('university')+"</td></tr></table></body></html>"
        return body



    def send_mail_to_raudra(self, data):
        from_ = settings.EMAIL_HOST_USER
        to_ = ('satti.atcha@gmail.com',)
        subject = "Resume For Teaching Assistance, " + data.get('first_name')
        body = self.get_body_content(data)
        msg = EmailMultiAlternatives(subject, body, from_, to_)
        msg.attach_alternative(body, "text/html")
        msg.send()
        # send_mail(subject, body, from_, to_)


    def post(self, request):
        req_data = request.data
        serializer = CareerSerializer(data=req_data)
        if serializer.is_valid():
            serializer.save()
            self.send_mail_to_user(serializer.data)
            self.send_mail_to_raudra(serializer.data)
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


class FAQView(generics.ListAPIView):

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

