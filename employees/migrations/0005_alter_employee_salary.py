# Generated by Django 4.2.7 on 2023-11-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0004_alter_employee_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="salary",
            field=models.DecimalField(decimal_places=1, max_digits=12),
        ),
    ]