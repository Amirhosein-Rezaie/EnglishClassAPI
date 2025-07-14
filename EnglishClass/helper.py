from rest_framework.request import Request
from django.core.exceptions import FieldError
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.db.models import Model
from rest_framework.serializers import ModelSerializer


def dynamic_search(request: Request, model: Model, serializer: ModelSerializer):
    """
    a function that you can have dynamic search in every ever
    """
    query_params = request.query_params
    try:
        query_search = Q()
        for key, value in query_params.items():
            query_search &= Q(**{f"{key}__icontains": value})
        founds = model.objects.filter(query_search)
        return Response(serializer(founds, many=True).data, status=status.HTTP_200_OK)
    except FieldError:
        return Response({
            "detials": f"پارامتر های ارسالی معتبر نیستند"
        }, status=status.HTTP_400_BAD_REQUEST)
