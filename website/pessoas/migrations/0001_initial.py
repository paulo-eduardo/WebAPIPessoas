# Generated by Django 2.0.5 on 2018-05-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('R', 'Rather not say')], default='R', max_length=10)),
                ('age', models.IntegerField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
