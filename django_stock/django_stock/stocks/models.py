from django.db import models
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)        
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)       
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)       
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)        

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RegisteredStock(models.Model):
    stk = models.ForeignKey('StockInfo', models.DO_NOTHING)
    end_date = models.DateTimeField(blank=True, null=True)
    end_price = models.FloatField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)       
    created_by = models.DateTimeField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = False
        db_table = 'registered_stock'


class StockInfo(models.Model):
    stk_id = models.CharField(primary_key=True, max_length=50)     
    stk_name = models.CharField(max_length=50, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)   
    country = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True) 
    fax = models.CharField(max_length=30, blank=True, null=True)   
    website = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=30, blank=True, null=True)
    sector = models.CharField(max_length=30, blank=True, null=True)
    bs_summary = models.CharField(max_length=1000, blank=True, null=True)
    payoutratio = models.FloatField(db_column='payoutRatio', blank=True, null=True)  # Field name made lowercase.
    regularmarketvolume = models.IntegerField(db_column='regularMarketVolume', blank=True, null=True)  # Field name made lowercase.   
    averagevolume = models.IntegerField(db_column='averageVolume', blank=True, null=True)  # Field name made lowercase.
    marketcap = models.BigIntegerField(db_column='marketCap', blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(max_length=20, blank=True, null=True)
    enterprisevalue = models.BigIntegerField(db_column='enterpriseValue', blank=True, null=True)  # Field name made lowercase.        
    forwardpe = models.FloatField(db_column='forwardPE', blank=True, null=True)  # Field name made lowercase.
    profitmargins = models.FloatField(db_column='profitMargins', blank=True, null=True)  # Field name made lowercase.
    floatshares = models.BigIntegerField(db_column='floatShares', blank=True, null=True)  # Field name made lowercase.
    earningsquarterlygrowth = models.FloatField(db_column='earningsQuarterlyGrowth', blank=True, null=True)  # Field name made lowercase.
    pegratio = models.FloatField(db_column='pegRatio', blank=True, null=True)  # Field name made lowercase.
    enterprisetorevenue = models.FloatField(db_column='enterpriseToRevenue', blank=True, null=True)  # Field name made lowercase.     
    enterprisetoebitda = models.FloatField(db_column='enterpriseToEbitda', blank=True, null=True)  # Field name made lowercase.       
    symbol = models.CharField(max_length=30, blank=True, null=True)
    shortname = models.CharField(db_column='shortName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    longname = models.CharField(db_column='longName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    timezonefullname = models.CharField(db_column='timeZoneFullName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    timezoneshortname = models.CharField(db_column='timeZoneShortName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uuid = models.CharField(max_length=50, blank=True, null=True)  
    recommendationkey = models.CharField(db_column='recommendationKey', max_length=20, blank=True, null=True)  # Field name made lowercase.
    totalcash = models.BigIntegerField(db_column='totalCash', blank=True, null=True)  # Field name made lowercase.
    totalcashpershare = models.FloatField(db_column='totalCashPerShare', blank=True, null=True)  # Field name made lowercase.
    ebitda = models.BigIntegerField(blank=True, null=True)
    totaldebt = models.BigIntegerField(db_column='totalDebt', blank=True, null=True)  # Field name made lowercase.
    quickratio = models.FloatField(db_column='quickRatio', blank=True, null=True)  # Field name made lowercase.
    currentratio = models.FloatField(db_column='currentRatio', blank=True, null=True)  # Field name made lowercase.
    totalrevenue = models.BigIntegerField(db_column='totalRevenue', blank=True, null=True)  # Field name made lowercase.
    debttoequity = models.FloatField(db_column='debtToEquity', blank=True, null=True)  # Field name made lowercase.
    revenuepershare = models.FloatField(db_column='revenuePerShare', blank=True, null=True)  # Field name made lowercase.
    returnonassets = models.FloatField(db_column='returnOnAssets', blank=True, null=True)  # Field name made lowercase.
    returnonequity = models.FloatField(db_column='returnOnEquity', blank=True, null=True)  # Field name made lowercase.
    grossprofits = models.BigIntegerField(db_column='grossProfits', blank=True, null=True)  # Field name made lowercase.
    freecashflow = models.FloatField(db_column='freeCashflow', blank=True, null=True)  # Field name made lowercase.
    operatingcashflow = models.BigIntegerField(db_column='operatingCashflow', blank=True, null=True)  # Field name made lowercase.    
    earningsgrowth = models.FloatField(db_column='earningsGrowth', blank=True, null=True)  # Field name made lowercase.
    revenuegrowth = models.FloatField(db_column='revenueGrowth', blank=True, null=True)  # Field name made lowercase.
    grossmargins = models.FloatField(db_column='grossMargins', blank=True, null=True)  # Field name made lowercase.
    ebitdamargins = models.FloatField(db_column='ebitdaMargins', blank=True, null=True)  # Field name made lowercase.
    operatingmargins = models.FloatField(db_column='operatingMargins', blank=True, null=True)  # Field name made lowercase.
    financialcurrency = models.CharField(db_column='financialCurrency', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stock_info'


class StockReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    stk = models.ForeignKey(StockInfo, models.DO_NOTHING)
    report_date = models.DateTimeField(blank=True, null=True)      
    personal_comment = models.CharField(max_length=1000, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)       

    class Meta:
        managed = False
        db_table = 'stock_report'