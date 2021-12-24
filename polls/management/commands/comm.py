import random
import string

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


def password():
    chars = string.digits + string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(20))


class Commands(BaseCommand):
    users = 'Fake users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 11))

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        faker = Faker()
        for i in range(total):

            try:
                User.objects.create_user(username=faker.name(),
                                         email=faker.email(),
                                         password=password())
            except 11 < total < 0:
                raise ValueError
