from rest_framework import serializers

from .models import Lead


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'first_name', 'last_name', 'email', 'is_contacted',
                  'notes', 'created_at', 'updated_at')
