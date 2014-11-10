#coding=utf-8
#-*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions

from rest_framework import renderers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import link

from ygg_app.permissions import IsOwnerOrReadOnly
from ygg_app.models import REST, site_hupu_today, site_hupu_topic, site_hupu_data, site_sinaNBA_video, site_smzdm_notice
from ygg_app.serializers import RESTSerializer, UserSerializer, SiteHupuTodaySerializer, SiteHupuTopicSerializer, \
    SiteSinaNBAVideoSerializer, SiteSmzdmNoticeSerializer

# import lxml.html as HTML
# import urllib2

def index(request):

    return render_to_response('v2.1/index.html', {})


def home(request):

    return render_to_response('v2.1/base.html', {})

def hupu(request):

    hupuData = site_hupu_data.objects.all()
    sinaNBAVideo = site_sinaNBA_video.objects.all()
    smzdmNotice = site_smzdm_notice.objects.all()


    param = {'hupuData': hupuData, 'sinaNBAVideo': sinaNBAVideo, 'smzdmNotice': smzdmNotice}

    return render_to_response('v2.1/nba.html', param)

def music(requset):

    return render_to_response('v2/music.html')

def zdm(request):

    return render_to_response('v2/zdm.html')

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'rests': reverse('rest-list', request=request, format=format)
    })

class SmzdmNoticeViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = site_smzdm_notice.objects.all()
    serializer_class = SiteSmzdmNoticeSerializer
    permission_classes = (permissions.AllowAny,)
    paginate_by = 30

class HupuTodayViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = site_hupu_today.objects.all()
    serializer_class = SiteHupuTodaySerializer
    permission_classes = (permissions.AllowAny,)
    paginate_by = 30


class HupuTodayViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = site_hupu_today.objects.all()
    serializer_class = SiteHupuTodaySerializer
    permission_classes = (permissions.AllowAny,)
    paginate_by = 30

class HupuTopicViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = site_hupu_topic.objects.all()
    serializer_class = SiteHupuTopicSerializer
    permission_classes = (permissions.AllowAny,)
    paginate_by = 16

class SinaNBAVideoViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = site_sinaNBA_video.objects.order_by("videoType")
    serializer_class = SiteSinaNBAVideoSerializer
    permission_classes = (permissions.AllowAny,)
    paginate_by = 200

class RESTViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = REST.objects.all()
    serializer_class = RESTSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @link(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        rest = self.get_object()
        return Response(rest.highlighted)

    def pre_save(self, obj):
        obj.owner = self.request.user

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer