# Generated by Django 3.0.3 on 2020-02-11 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('save', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='completed_items',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.TextField()),
                ('lists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='save.List')),
            ],
        ),
    ]
