# Generated by Django 5.0.6 on 2024-07-03 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0010_rename_customer_id_order_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product_id',
            new_name='product',
        ),
    ]