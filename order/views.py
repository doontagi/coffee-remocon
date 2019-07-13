from order.models import Order
from rest_framework import viewsets
from order.serializers import OrderSerializer
from django.shortcuts import reverse, redirect
from django.http import HttpResponseRedirect
# import requests
# import json

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # def perform_create(self, serializer):
    #         print(self.request.user.__dict__)
    #         serializer.save(creator=self.request.user)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=self.request.user)
            user = request.user.username
            return redirect(reverse('kakao_pay') + '?user=' + user)