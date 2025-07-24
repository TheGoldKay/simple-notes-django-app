from django.db import migrations

def create_admin_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')

class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20210616_1850'),  # Replace with your latest migration file name
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]