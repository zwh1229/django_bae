from django import template


register =  template.Library()


@register.filter('mobile')
def mobile(content):
    return  content[:3]+"******"+content[-3:]