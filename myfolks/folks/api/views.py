from django.db.models import F
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveAPIView
    )

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
    )
from folks.models import Profile,SubCategory,Category
from .serializers import (ProfileCreateSerializer,ProfileListSerializer,
ProfileDeleteSerializer,ProfileUpdateSerializer,ProfileDetailsSerializer,
CategoryListSerializer,SubCategoryListSerializer)


class ProfileCreateAPIView(CreateAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileCreateSerializer


class ProfileListAPIView(ListAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileListSerializer

class ProfileUpdateAPIView(UpdateAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileUpdateSerializer   
    # lookup_field = "id"

class ProfileDeleteAPIView(DestroyAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileDeleteSerializer   
    # lookup_field = "id"   


class ProfileDetailsAPIView(RetrieveAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileDetailsSerializer  


class CategoryListAPIView(ListAPIView):
    queryset= Category.objects.all()
    serializer_class= CategoryListSerializer


class SubCategoryListAPIView(ListAPIView):
    # queryset= SubCategory.objects.filter(category=category_id)
     serializer_class= SubCategoryListSerializer
     lookup_url_kwarg = "pk"        

     def get_queryset(self):
        pk = self.kwargs.get(self.lookup_url_kwarg)
        queryset= SubCategory.objects.filter(category=pk)
        return queryset
    


