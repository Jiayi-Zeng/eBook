# models.py
from django.db import models
from wagtail.admin.filters import WagtailFilterSet


class Member(models.Model):
    class ShirtSize(models.TextChoices):
        SMALL = "S", "Small"
        MEDIUM = "M", "Medium"
        LARGE = "L", "Large"
        EXTRA_LARGE = "XL", "Extra Large"

    name = models.CharField(max_length=255)
    shirt_size = models.CharField(max_length=5, choices=ShirtSize.choices, default=ShirtSize.MEDIUM)

    def get_shirt_size_display(self):
        return self.ShirtSize(self.shirt_size).label

    get_shirt_size_display.admin_order_field = "shirt_size"
    get_shirt_size_display.short_description = "Size description"


class MemberFilterSet(WagtailFilterSet):
    class Meta:
        model = Member
        fields = ["shirt_size"]