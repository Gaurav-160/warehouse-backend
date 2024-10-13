from rest_framework import viewsets
from django.http import JsonResponse
from .models import Godown, Item
from .serializers import GodownSerializer, ItemSerializer
from .functions import *


class GodownViewSet(viewsets.ModelViewSet):
    queryset = Godown.objects.all()
    serializer_class = GodownSerializer

    def get_queryset(self):
        # Return only top-level godowns (where parent_godown is null)
        return Godown.objects.filter(parent_godown__isnull=True)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def generate_fake_data(request):
    print("Generating fake data!")

    # Generate Fake Data
    godowns = generate_godowns(3)
    sub_godowns = generate_sub_godowns(godowns, 0)
    items = generate_items(godowns + sub_godowns, 4)

    # Combine Godowns and Sub-Godowns
    all_godowns = godowns + sub_godowns

    # Save Godowns to the database
    for godown in all_godowns:
        # Set parent_godown to the actual Godown instance or None
        parent_godown = None
        if godown['parent_godown']:
            parent_godown = Godown.objects.get(id=godown['parent_godown'])

        new_godown = Godown.objects.create(
            id=godown['id'],
            name=godown['name'],
            parent_godown=parent_godown  # Assign the actual instance
        )

    # Save Items to the database
    for item in items:
        # Fetch the actual Godown instance for godown_id
        godown_instance = Godown.objects.get(id=item['godown_id'])

        Item.objects.create(
            item_id=item['item_id'],
            name=item['name'],
            quantity=item['quantity'],
            category=item['category'],
            price=item['price'],
            status=item['status'],
            godown=godown_instance,  # Use the actual Godown instance
            brand=item['brand'],
            # Ensure your Item model can handle this
            attributes=item['attributes'],
            image_url=item['image_url']
        )

    # Output response
    response_data = {
        "total_godowns": len(all_godowns),
        "total_items": len(items)
    }

    return JsonResponse(response_data)

