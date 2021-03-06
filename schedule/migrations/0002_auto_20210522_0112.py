# Generated by Django 3.2.3 on 2021-05-21 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('useremail', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='fk_todo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.todo', verbose_name='할일'),
        ),
        migrations.AddField(
            model_name='comment',
            name='fk_username',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.user', verbose_name='작성자'),
        ),
        migrations.AddField(
            model_name='todo',
            name='fk_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='schedule.user', verbose_name='작성자'),
        ),
    ]
