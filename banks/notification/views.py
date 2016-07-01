from serializers import *
from rest_framework import generics

class NotificationView(generics.ListAPIView):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class CurrentNewsView(generics.ListAPIView):

    queryset = CurrentNews.objects.all()
    serializer_class = CurrentNewsSerializer
