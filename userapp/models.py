# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAppuser(models.Model):
    realname_status = (
        (0, '未实名认证'),
        (1, '已实名认真')
    )

    user_id = models.IntegerField(primary_key=True, auto_created=True, verbose_name='用户ID')
    name = models.CharField(max_length=20, blank=True, null=True, verbose_name='用户名')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='手机号')
    has_realname = models.IntegerField(verbose_name='实名状态',
                                       choices=realname_status, default=0)

    @property
    def realname_state(self):
        return self.realname_status[self.has_realname][-1]

    def __str__(self):
        return self.name+'-'+self.phone

    class Meta:
        managed = True
        db_table = 't_appuser'
        verbose_name_plural = verbose_name = '会员管理'
