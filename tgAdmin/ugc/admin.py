from django.contrib import admin
from .models import Companies, Cars, Employees, Security, ParkingSpaces
from .forms import CompaniesForm, CarForm, EmployeesForm, SecurityForm
from django.contrib.auth.models import Group


@admin.register(Companies)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    fields = ('name',)
    list_display = ('name',)
    form = CompaniesForm


@admin.register(Cars)
class CarAdd(admin.ModelAdmin):
    search_fields = ("model__startswith", )
    fields = ('model', 'num_car', 'color', 'driver')
    list_display = ('model', 'num_car', 'color', 'driver')
    form = CarForm


@admin.register(Employees)
class EmployeeAdd(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    fields = ('name', 'surname', 'patronymic', 'company')
    list_display = ('name', 'surname', 'patronymic', 'company')
    form = EmployeesForm


@admin.register(Security)
class SecurityAdd(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    fields = ('name', 'lastname', 'password', 'blocked', 'block_comment')
    list_display = ('name', 'lastname', 'phone', 'tg_account_id', 'password', 'blocked')
    form = SecurityForm


@admin.register(ParkingSpaces)
class SpaceAdd(admin.ModelAdmin):
    fields = ('busy_spaces', 'all_spaces')
    list_display = ('busy_spaces', 'all_spaces')


admin.site.unregister(Group)
admin.site.site_header = "Админка Стоянки"
