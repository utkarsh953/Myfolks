from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
            'password',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }



        def validate_email(self, value):
            data = self.get_initial()
            email1 = data.get("email2")
            email2 = value
            if email1 != email2:
                raise ValidationError("Emails must match.")
            
            user_qs = User.objects.filter(email=email2)
            if user_qs.exists():
                raise ValidationError("This user has already registered.")

            return value

    def validate_email2(self, value):
            data = self.get_initial()
            email1 = data.get("email")
            email2 = value
            if email1 != email2:
                raise ValidationError("Emails must match.")
            return value                        

    def create(self, validated_data):
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
                username=username,
                email = email,
                first_name=first_name,
                last_name=last_name
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data




class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    # username = CharField()
    email = EmailField(label='Email Address',required=False,allow_blank=True)
    class Meta:
        model = User
        fields = [
            # 'username',
            'email',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def validate(self,data):
        user_obj = None
        email = data.get("email",None)
        password=data["password"]
        if not email:
            raise ValidationError("Email is required to login")
        user = User.objects.filter(
                    Q(email=email)).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count()==1:
            user_obj = user.first()
        else:
            raise ValidationError("This email is not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials.Please try again.")

        data["token"] = "Some random token"
        return data        






                        