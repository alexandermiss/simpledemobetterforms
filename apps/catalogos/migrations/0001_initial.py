# Generated by Django 2.1 on 2018-09-10 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[(0, 'Secretario'), (1, 'Tesorero'), (2, 'Jefe')], max_length=2)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.Persona'),
        ),
    ]