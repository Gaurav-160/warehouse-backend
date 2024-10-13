from django.http import JsonResponse
# Adjust according to your project structure
from warehouse.models import Godown, Item
import random
import uuid
from faker import Faker

fake = Faker()

# Existing functions to generate fake data (these remain unchanged)


def generate_godowns(num_godowns):
    godowns = []
    for _ in range(num_godowns):
        godown = {
            'id': str(uuid.uuid4()),
            'name': fake.company(),
            'parent_godown': None  # Initial godowns don't have parents
        }
        godowns.append(godown)
    return godowns


def generate_sub_godowns(godowns, num_sub_godowns):
    sub_godowns = []
    for godown in godowns:
        for _ in range(num_sub_godowns):
            sub_godown = {
                'id': str(uuid.uuid4()),
                'name': fake.company(),
                'parent_godown': godown['id']  # Associate with a parent godown
            }
            sub_godowns.append(sub_godown)
    return sub_godowns


def generate_items(godowns, num_items):
    items = []
    categories = ['Electronics', 'Toys', 'Tools', 'Furniture']
    for _ in range(num_items):
        item = {
            'item_id': str(uuid.uuid4()),
            'name': fake.catch_phrase(),
            'quantity': random.randint(1, 500),
            'category': random.choice(categories),
            'price': round(random.uniform(10.0, 1000.0), 2),
            'status': 'in_stock' if random.random() > 0.2 else 'out_of_stock',
            'godown_id': random.choice(godowns)['id'],
            'brand': fake.company(),
            'attributes': {
                'material': random.choice(['Plastic', 'Wood', 'Metal']),
                'warranty_years': random.randint(1, 5),
                'color': fake.color_name()
            },
            'image_url': fake.image_url()
        }
        items.append(item)
    return items
