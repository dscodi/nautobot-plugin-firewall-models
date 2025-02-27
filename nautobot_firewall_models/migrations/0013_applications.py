# Generated by Django 3.2.15 on 2022-11-22 21:23

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.models.mixins
import nautobot.extras.models.statuses
import nautobot_firewall_models.utils
import taggit.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0047_enforce_custom_field_slug"),
        ("nautobot_firewall_models", "0012_remove_status_m2m_through_models"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationObject",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("description", models.CharField(blank=True, null=True, max_length=200)),
                ("category", models.CharField(blank=True, null=True, max_length=48)),
                ("subcategory", models.CharField(blank=True, null=True, max_length=48)),
                ("technology", models.CharField(blank=True, null=True, max_length=48)),
                ("risk", models.PositiveIntegerField(blank=True, null=True)),
                ("default_type", models.CharField(blank=True, null=True, max_length=48)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("default_ip_protocol", models.CharField(blank=True, null=True, max_length=48)),
                (
                    "status",
                    nautobot.extras.models.statuses.StatusField(
                        default=nautobot_firewall_models.utils.get_default_status,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="nautobot_firewall_models_applicationobject_related",
                        to="extras.status",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "verbose_name_plural": "Application Objects",
                "ordering": ["name"],
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.CreateModel(
            name="ApplicationObjectGroup",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("description", models.CharField(blank=True, null=True, max_length=200)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name_plural": "Application Object Groups",
                "ordering": ["name"],
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.AlterModelOptions(
            name="natpolicy",
            options={"ordering": ["name"], "verbose_name": "NAT Policy", "verbose_name_plural": "NAT Policies"},
        ),
        migrations.AlterModelOptions(
            name="natpolicyrule",
            options={
                "ordering": ["index"],
                "verbose_name": "NAT Policy Rule",
                "verbose_name_plural": "NAT Policy Rules",
            },
        ),
        migrations.AlterModelOptions(
            name="iprange",
            options={"ordering": ["start_address"], "verbose_name": "IP Range", "verbose_name_plural": "IP Ranges"},
        ),
        migrations.CreateModel(
            name="ApplicationObjectGroupM2M",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "application",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="nautobot_firewall_models.applicationobject"
                    ),
                ),
                (
                    "application_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nautobot_firewall_models.applicationobjectgroup",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="applicationobjectgroup",
            name="application_objects",
            field=models.ManyToManyField(
                blank=True,
                related_name="application_object_groups",
                through="nautobot_firewall_models.ApplicationObjectGroupM2M",
                to="nautobot_firewall_models.ApplicationObject",
            ),
        ),
        migrations.AddField(
            model_name="applicationobjectgroup",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                default=nautobot_firewall_models.utils.get_default_status,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="nautobot_firewall_models_applicationobjectgroup_related",
                to="extras.status",
            ),
        ),
        migrations.AddField(
            model_name="applicationobjectgroup",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.CreateModel(
            name="ApplicationM2M",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "app",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="nautobot_firewall_models.applicationobject"
                    ),
                ),
                (
                    "pol_rule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ApplicationGroupM2M",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "app_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="nautobot_firewall_models.applicationobjectgroup",
                    ),
                ),
                (
                    "pol_rule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="nautobot_firewall_models.policyrule"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="policyrule",
            name="application_groups",
            field=models.ManyToManyField(
                related_name="policy_rules",
                through="nautobot_firewall_models.ApplicationGroupM2M",
                to="nautobot_firewall_models.ApplicationObjectGroup",
            ),
        ),
        migrations.AddField(
            model_name="policyrule",
            name="applications",
            field=models.ManyToManyField(
                related_name="policy_rules",
                through="nautobot_firewall_models.ApplicationM2M",
                to="nautobot_firewall_models.ApplicationObject",
            ),
        ),
    ]
