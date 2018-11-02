# Generated by Django 2.1 on 2018-11-02 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerobicicleta', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=30)),
                ('rin', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cardinalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcioncardinalidad', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionciudad', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrpciondepartamento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Geolocalizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitudgeolocalizacion', models.IntegerField()),
                ('longitudgeolocalizacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlimagen', models.ImageField(blank=True, null=True, upload_to='img/fotosapp/')),
                ('bicicleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Bicicleta')),
            ],
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letrauno', models.CharField(max_length=1)),
                ('bis', models.CharField(max_length=3)),
                ('letrados', models.CharField(max_length=1)),
                ('numerocalle', models.CharField(max_length=3)),
                ('letratres', models.CharField(max_length=1)),
                ('numerocomplemento', models.CharField(max_length=3)),
                ('email', models.CharField(max_length=30)),
                ('cardinalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Cardinalidad')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroidentificacion', models.IntegerField()),
                ('nombrepropietario', models.CharField(max_length=30)),
                ('apellidopropietario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tipocalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripciontipocalle', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipoidentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripciontipoidentificacion', models.TextField()),
                ('siglatipoidentificacion', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='propietario',
            name='tipoidentificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Tipoidentificacion'),
        ),
        migrations.AddField(
            model_name='propietario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='localizacion',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Propietario'),
        ),
        migrations.AddField(
            model_name='localizacion',
            name='tipocalle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Tipocalle'),
        ),
        migrations.AddField(
            model_name='geolocalizacion',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Propietario'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movil.Departamento'),
        ),
    ]
