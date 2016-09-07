from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def get_twitter_url(site):
    if site == settings.ENUCS_SITE:
        return settings.ENUCS_TWITTER_URL
    if site == settings.ENUWS_SITE:
        return settings.ENUWS_TWITTER_URL
