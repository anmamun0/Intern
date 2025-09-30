from django.urls import path
from .views import (
                    DashboardView, 
                    TaskCreateView, TaskUpdateView, TaskDeleteView, TaskChangeStatusView,
                    LeaveRequestCreateView,LeaveRequestListView,
                    LeaveRequestStatusUpdateView
                    )

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('task/create/', TaskCreateView.as_view(), name='create_task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('task/<int:id>/status/', TaskChangeStatusView.as_view(), name='change_task_status'),


    # ---------------
    path('leave-request/new/', LeaveRequestCreateView.as_view(), name='leave-request-create'),
    path('leave-requests/', LeaveRequestListView.as_view(), name='leave-request-list'), 
    path('leave-request/<int:pk>/status/', LeaveRequestStatusUpdateView.as_view(), name='leave-request-status-update'),
]
