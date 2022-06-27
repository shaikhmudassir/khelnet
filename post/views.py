from .models import PostModel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
from rest_framework import serializers

        
class PostViewSet(viewsets.ModelViewSet):
    queryset = PostModel.objects.filter()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)