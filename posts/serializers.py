from rest_framework.serializers import ModelSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"



# pagination
class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'result': data,
        })