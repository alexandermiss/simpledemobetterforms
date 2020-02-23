# Generated by Django 2.2.10 on 2020-02-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=150)),
                ('colonia', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='empleado',
            name='categoria',
            field=models.CharField(choices=[('0', 'Secretario'), ('1', 'Tesorero'), ('2', 'Jefe')], max_length=2),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='individuos', related_query_name='individuo', to='catalogos.Persona'),
        ),
        migrations.AddField(
            model_name='persona',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='domicilios', related_query_name='domicilio', to='catalogos.Domicilio'),
        ),
    ]