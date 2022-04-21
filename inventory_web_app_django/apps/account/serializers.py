from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

class AccountRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'first_name', 'last_name', 'department', 'password',)