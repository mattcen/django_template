#!/usr/bin/env python3
from os import environ
from django.contrib.auth import get_user_model


def run():
    super_username = environ["SUPERUSER_USERNAME"]
    super_password = environ["SUPERUSER_PASSWORD"]
    super_email = environ["SUPERUSER_EMAIL"]

    User = get_user_model()
    if super_username != "" and super_password != "" and super_email != "":
        has_superuser = False
        for u in User.objects.values():
            if u["is_superuser"]:
                has_superuser = True
                break
        if not has_superuser:
            print("Creating super user: " + super_username)
            User.objects.create_superuser(super_username, super_email, super_password)
        else:
            print("Super user already exists. Not creating another.")
