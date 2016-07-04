from django.contrib import admin
from models import Notification, CurrentNews, Category


class NotificationAdmin(admin.ModelAdmin):

    class Meta:
        model = Notification

    list_display = ('exam', 'vacancies', 'last_date')


class CurrentNewsAdmin(admin.ModelAdmin):

    class Meta:
        model = CurrentNews

    list_display = ('title', 'created')


class CategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Category

admin.site.register(Notification, NotificationAdmin)
admin.site.register(CurrentNews, CurrentNewsAdmin)
admin.site.register(Category, CategoryAdmin)