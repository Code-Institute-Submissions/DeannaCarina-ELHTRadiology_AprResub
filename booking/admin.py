from django.contrib import admin
from .models import XrayAppointment, CtAppointment, MriAppointment, FluoroAppointment, AngioAppointment



# Register your models here.

admin.site.register(XrayAppointment)

admin.site.register(CtAppointment)

admin.site.register(MriAppointment)

admin.site.register(FluoroAppointment)

admin.site.register(AngioAppointment)