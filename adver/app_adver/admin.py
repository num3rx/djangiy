from django.contrib import admin
from .models import Advertisements

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'updated_at', 'auction']

    fieldsets = (
        (
            'Общее', {
                'fields': ('title', 'description')
            }
        ),
        (
            'Финансы', {
                'fields': ('price', 'auction'),
                'classes': ['collapse']
            }
        )
    )

    list_filter = ['auction', 'created_at']

    actions = ['make_auction_disabled', 'make_auction_enabled']


    @admin.action(description='Убрать возможность торга')
    def make_auction_disabled(self, request, queryset):
        queryset.update(auction=False)


    @admin.action(description='Добавить возможность торга')
    def make_auction_enabled(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisements, AdvertisementAdmin)
