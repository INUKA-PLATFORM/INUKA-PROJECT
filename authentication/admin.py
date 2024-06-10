from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.mail import send_mail


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_student')
    actions = ['activate_users']

    def activate_users(self, request, queryset):
        for user in queryset:
            user.is_active = True
            user.save()
            # Send activation email
            send_mail(
                'Account Activated',
                'Dear Your account has been activated. You can now Proceed to login.',
                'kickouthungerke@gmail.com',  
                [user.email],
                fail_silently=False,
            )
        self.message_user(request, "Selected users have been activated and notified via email.")
    activate_users.short_description = "Activate selected users and send activation email"


admin.site.register(User, UserAdmin)
# admin.site.register(User)
admin.site.register(Donation)
