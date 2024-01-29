from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='FoodImage',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
