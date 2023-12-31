#!/user/bin/env python3
"""
    @File: <filename>.py
    @Version: 0.3.0 to 0.3.0.?
    @Desc: apps | <app> |  <module>
    @Author: Charles Fowler
    @Copyright: 2023
    @Date Created: 23/09/?
    @Date Modified: 23/09/??
    @Python Version: 3.11.04
    @Django Version: 4.2.3/.04/.05
    @Notes / Ideas v Implement:
        - .
    @Changelog:
    - Added:
        - added: Created initial file: 23/09/??:
    - Updated:
        - updated:
    @Plan:
        - TODO:
        - FIXME:
        - CHECK:
"""

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.managers import DashUserManager


class DashUser(AbstractBaseUser, PermissionsMixin):
    """Credit:
    - Author: Sarthak Kumar(@ksarthak4ever)
    - Title: Django Custom User Model + Allauth for OAuth
    - Date Created: 2019-04-02
    - URL: https://medium.com/
    - USER: @ksarthak4ever/
    - SLUG: django-custom-user-model-allauth-for-oauth-20c84888c3184
    - Last Accessed: 2023-09-24
    :class: DashUser: Custom User Model, subclasses: AbstractBaseUser
    :param email:
    :param name:
    :param is_staff: required by admin
    :param is_superuser: PermissionsMixin to grant all permissions
    :param is_active: user active?
    :param last_login:
    :param date_joined:
    :param USERNAME_FIELD: unique id, i.e email
    :param EMAIL_FIELD: re get_email_field_name()
    :param REQUIRED_FIELDS: list of required fields on sigh up
    :param objects: User Manager
    :return: User
    :rtype: User.
    """

    class Meta:  # pylint: disable=R0903
        """Meta definition for DashUser."""
        db_table = 'dashuser'
        app_label = 'users'
        verbose_name = 'DashUser'

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = DashUserManager()

    def get_absolute_url(self):
        """Return the absolute URL for the DashUser instance.

        :return: The absolute URL for the DashUser instance.
        """
        return f"/users/{self.pk}/"

    def __str__(self):
        """Return the string representation of the DashUser instance."""
        return f"{self.name} ({self.email})" \
            if self.name else self.email or "No email"
