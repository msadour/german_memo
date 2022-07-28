from django.db.models import Model


def approve(item: Model, is_approved: bool):
    if is_approved is True:
        item.approved = True
        item.save()
    else:
        item.delete()
