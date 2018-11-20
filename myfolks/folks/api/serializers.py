from rest_framework import serializers
from folks.models import Profile,Category,SubCategory



class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'address', 'contact', 'location')


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name', 'address', 'contact', 'location')  


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','name', 'address', 'contact', 'location')



class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"       
        

class ProfileDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'address', 'contact', 'location') 



class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','desc','catImg')  

class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id','name', 'desc','subCatImg','category')  


