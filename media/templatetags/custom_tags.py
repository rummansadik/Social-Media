from django import template
from media.models import Notification
from django.contrib.auth.models import Group

register = template.Library()


@register.inclusion_tag('media/show_notifications.html', takes_context=True)
def show_notifications(context):
    request_user = context['request'].user
    notifications = Notification.objects.filter(
        to_user=request_user).exclude(user_has_seen=True).order_by('-date')
    return {'notifications': notifications}


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.filter(name=group_name)
    if group:
        group = group.first()
        return group in user.groups.all()
    else:
        return False
