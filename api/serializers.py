from django.forms import widgets
from rest_framework import serializers
from api.models import Source, Map, Comment
from django.contrib.auth.models import User
from rest_framework import serializers

class TagListSerializer(serializers.WritableField):
    def from_native(self, data):
        # if type(data) is not list:
        #     print data
        #     raise ParseError("expected a list of data")     
        return data
     
    def to_native(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj

class SourceSerializer(serializers.ModelSerializer):
    # user = serializers.Field(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    # communities = serializers.HyperlinkedRelatedField(view_name='community-detail', lookup_field='name', required=False, read_only=True)
    # community = serializers
    user = serializers.Field(source='owner')
    created = serializers.Field(source='created')
    tags = TagListSerializer(blank=True)

    class Meta:
        model = Source
        fields = ('id', 'name', 'description', 'map', 'user', 'latitude', 'longitude', 'created', 'tags')        

class MapSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.Field(source='owner.username')
    sources = SourceSerializer(many=True, read_only=True)
    class Meta:
        model = Map
        fields = ('name', 'namespace', 'id', 'sources', 'description')
        # read_only_fields = ('namespace')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # communities = serializers.HyperlinkedRelatedField(many=True, view_name='community-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'map')

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='owner')
    created = serializers.Field(source='created')
    class Meta:
        model = Comment
        fields = ('created', 'user', 'content', 'source')
