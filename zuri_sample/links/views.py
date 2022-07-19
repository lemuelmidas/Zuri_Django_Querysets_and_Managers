from django.shortcuts import render

# Create your views here.


#import local viewsets
from rest_framework import viewsets

#import local data
from .serializers import LinkSerializer
from .models import Links


#create a viewset
class PostListApi(viewsets.ListAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostCreateApi(viewsets.CreateAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostDetailApi(viewsets.RetrieveAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostUpdateApi(viewsets.UpdateAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostDeleteApi(viewsets.DestroyAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)