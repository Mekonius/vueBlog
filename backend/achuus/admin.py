from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group, User
from .models import Achuu_Profile

class UserAdmin(admin.ModelAdmin):
    Model = User
    #Only display the "username field"
    fields = ["username"]
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
    


admin.site.register(Achuu_Profile)
admin.site.unregister(Group)

