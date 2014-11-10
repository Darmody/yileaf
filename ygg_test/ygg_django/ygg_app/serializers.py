__author__ = 'caihuanyu'

from rest_framework import serializers
from django.contrib.auth.models import User

from ygg_app.models import REST, site_hupu_today, site_hupu_topic, site_sinaNBA_video, site_smzdm_notice

class SiteSmzdmNoticeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = site_smzdm_notice

        fields = ('url', 'id', 'zdmLink', 'zdmCoverLink', 'zdmTitle', 'buyLink', 'zdmContent')


class SiteSinaNBAVideoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = site_sinaNBA_video

        fields = ('url', 'id', 'coverAddress', 'videoName', 'videoAddress', 'videoType')

class SiteHupuTodaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = site_hupu_today

        fields = ('url', 'id', 'title', 'titleLink', 'alert', 'alertLink', 'teamlogo1', 'teamlogo2', 'create_time')

class SiteHupuTopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = site_hupu_topic

        fields = ('url', 'id', 'title', 'titleLink', 'reply', 'up', 'create_time')

class RESTSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = REST
        owner = serializers.Field(source = 'owner.username')
        highlighted = serializers.HyperlinkedIdentityField(view_name='rest-highlight', format='html')
        fields = ('url', 'highlighted', 'id', 'title', 'code', 'linenos', 'language', 'style', 'owner', 'created')

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        field = ('username', 'password', 'email')