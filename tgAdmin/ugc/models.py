from django.db import models


class Companies(models.Model):
	name = models.TextField(verbose_name='Название Компании')

	def __str__(self):
		return f'{self.name}'

	class Meta:
		verbose_name = 'Компанию'
		verbose_name_plural = 'Компании'


class Employees(models.Model):
	name = models.TextField(verbose_name='Имя')
	surname = models.TextField(verbose_name='Фамилие')
	patronymic = models.TextField(verbose_name='Отчество', blank=True, null=True)
	company = models.ForeignKey(Companies, on_delete=models.CASCADE, verbose_name='Компания')

	def __str__(self):
		return f'{self.name.title()} {self.surname[0:1].title()}.{self.patronymic[0:1].title()}'

	class Meta:
		verbose_name = 'Сотрудника'
		verbose_name_plural = 'Сотрудники'


class Cars(models.Model):
	model = models.TextField(verbose_name='Модель Автомобиля')
	num_car = models.TextField(verbose_name='Номер Автомобиля')
	color = models.TextField(verbose_name='Цвет Автомобиля')
	driver = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Водитель')

	def __str__(self):
		return f'{self.model}'

	class Meta:
		verbose_name = 'Автомобиль'
		verbose_name_plural = 'Автомобили'


class Security(models.Model):
	name = models.CharField(max_length=30, verbose_name='Имя')
	lastname = models.CharField(max_length=30, verbose_name='Фамилие')
	password = models.CharField(max_length=30, verbose_name='Пароль')
	tg_account_id = models.IntegerField(verbose_name='Telegram Id', blank=True, null=True)
	phone = models.TextField(verbose_name='Телефон номер', blank=True, null=True)
	blocked = models.BooleanField(default=False, verbose_name='Заблокирован')
	block_comment = models.CharField(max_length=255, verbose_name='Причина Блокировки', null=True, blank=True)

	def __str__(self):
		return f'{self.name} {self.lastname}'
	class Meta:
		verbose_name = 'Охранник'
		verbose_name_plural = 'Охранники'

class ParkingSpaces(models.Model):
	busy_spaces = models.IntegerField(verbose_name='Занято мест', default=0)
	all_spaces = models.IntegerField(verbose_name='Все места', default=100)

	def __str__(self):
		return "Места на стоянке"

	class Meta:
		verbose_name = 'Место'
		verbose_name_plural = 'Места'

