from django.core.management.base import BaseCommand
from authapp.models import AuthUser


class Command(BaseCommand):
    def handle(self, *args, **options):

        # Создаем суперпользователя при помощи менеджера модели
        super_user = AuthUser.objects.create_superuser('admin', 'admin@admin.admin', '2222', age=33)