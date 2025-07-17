from rest_framework.request import Request
from django.core.exceptions import FieldError
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, Model
from rest_framework.serializers import ModelSerializer
from EnglishClass.pagination import DynamicPagination
from django.db.models import ForeignKey, OneToOneField, ManyToManyField


# fields
description_search_swagger = "ارسال گویری پارامتر برای جست و جو براساس فیلد های دیتابیس"
out_query_params = ['limit', 'page']
paginator = DynamicPagination()

# variables
like = "istartswith"


# functions
def dynamic_search(request: Request, model: Model, serializer: ModelSerializer):
    relation_fields = {
        f.name: f.related_model for f in model._meta.get_fields()
        if isinstance(f, (ForeignKey, OneToOneField))
    }
    query_params = request.query_params
    if query_params:
        try:
            query_search = Q()
            for key, value in query_params.items():
                if key in out_query_params:
                    continue
                if not value:
                    return Response({"details": "مقدار برای جست و جو وجود ندارد"}, status=status.HTTP_400_BAD_REQUEST)

                # if key is a foreignkey
                if key in relation_fields:
                    # get the model of the field
                    related_model = relation_fields[key]

                    # get the fields of the model
                    related_fields = [
                        f.name for f in related_model._meta.get_fields()
                        if f.concrete and not f.auto_created and f.name != 'id'
                    ]

                    # search in the fields
                    sub_query = Q()
                    for sub_field in related_fields:
                        sub_query |= Q(
                            **{f"{key}__{sub_field}__{like}": value})
                    query_search &= sub_query
                else:
                    field = key
                    if key not in ['id']:
                        field += f"__{like}"
                    query_search &= Q(**{f"{field}": value})

            founds = model.objects.filter(query_search).distinct()

            # pagination
            if query_params.get('limit'):
                if query_params.get('limit').lower() == 'none':
                    return Response(serializer(founds, many=True).data, status=status.HTTP_200_OK)
                paginator.page_size = query_params.get('limit')

            paginated_founds = paginator.paginate_queryset(founds, request)
            serialize_found = serializer(paginated_founds, many=True)
            return paginator.get_paginated_response(serialize_found.data)

        except FieldError:
            return Response({
                "details": f"پارامتر های ارسالی معتبر نیستند"
            }, status=status.HTTP_400_BAD_REQUEST)
