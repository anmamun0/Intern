 
from django.contrib import admin
from django.urls import path,include
from .views import dashboard_view
from .views import TaskCreateView,TaskDeleteView,TaskUpdateView
from .views import LeaveRequestCreateView,LeaveRequestStatusUpdateView,LeaveRequestListView,TaskChangeStatusView
 

urlpatterns = (
    [    
        path('',dashboard_view,name='dashboard'),

        path('task/create/', TaskCreateView.as_view(), name='create_task'),
        path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
        path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
        
        
        path('task/<int:id>/status/', TaskChangeStatusView.as_view(), name='change_task_status'),
        # ------------------------------------ 
        path('leave-request/new/', LeaveRequestCreateView.as_view(), name='leave-request-create'),
        path('leave-requests/', LeaveRequestListView.as_view(), name='leave-request-list'), 
        path('leave-request/<int:pk>/status/', LeaveRequestStatusUpdateView.as_view(), name='leave-request-status-update'),
    ] 
)
