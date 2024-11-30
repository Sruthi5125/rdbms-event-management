from django.db import models
class Events(models.Model):
    eid = models.CharField(primary_key=True, max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.CharField(max_length=254)
    econtact = models.CharField(max_length=15)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    event_coordinator = models.CharField(max_length=20, blank=True, null=True)
    dept = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)
    v = models.ForeignKey('Venue', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


    def __str__(self):
        return self.ename

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

    def __str__(self):
        return self.dept_name


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

    def __str__(self):
        return self.v_name

class Volunteers(models.Model):
    volunteer_id = models.CharField(primary_key=True, max_length=10)
    volunteer_roll_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    volunteer_name = models.CharField(max_length=20, blank=True, null=True)
    volunteer_age = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    volunteer_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    volunteer_email = models.CharField(unique=True, max_length=20, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    eid = models.ForeignKey(Events, on_delete=models.CASCADE, db_column='eid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteers'

class Contests(models.Model):
    contest_id = models.CharField(primary_key=True, max_length=20)
    contest_name = models.CharField(max_length=50, blank=True, null=True)
    event = models.ForeignKey('Events',on_delete=models.CASCADE, related_name='contests', blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, blank=True, null=True, )
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contest_email = models.CharField(max_length=30, blank=True, null=True)
    coordinator = models.CharField(max_length=30, blank=True, null=True)
    coordinator_contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contests'

    def __str__(self):
        return self.contest_name

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
    registration_date = models.DateField()
    event = models.ForeignKey(Events,  models.DO_NOTHING,blank=True, null=True)
    contest = models.ForeignKey(Contests, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registration'

    def __str__(self):
        return self.participant_id


class Sponsers(models.Model):
    sponser_id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=0)
    sponser_name = models.CharField(max_length=15, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mode_of_transaction = models.CharField(max_length=30, blank=True, null=True)
    ratings = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    sponser_contactno = models.DecimalField(unique=True, max_digits=10, decimal_places=0, blank=True, null=True)
    event = models.ForeignKey(Events,  on_delete=models.CASCADE, db_column='eid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsers'


