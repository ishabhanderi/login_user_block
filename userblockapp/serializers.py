from rest_framework import serializers
from userblockapp.models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        # fields = '__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }
