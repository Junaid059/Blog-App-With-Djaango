from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import BasePermission, IsAdminUser,DjangoModelPermissionsOrAnonReadOnly

class CustomUserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET','POST','PUT','DELETE']:
            return request.user and request.user.is_staff
        return True

class PostList(generics.ListCreateAPIView):
    permission_classes = [CustomUserPermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomUserPermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer