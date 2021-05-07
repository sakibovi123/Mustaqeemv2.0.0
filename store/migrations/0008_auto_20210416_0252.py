# Generated by Django 3.1.7 on 2021-04-15 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210415_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='LocalGroceryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='brand_slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat_slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='campaign',
        ),
        migrations.RemoveField(
            model_name='product',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_slug',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='shop_slug',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='sub_slug',
        ),
        migrations.AddField(
            model_name='product',
            name='isFavorite',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='title',
            field=models.CharField(max_length=120, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]