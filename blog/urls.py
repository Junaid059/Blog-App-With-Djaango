from django.urls import path
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
#     path('post/<int:pk>/', TemplateView.as_view(template_name='blog/post_detail.html'), name='post-detail'),
 ]