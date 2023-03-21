# Generated by Django 4.1.7 on 2023-03-21 06:13

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SexualOrientation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('image', models.ImageField(blank=True, null=True, upload_to=users.models.upload_path)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('agender', 'Agender'), ('androgynous', 'Androgynous'), ('bigender', 'Bigender'), ('female_to_male', 'Female to male'), ('genderfluid', 'Gender fluid'), ('genderqueer', 'Gender Queer'), ('male_to_female', 'Male to female'), ('FMT', 'FMT'), ('non-binary', 'Non-binary'), ('pangender', 'Pangender')], max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_premium', models.BooleanField(default=False)),
                ('date_of_birth', models.DateField()),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('show_me', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('agender', 'Agender'), ('androgynous', 'Androgynous'), ('bigender', 'Bigender'), ('female_to_male', 'Female to male'), ('genderfluid', 'Gender fluid'), ('genderqueer', 'Gender Queer'), ('male_to_female', 'Male to female'), ('FMT', 'FMT'), ('non-binary', 'Non-binary'), ('pangender', 'Pangender')], max_length=20)),
                ('looking_for', models.CharField(choices=[('long_term_partner', 'Long term partner'), ('short_term_partner', 'Short term partner'), ('friends', 'Friends'), ('still_figuring_out', 'Still figuring out'), ('not_sure', 'Not sure')], max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('passion', models.ManyToManyField(related_name='passion', to='users.passion')),
                ('sexual_orientation', models.ManyToManyField(related_name='sexual_orientation', to='users.sexualorientation')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
