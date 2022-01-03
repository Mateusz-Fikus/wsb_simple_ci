from rest_framework import viewsets, mixins, generics, status
from rest_framework.response import Response

from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ListOrdersViewSet(viewsets.GenericViewSet,
                        mixins.ListModelMixin):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(customer=self.request.user)

        return queryset


class CreateOrderViewSet(generics.ListCreateAPIView):

    serializer_class = OrderItemSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        order = Order.objects.create(customer=self.request.user,
                                     complete=False)
        data = request.data

        for item in data:
            item["order"] = order.id
            print(data)

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




