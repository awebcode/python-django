
# Create your views here.
# myapp/views.py

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger


class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Item.objects.all()

        # Apply filters based on query parameters
        name_contains = request.query_params.get('name_contains')
        if name_contains:
            queryset = queryset.filter(name__icontains=name_contains)

        # Order queryset by id by default (or any other field specified)
        queryset = queryset.order_by('id')

        # Pagination
        paginator = Paginator(queryset, 10)  # 10 items per page
        page_number = request.query_params.get('page')
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        serializer = ItemSerializer(page, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
