from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from blogs.models import Blog, Comment

@receiver(post_save, sender=Blog)
def blog_created(sender, instance, created, **kwargs):
    if created:
        print(f"New blog created: {instance.title} by {instance.author}")

@receiver(post_delete, sender=Blog)
def delete_blog_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete()
