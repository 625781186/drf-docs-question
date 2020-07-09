
from rest_framework import serializers

from .models import UWorksmain


class WorksmainSerializer(serializers.ModelSerializer):
    pk_user_main = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = UWorksmain
        fields = '__all__'

        # depth = 1


class WorksmainBulkSerializer(serializers.Serializer):
    bulk_list = serializers.ListField(help_text = '批量操作的id列表',
        required = True, child = serializers.IntegerField())

    atlas_id = serializers.IntegerField(help_text = '需要替换成的分类id',
        default = -1)
