import random
from rest_framework.response import Response
from .models import ESIM, Order
from .serializers import OrderSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def buy_esim(request):
    price = request.GET.get('price')
    days = request.GET.get('days')
    region = request.GET.get('region')

    user_id = request.GET.get('user_id')
    
    esims = ESIM.objects.filter(price=price, days=days, region=region)

    if esims.exists():
        tried_esims = set()
        esim = random.choice(esims)
        is_exist = Order.objects.filter(esim=esim, user_id=user_id).exists()
        while is_exist:
            tried_esims.add(esim)
            if len(tried_esims) == esims.count():
                return Response({"error": "No available ESIMs for the user"}, status=400)
            esim = random.choice(esims.exclude(id__in=[e.id for e in tried_esims]))
            is_exist = Order.objects.filter(esim=esim, user_id=user_id).exists()

        order = Order.objects.create(esim=esim, user_id=user_id)
    else:
        return Response({"error": "No ESIMs available for the given criteria"}, status=400)

    serializer = OrderSerializer(order)

    return Response(serializer.data, status=200)

            

