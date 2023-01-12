from rest_framework import viewsets
from .models import Category, QuestionAnswer
from .serializers import CategorySerializer, QuestionAnswerSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PostPagePagination(PageNumberPagination):
    page_size = 3


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuestionAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['question', 'category']
    search_fields = ['answer']
    ordering_fields = ['importance']
    pagination_class = PostPagePagination