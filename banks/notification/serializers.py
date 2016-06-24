from models import *
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('exam', 'qualification', 'vacancies', 'last_date', 'apply_now', 'details')


class CurrentNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurrentNews
        fields = ('title', 'img', 'description', 'created', 'source', 'published')
