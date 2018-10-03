from rest_framework import serializers
from .models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id',  'name' ,'content', 'image','timestamp','updated' )


    # def validate(self, data):

    # 	user =data.get("content", 'None')
    # 	#@import pdb; pdb.set_trace()
    # 	if len(user) >  5:
    # 		raise serializers.ValidationError('Username error ')


	    


    	



