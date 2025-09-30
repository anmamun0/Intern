# signals.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs): 
    if sender.name == 'apps.accounts':  
        Group.objects.get_or_create(name='agent') 
        Group.objects.get_or_create(name='manager')
