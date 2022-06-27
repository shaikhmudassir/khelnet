from rest_framework import serializers
from .models import PostModel

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField( max_length=1000,style={'base_template': 'textarea.html', 'rows': 10})
    created = serializers.CharField(required=False,style={'input_type': 'hidden','hide_label':True})
    user = serializers.CharField(required=False,style={'input_type': 'hidden','hide_label':True})

    def create(self, validated_data):
        return PostModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
    
    class Meta:
        model = PostModel
        fields = ['url', 'title', 'content','created','user']
