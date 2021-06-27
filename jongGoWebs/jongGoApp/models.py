from django.db import models

# Create your models here.
class ProductDetail(models.Model):
    product_idx = models.IntegerField(db_column='PRODUCT_IDX', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=30)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=30)  # Field name made lowercase.
    product_code = models.CharField(db_column='PRODUCT_CODE', max_length=30)  # Field name made lowercase.
    product_reg = models.DateField(db_column='PRODUCT_REG')  # Field name made lowercase.
    product_edit = models.DateField(db_column='PRODUCT_EDIT')  # Field name made lowercase.
    product_comment = models.CharField(db_column='PRODUCT_COMMENT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    product_price = models.IntegerField(db_column='PRODUCT_PRICE')  # Field name made lowercase.
    product_res = models.CharField(db_column='PRODUCT_RES', max_length=30, blank=True, null=True)  # Field name made lowercase.
    product_state = models.CharField(db_column='PRODUCT_STATE', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_detail'