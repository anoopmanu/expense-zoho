# Generated by Django 4.2.7 on 2024-03-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0027_alter_expense_expense_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='vendor_source_of_supply',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
