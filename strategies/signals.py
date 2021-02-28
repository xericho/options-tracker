from django.db.models.signals import pre_save
from django.dispatch import receiver

# from .models import BasicOption, SpreadOption
#
#
# @receiver(pre_save, sender=BasicOption)
# def calc_fields_basic(sender, instance, **kwargs):
#     if instance.close_price:
#         if instance.longshort == 'long':
#             instance.profitloss = 100*instance.quantity*(instance.close_price-instance.premium)
#         else:
#             instance.profitloss = 100*instance.quantity*(instance.premium-instance.close_price)
#
#     if instance.broker.broker == 'TD':
#         # Comission is 0.65 per option and fees on avg is 0.02
#         instance.fees = instance.quantity*0.67*2
#
#
# @receiver(pre_save, sender=SpreadOption)
# def calc_fields_basic(sender, instance, **kwargs):
#     if instance.close_price:
#         if instance.creditdebit == 'debit':
#             instance.profitloss = 100*instance.quantity*(instance.close_price-instance.premium)
#         else:
#             instance.profitloss = 100*instance.quantity*(instance.premium-instance.close_price)
#
#     if instance.broker.broker == 'TD':
#         # 1.34 because two legs in a spread (0.67*2)
#         instance.fees = instance.quantity*1.34*2
