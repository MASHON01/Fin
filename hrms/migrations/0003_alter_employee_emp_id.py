# Generated by Django 4.0.3 on 2022-03-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_mymodel_alter_employee_emp_id_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp367', max_length=70),
        ),
    ]
