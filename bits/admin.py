from django.contrib import admin
from .models import bp_products, bp_users, bp_pages, ContactModel
# Register your models here.

admin.site.register(bp_users)
admin.site.register(bp_pages)
admin.site.register(bp_products)
admin.site.register(ContactModel)

