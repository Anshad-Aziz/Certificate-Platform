# Generated by Django 4.2.11 on 2025-05-07 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="plan",
            options={},
        ),
        migrations.AlterModelOptions(
            name="subscription",
            options={},
        ),
        migrations.RemoveField(
            model_name="plan",
            name="description",
        ),
        migrations.RemoveField(
            model_name="plan",
            name="monthly_price",
        ),
        migrations.RemoveField(
            model_name="plan",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="plan",
            name="certificate_limit",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="plan",
            name="name",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="certificates_used",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="plan",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="subscriptions.plan"
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="start_date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
