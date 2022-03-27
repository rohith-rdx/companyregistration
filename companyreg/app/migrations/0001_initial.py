# Generated by Django 4.0 on 2022-03-14 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='companys',
            fields=[
                ('cmpnyid', models.AutoField(primary_key=True, serialize=False)),
                ('cmpnyname', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('businessname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobno', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
                ('logo', models.ImageField(default='default.png', upload_to='images')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]