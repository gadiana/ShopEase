# Generated by Django 4.0 on 2023-12-06 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0008_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cartname', models.CharField(max_length=255)),
                ('store_wheretobuy', models.CharField(max_length=255)),
                ('date_for_notification', models.DateField()),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('cart', models.ForeignKey(db_column='cart_id', on_delete=django.db.models.deletion.CASCADE, to='main.cart')),
            ],
        ),
    ]
