# Generated by Django 4.0.5 on 2023-07-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_Generator', '0003_rename_customername_invoice_customer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_details', to='invoice_Generator.invoice'),
        ),
    ]