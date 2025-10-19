from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

"""
# API Request Permission

AllowAny        # Any use can access authenticated or unauthenticated
IsAuthenticated # Just access authenticated user request
IsAdminUser     # Just Access can admin / staff user request
IsAuthenticatedOrReadOnly # GET Request Allow any user | But [POST, PUT, PATCH, DELETE] authenticated user can access  

"""

# Model Class Permission
"""
Django-তে প্রতিটি model এর জন্য ৪টা permission থাকে:
add_modelname,change_modelname, delete_modelname, view_modelname


DjangoModelPermissions                  #
DjangoModelPermissionsOrAnonReadOnly    #  just can access view_model ,
"""



from rest_framework.permissions import BasePermission

# Just get Method allow
class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):  
        print(view.__class__.__name__)   #  View class name
        print(view.action)               #  'list', 'retrieve', 'create'
        print(view.queryset)            
        return request.method in ['GET']

 
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Just get Method allow
        if request.method in ['GET']:
            return True
        # Checking the current data is owner the reqest user
        return obj.user == request.user
