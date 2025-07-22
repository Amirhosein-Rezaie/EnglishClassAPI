from . import models
from . import serializers
from rest_framework.viewsets import ModelViewSet
from EnglishClass.permissions import (DeleteForAdmin, NotAllow)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from EnglishClass.helper import dynamic_search, description_search_swagger
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
from django.http import HttpResponse
from io import BytesIO


# terms
class TermViewset(ModelViewSet):
    serializer_class = serializers.TermSerializer
    queryset = models.Terms.objects.all()
    permission_classes = [DeleteForAdmin]

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Terms,
                                  serializer=serializers.TermSerializer)
        return super().list(request, *args, **kwargs)


# register
class RegisterViewset(ModelViewSet):
    serializer_class = serializers.RegisterSerializer
    queryset = models.Registers.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Registers,
                                  serializer=serializers.RegisterSerializer)
        return super().list(request, *args, **kwargs)


# grades
class GradeViewset(ModelViewSet):
    serializer_class = serializers.GradeSerializer
    queryset = models.Grades.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.Grades,
                                  serializer=serializers.GradeSerializer)
        return super().list(request, *args, **kwargs)


# book sales
class BookSaleViewset(ModelViewSet):
    serializer_class = serializers.BookSaleSerializer
    queryset = models.BookSales.objects.all()
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['DELETE']:
            return [NotAllow()]
        return super().get_permissions()

    @extend_schema(
        description=description_search_swagger
    )
    def list(self, request: Request, *args, **kwargs):
        if request.query_params:
            return dynamic_search(request=request, model=models.BookSales,
                                  serializer=serializers.BookSaleSerializer)
        return super().list(request, *args, **kwargs)


# export excel file of terms
class export_terms_excel(APIView):
    def get(self, request: Request):
        wb = Workbook()
        ws = wb.active
        ws.sheet_view.rightToLeft = True
        ws.title = 'terms'

        # general style
        # # border
        side = Side(style='thin')
        border = Border(right=side, bottom=side, top=side)
        # # aligment
        alignment = Alignment(horizontal='center', vertical='center')
        # # font
        font = Font(size=14, name='Calibri')
        # # fill
        fill = PatternFill(fill_type='solid', fgColor='fdf2e7')
        # # cell height and width
        height = 25

        # header style
        # # fill
        header_fill = PatternFill(fill_type='solid', fgColor='daf6ff')
        # # cell height and width
        height = 30
        width = 40

        # header
        columns = ['ردیف', 'کتاب زبان اموز', 'کتاب کار', 'کتاب داستان', 'نام معلم',
                   'عنوان', 'شهریه', 'تاریخ شروع', 'تاریخ پایان', 'ساعت شروع', 'ساعت پایان', 'نوع', 'سطح']
        for col in range(len(columns)):
            cell = ws.cell(row=1, column=col+1)
            cell.value = columns[col]
            cell.fill = header_fill
            cell.font = font
            cell.alignment = alignment
            cell.border = border
            ws.column_dimensions[cell.column_letter].width = width
            ws.row_dimensions[1].height = height

        # data
        terms = serializers.TermSerializer(
            models.Terms.objects.all(), many=True).data
        values = []
        row = 2
        for term in terms:
            values = []
            for key, value in dict(term).items():
                if isinstance(value, dict):
                    if 'title' in dict(value).keys():
                        values.append(value['title'])
                    if 'first_name' in dict(value).keys() and 'last_name' in dict(value).keys() and key == 'teacher_detail':
                        values.append(
                            f"{value['first_name']} {value['last_name']}")
                if isinstance(value, str) or key == 'tution':
                    values.append(value)
            for col in range(len(columns)):
                cell = ws.cell(row=row, column=col+1)
                cell.value = values[col - 1] if col != 0 else row - 1
                cell.alignment = alignment
                cell.fill = header_fill if col == 0 else fill
                cell.border = border
            row += 1

        # save the file
        stream = BytesIO()
        wb.save(stream)
        stream.seek(0)

        # send the file
        response = HttpResponse(
            stream.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = f'attachment; filename="terms.xlsx"'
        return response
