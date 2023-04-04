from rest_framework import serializers

from addwords.models import Word



class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('word', 'translation', 'add_date')