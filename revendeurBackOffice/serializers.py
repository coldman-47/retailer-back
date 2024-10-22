from django.forms import CharField, EmailField, ValidationError
from rest_framework.serializers import ModelSerializer
from revendeurBackOffice.models import Operation, Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'tig_id', 'name', 'category', 'price', 'sale', 'sale_percentage', 'discount', 'comments', 'stock', 'unit_sold')

class OperationSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Operation
        fields = "__all__"
        
        
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
class UserSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = CharField(
        required=True, validators=[validate_password]
    )
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    # def validate(self, attrs):
    #     if attrs['password'] != attrs['password2']:
    #         raise ValidationError({"password": "Password fields didn't match."})

    #     return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user