# Generated by Django 3.2.20 on 2023-10-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_favoritevacancies'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='admin_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='date_comment',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(choices=[('ЧЕРНОВИК', 'ЧЕРНОВИК'), ('РАССМОТРЕНИЕ', 'РАССМОТРЕНИЕ'), ('ПУБЛИКАЦИЯ', 'ПУБЛИКАЦИЯ'), ('ДОРАБОТКА', 'ДОРАБОТКА')], default='ЧЕРНОВИК', max_length=12),
        ),
    ]
