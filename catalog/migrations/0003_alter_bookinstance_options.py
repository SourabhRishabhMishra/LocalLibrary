# Generated by Django 3.2.2 on 2021-05-28 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
