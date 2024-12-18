# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contests(models.Model):
    contest_id = models.CharField(primary_key=True, max_length=20)
    contest_name = models.CharField(max_length=50, blank=True, null=True)
    event = models.ForeignKey('Events', models.DO_NOTHING, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey('Venue', models.DO_NOTHING, blank=True, null=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contest_email = models.CharField(max_length=30, blank=True, null=True)
    coordinator = models.CharField(max_length=30, blank=True, null=True)
    coordinator_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contests'


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    hod = models.CharField(max_length=30, blank=True, null=True)
    director = models.CharField(max_length=30, blank=True, null=True)
    dept_email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    dept_website = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Events(models.Model):
    eid = models.CharField(primary_key=True, max_length=20)
    ename = models.CharField(max_length=100)
    edate = models.DateTimeField()
    eregistrationfee = models.CharField(max_length=100)
    eemail = models.CharField(max_length=254)
    econtact = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'events'


class Registration(models.Model):
    participant_id = models.AutoField(primary_key=True)
    participant_name = models.CharField(max_length=30, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    participant_age = models.IntegerField(blank=True, null=True)
    participant_gender = models.CharField(max_length=1, blank=True, null=True)
    dept_name = models.CharField(max_length=40, blank=True, null=True)
    participant_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    participant_email = models.CharField(unique=True, max_length=20, blank=True, null=True)
    payment_status = models.CharField(max_length=20, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    contest = models.ForeignKey(Contests, models.DO_NOTHING, blank=True, null=True)
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration'


class Sponsers(models.Model):
    sponser_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    sponser_name = models.CharField(max_length=15, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mode_of_transaction = models.CharField(max_length=30, blank=True, null=True)
    ratings = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    sponser_contactno = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    eid = models.ForeignKey(Events, models.DO_NOTHING, db_column='eid', blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsers'


class Venue(models.Model):
    v_id = models.IntegerField(primary_key=True)
    v_name = models.CharField(unique=True, max_length=30, blank=True, null=True)
    v_block = models.CharField(max_length=20, blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    v_email = models.CharField(max_length=20, blank=True, null=True)
    v_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue'


'''class Volunteers(models.Model):
    volunteer_id = models.CharField(primary_key=True, max_length=10)
    volunteer_roll_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    volunteer_name = models.CharField(max_length=20, blank=True, null=True)
    volunteer_age = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    volunteer_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    volunteer_email = models.CharField(unique=True, max_length=20, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    eid = models.ForeignKey(Events, models.DO_NOTHING, db_column='eid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteers'
        '''
class Volunteers(models.Model):
    volunteer_id = models.CharField(primary_key=True, max_length=10)
    volunteer_roll_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    volunteer_name = models.CharField(max_length=20, blank=True, null=True)
    volunteer_age = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    volunteer_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    volunteer_email = models.CharField(unique=True, max_length=20, blank=True, null=True)
    dept_id = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    eid = models.ForeignKey(Events, models.DO_NOTHING, db_column='eid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteers'

