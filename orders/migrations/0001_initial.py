
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_auto_20200706_1521'),
        ('products', '0002_auto_20200707_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Out for delivery', 'out for delivery')], max_length=100, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.Customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
        ),
    ]
