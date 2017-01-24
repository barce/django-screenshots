from rest_framework import serializers
from screenshots.models import Screenshot

# class ScreenshotSerializer(serializers.HyperlinkedModelSerializer):
class ScreenshotSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(required=False, allow_blank=True, max_length=255)
    image_url = serializers.CharField(required=False, allow_blank=True, read_only=True)
    filename = serializers.CharField(required=False, allow_blank=True, read_only=True)
    status = serializers.CharField(required=False, allow_blank=True, max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Screenshot.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.url = validated_data.get('url', instance.url)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

