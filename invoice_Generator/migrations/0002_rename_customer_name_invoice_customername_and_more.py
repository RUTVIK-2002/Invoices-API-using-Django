# Generated by Django 4.0.5 on 2023-07-14 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_Generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='customer_name',
            new_name='customerName',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='invoice_no',
            new_name='invoiceNo',
        ),
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='unit_price',
            new_name='unitPrice',
        ),
    ]
