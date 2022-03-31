from django import forms
from django.forms import ValidationError

from .models import Companies, Cars, Employees, Security


class CarForm(forms.ModelForm):
    def clean_num_car(self):
        num_car = self.cleaned_data.get('num_car')
        if isinstance(num_car, str):
            num_car = num_car.replace(" ", "")
        return num_car
    class Meta:
        model = Cars
        fields = {
			'model',
			'num_car',
			'color',
			'driver'
		}
        widgets = {
			'model': forms.TextInput,
			'num_car': forms.TextInput,
			'color': forms.TextInput
		}


class EmployeesForm(forms.ModelForm):
	class Meta:
		model = Employees
		fields = {
			'name',
			'surname',
			'patronymic',
			'company'
		}
		widgets = {
			'name': forms.TextInput,
			'surname': forms.TextInput,
			'patronymic': forms.TextInput,
		}


class CompaniesForm(forms.ModelForm):
	class Meta:
		model = Companies
		fields = {
			'name',
		}
		widgets = {
			'name': forms.TextInput,
		}


class SecurityForm(forms.ModelForm):
    def clean_block_comment(self):
        fieldBlocked = self.cleaned_data.get('blocked')
        fieldBlockedComment = self.cleaned_data.get('block_comment')

        if fieldBlocked and fieldBlockedComment == None or isinstance(fieldBlockedComment, str) and len(fieldBlockedComment) < 3:
            raise ValidationError("Укажите причину блокировки")

        return fieldBlockedComment
    class Meta:
        model = Security
        fields = '__all__'
        widgets = {
            'block_comment': forms.Textarea,
        }
