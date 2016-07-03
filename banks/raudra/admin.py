from django.contrib import admin
from models import Testimonial, Career, FAQ


class TestimonialAdmin(admin.ModelAdmin):

    class Meta:
        model = Testimonial

    list_display = ('name', 'college', 'created')


class CareerAdmin(admin.ModelAdmin):

    class Meta:
        model = Career

    list_display = ('first_name', 'last_name', 'email')


class FAQAdmin(admin.ModelAdmin):

    class Meta:
        model = FAQ


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(FAQ, FAQAdmin)