from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, LeaveRequest
from .forms import TaskForm, LeaveRequestForm
from django.shortcuts import render
 
class DashboardView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "employes/dashboard.html"
    context_object_name = "tasks"
    login_url = '/user/login'   
    redirect_field_name = 'next'  

    def get_queryset(self):
        user = self.request.user
        user_groups = user.groups.values_list('name', flat=True)
        is_manager = 'manager' in user_groups

        if is_manager: 
            return Task.objects.all().order_by('-created_at')
        else: 
            return Task.objects.filter(created_by=user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        user_groups = user.groups.values_list('name', flat=True)
        context['is_agent'] = 'agent' in user_groups
        context['is_manager'] = 'manager' in user_groups
 
        if context['is_manager']:
            context['leave_requests'] = LeaveRequest.objects.all().order_by('-created_at')
        else:
            context['leave_requests'] = LeaveRequest.objects.filter(agent=user).order_by('-created_at')

        return context

 
class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "employes/task_form.html"
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.request.user.groups.filter(name='agent').exists()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
 


 
class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "employes/task_form.html"
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        task = self.get_object()
        return self.request.user.groups.filter(name='agent').exists() and task.status != 'approved'
 



class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "employes/confirm_delete.html"
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        task = self.get_object()
        return self.request.user.groups.filter(name='agent').exists() and task.status != 'approved'
 





class TaskChangeStatusView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = "employes/change_status.html"

    def test_func(self):
        return self.request.user.groups.filter(name='manager').exists()

    def get(self, request, id):
        task = get_object_or_404(Task, id=id)
        return render(request, self.template_name, {"task": task})

    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        new_status = request.POST.get("status")
        if new_status in ['approved', 'canceled']:
            task.status = new_status
            task.save()
        return redirect('dashboard')

# ----------------------------------------------
 
class LeaveRequestCreateView(LoginRequiredMixin, CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'employes/leave_request_form.html'
    success_url = reverse_lazy('leave-request-list')

    def form_valid(self, form):  
        form.instance.agent = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class) 
        form.instance.agent = self.request.user
        return form

 
class LeaveRequestListView(LoginRequiredMixin, ListView):
    model = LeaveRequest
    template_name = 'employes/leave_request_list.html'
    context_object_name = 'leave_requests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['approved_count'] = self.get_queryset().filter(status='approved').count()
        return context
    


#  ---------------------- 
  

class LeaveRequestStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LeaveRequest
    fields = ['status']
    template_name = 'leave_request_status_form.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self): 
        return self.request.user.groups.filter(name='manager').exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        leave_request = self.get_object()
        agent_user = leave_request.agent
 
        all_leaves = LeaveRequest.objects.filter(agent=agent_user).order_by('-created_at')
        context['agent_leave_history'] = all_leaves
 
        context['approved_count'] = all_leaves.filter(status='approved').count()
        context['cancelled_count'] = all_leaves.filter(status='canceled').count()   

        return context

