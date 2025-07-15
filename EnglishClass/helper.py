from rest_framework.request import Request
from django.core.exceptions import FieldError
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Model
from rest_framework.serializers import ModelSerializer


# fields
description_search_swagger = "ارسال گویری پارامتر برای جست و جو براساس فیلد های دیتابیس"


# functions
def dynamic_search(request: Request, model: Model, serializer: ModelSerializer):
    """
    a function that you can have dynamic search in every ever
    """
    query_params = request.query_params
    if query_params:
        try:
            query_search = Q()
            for key, value in query_params.items():
                if not value:
                    return Response({
                        "details": f"مقدار برای جست و جو وجود ندارد"
                    }, status=status.HTTP_400_BAD_REQUEST)
                field = key
                if key not in ['id']:
                    field += "__istartswith"
                query_search &= Q(**{f"{field}": value})
            founds = model.objects.filter(query_search)
            return Response(serializer(founds, many=True).data, status=status.HTTP_200_OK)
        except FieldError:
            return Response({
                "details": f"پارامتر های ارسالی معتبر نیستند"
            }, status=status.HTTP_400_BAD_REQUEST)
