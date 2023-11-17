# Generated by Django 4.2.7 on 2023-11-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('deactive', 'deactive')], default='active', max_length=9),
        ),
    ]
