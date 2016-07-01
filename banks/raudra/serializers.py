from models import *
from rest_framework import serializers


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial


class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
