from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^career/$', CareerView.as_view()),
    url(r'^testimonials/$', TestimonialView.as_view()),
    url(r'^subscribe/$', SubscribeView.as_view())
]