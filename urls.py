# urls.py
from django.urls import path
from .views import StateListView, StateDetailView, StateCreateView, StateUpdateView, StateDeleteView

urlpatterns = [
    path('', StateListView.as_view(), name='state_list'),
    path('<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('create/', StateCreateView.as_view(), name='state_create'),
    path('update/<int:pk>/', StateUpdateView.as_view(), name='state_update'),
    path('delete/<int:pk>/', StateDeleteView.as_view(), name='state_delete'),
]
