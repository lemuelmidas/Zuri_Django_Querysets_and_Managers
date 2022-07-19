#import serializer from rest_framework
from rest_framework import serializers

#create a serializer
class LinkSerializer(serializers.ModelSerializer)
    class Meta:
        model= Links
        fields= (target_url, description, identifier, author, created_date, active)
        