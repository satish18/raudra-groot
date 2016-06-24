from models import *
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('exam', 'qualification', 'vacancies', 'last_date', 'apply_now', 'details')


class CurrentNewsSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()

    class Meta:
        model = CurrentNews
        fields = ('title', 'img', 'description', 'category', 'created', 'source', 'published')

    def get_category(self, obj):
        return obj.category.name
