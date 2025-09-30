from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission 

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name != "accounts":
        return 
    
    manager_group, _ = Group.objects.get_or_create(name="Manager")
    editor_group, _ = Group.objects.get_or_create(name="Editor")
    viewer_group, _ = Group.objects.get_or_create(name="Viewer")

    target_models = ["product", "category", "cart", "cartitem", "order"]
 
    # Manager 
    manager_perms = Permission.objects.filter(content_type__model__in=target_models)
    manager_group.permissions.set(manager_perms)

    # Editor 
    editor_permission = [ "change_product", "view_product",  "change_category", "view_category","change_cart", "view_cart", "change_cartitem", "view_cartitem", "change_order", "view_order",]
    editor_perms = Permission.objects.filter( content_type__model__in=target_models, codename__in=editor_permission,)
    editor_group.permissions.set(editor_perms)

    # Viewer 
    viewer_permission = [  "view_product", "view_category", "view_cart", "view_cartitem", "view_order",]
    viewer_perms = Permission.objects.filter( content_type__model__in=target_models, codename__in=viewer_permission,)
    viewer_group.permissions.set(viewer_perms)
 