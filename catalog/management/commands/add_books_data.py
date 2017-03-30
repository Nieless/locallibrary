import csv
from django.core.management.base import BaseCommand
from locallibrary.settings import BASE_DIR
from catalog.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		print BASE_DIR + '/books.csv'
		with open(BASE_DIR + '/books.csv') as f:
			reader = csv.reader(f)
			for row in reader:
				for i in range(20):
					Book.objects.create(title=row[0],author=Author.objects.get(id=1),summary=row[2],isbn=row[3])
