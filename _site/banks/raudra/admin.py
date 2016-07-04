from django.contrib import admin
from models import Testimonial


class TestimonialAdmin(admin.ModelAdmin):

    class Meta:
        model = Testimonial

    list_display = ('name', 'college', 'created')


admin.site.register(Testimonial, TestimonialAdmin)
