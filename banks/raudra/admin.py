from django.contrib import admin
from models import Testimonial, Career


class TestimonialAdmin(admin.ModelAdmin):

    class Meta:
        model = Testimonial

    list_display = ('name', 'college', 'created')


class CareerAdmin(admin.ModelAdmin):

    class Meta:
        model = Career

    list_display = ('first_name', 'last_name', 'email')

admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Career, CareerAdmin)