
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20200706_1521'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='tbl_customers',
        ),
    ]
