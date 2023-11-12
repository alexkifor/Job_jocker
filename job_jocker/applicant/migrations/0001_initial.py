# Generated by Django 4.2.6 on 2023-10-23 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='applicant', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('skills', models.TextField(blank=True, null=True)),
                ('education', models.CharField(max_length=256)),
                ('experience', models.TextField(default='Без опыта')),
                ('salary', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(choices=[('ЧЕРНОВИК', 'ЧЕРНОВИК'), ('РАССМОТРЕНИЕ', 'РАССМОТРЕНИЕ'), ('ОПУБЛИКОВАНО', 'ОПУБЛИКОВАНО'), ('ОТКЛОНЕНО', 'ОТКЛОНЕНО')], default='ЧЕРНОВИК', max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.applicant')),
            ],
        ),
    ]
