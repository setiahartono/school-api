from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver

from api.models import School, ChangeLog, Student


def track_to_changelog(instance, kwargs):
    changes_summary = []
    final_summary = ""
    class_name = instance.__class__.__name__

    if kwargs['created']:
        # If created, record it
        changes_summary.append(f"CREATED: {class_name} {instance}")
    else:
        # Give a brief summary of changes, for each changed field
        for field, value in instance.changed_data.items():
            if final_summary == "":
                final_summary = "CHANGED: "
            narration = f"{field}: {value} -> {instance.__dict__[field]}"
            changes_summary.append(narration)

    final_summary += ", ".join(changes_summary)
    if final_summary != "":
        ChangeLog.objects.create(
            model_name=f"{class_name}",
            instance_id=instance.id,
            action = final_summary
        )


def track_changelog_delete(instance):
    class_name = instance.__class__.__name__
    ChangeLog.objects.create(
        model_name=class_name,
        instance_id=instance.id,
        action=f"DELETED: {class_name} - {instance.id}"
    )


@receiver(pre_save, sender=School)
@receiver(pre_save, sender=Student)
def pre_save_signal(sender, instance, **kwargs):
    # Track changes before save
    instance.changed_data = instance.tracker.changed()


@receiver(post_save, sender=School)
@receiver(post_save, sender=Student)
def post_save_signal(sender, instance, **kwargs):
    # Create changelog after saving
    track_to_changelog(instance, kwargs)


@receiver(post_delete, sender=School)
@receiver(post_delete, sender=Student)
def post_delete_signal(sender, instance, **kwargs):
    # Post delete signal
    track_changelog_delete(instance)
