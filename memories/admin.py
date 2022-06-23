from django.contrib import admin
from memories.models import Memory
# Register your models here.
class MemoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Memory, MemoryAdmin)