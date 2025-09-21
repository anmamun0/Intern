from blogs.models import Blog

def my_context(request):
    return {
        'current_user': request.user,
        'recent_blogs': Blog.objects.order_by('-created_at') 
        # 'recent_blogs': Blog.objects.order_by('-created_at')[:5]
    }
