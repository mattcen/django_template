from os import environ


def run():
    super_username = environ['SUPERUSER_USERNAME']
    super_password = environ['SUPERUSER_PASSWORD']
    super_email = environ['SUPERUSER_EMAIL']

    if (super_username != '' and super_password != '' and super_email != ''):
        from django.contrib.auth import get_user_model
        from django.contrib.auth.models import User
        has_superuser = False
        for u in User.objects.values():
            if u['is_superuser']:
                has_superuser = True
                break
        if not has_superuser:
            print("Creating super user: " + super_username)
            User = get_user_model()
            User.objects.create_superuser(
                super_username, super_email, super_password)
        else:
            print("Super user already exists. Not creating another.")
