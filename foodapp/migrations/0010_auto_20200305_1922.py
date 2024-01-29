from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0009_food_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='Address',
        ),
        migrations.AddField(
            model_name='cust',
            name='Address',
            field=models.CharField(default='', max_length=150),
        ),
    ]
