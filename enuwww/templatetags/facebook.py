from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def get_facebook_url(site):
    if site == settings.ENUCS_SITE:
        return settings.ENUCS_FACEBOOK_URL
    if site == settings.ENUWS_SITE:
        return settings.ENUWS_FACEBOOK_URL
