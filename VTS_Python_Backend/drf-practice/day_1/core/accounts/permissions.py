from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

"""
# API Request Permission

AllowAny        # Any use can access authenticated or unauthenticated
IsAuthenticated # Just access authenticated user request
IsAdminUser     # Just Access can admin / staff user request
IsAuthenticatedOrReadOnly # GET Request Allow any user | But [POST, PUT, PATCH, DELETE] authenticated user can access  

"""