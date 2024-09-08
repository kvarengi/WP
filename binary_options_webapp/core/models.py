from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # tg_user_id = models.IntegerField(blank=True, null=True)
    matter_ballance = models.FloatField(blank=True, null=True)
    idea_ballance = models.FloatField(blank=True, null=True)
    crypto_wallet_address = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Block(models.Model):
    class BlockState(models.IntegerChoices):
        CLOSED = 0, _("Closed")
        OPEN = 1, _("Open")
        FREEZED = 2, _("Freeze")

    # state = models.IntegerField()  # 0 - close, 1 - open, 2 - freeze
    state = models.IntegerField(
        choices=BlockState.choices,
        default=BlockState.OPEN,
    )
    prev_block_hash = models.CharField(max_length=32)  # TODO : adjust max length
    created_at = models.DateTimeField(auto_now_add=True)


class Bet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    block = models.OneToOneField(Block, on_delete=models.RESTRICT)
    bet_percent = models.FloatField()
    start_matter_price = models.FloatField()
    start_idea_price = models.FloatField()
    starts_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField()
