from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from views import *

urlpatterns = [
    url(r'^career/$', csrf_exempt(CareerView.as_view())),
    url(r'^testimonials/$', TestimonialView.as_view()),
    url(r'^subscribe/$', SubscribeView.as_view()),
    url(r'^faq/$', FAQView.as_view())
]