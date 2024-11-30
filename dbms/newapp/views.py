from django.shortcuts import redirect,render,get_object_or_404
from .models import Events,Department,Venue,Contests,Registration,Sponsers,Volunteers
from django.db import connection
from django.http import JsonResponse
from .forms import RegistrationForm
from .sponsers_register import SponsersForm
from .volunteers_register import VolunteersForm
from django.contrib import messages
def index(request):
    return render(request, "newapp/index.html", {})

def userreg(request):
    return render(request, "newapp/userreg.html", {})
# Create your views here.

def insertevent(request):
    veid = request.POST['teid'];
    vename = request.POST['tename'];
    vedate = request.POST['tedate'];
    veregistrationfee = request.POST['teregistrationfee'];
    veemail = request.POST['teemail'];
    vecontact = request.POST['tecontact'];
    vstart_date = request.POST['tstart_date'];
    vend_date = request.POST['tend_date'];
    vevent_coordinator = request.POST['tevent_coordinator'];
    vdept = request.POST['tdept '];
    vv = request.POST['tv '];
    us=Events(eid=veid, ename=vename, edate=vedate, eregistrationfee=veregistrationfee, eemail=veemail, econtact=vecontact, start_date=vstart_date, end_date=vend_date, event_coordinator=vevent_coordinator, dept=vdept, v=vv );
    us.save();
    return render(request, 'newapp/index.html', {})

'''def register_participant(request):
    vparticipant_id = request.POST['tparticipant_id'];
    vparticipant_name = request.POST['tparticipant_name'];
    vcollege = request.POST['tcollege'];
    vparticipant_age = request.POST['tparticipant_age'];
    vparticipant_gender = request.POST['tparticipant_gender'];
    vparticipant_dept = request.POST['tparticipant_dept'];
    vparticipant_contact = request.POST['tparticipant_contact'];
    vparticipant_email = request.POST['tparticipant_email'];
    vpayment_status = request.POST['tpayment_status'];
    vregistration_date = request.POST['tregistration_date'];
    vevent_id = request.POST['tevent_id'];'''

def viewusers(request):
    events = Events.objects.all()
    return render(request,"newapp/viewusers.html",{'userdata': events})

def viewdept(request):
    dept=Department.objects.all()
    return render(request,"newapp/viewdept.html",{'userdata': dept})

def deletedept(request, id):
    us=Department.objects.filter(dept_id=id)
    us.delete()
    return redirect("/viewdept")


def viewvenue(request):
    venue=Venue.objects.all()
    return render(request,"newapp/viewvenue.html",{'userdata': venue})
'''
def deletevenue(request, id):
    us=Venue.objects.filter(v_id=id)
    us.delete()
    return redirect("/viewvenue")
'''
def deleteprofile(request, id):
    us=Events.objects.filter(eid=id)
    us.delete()
    return redirect("/viewusers")

def editprofile(request, id):
    event=Events.objects.get(eid=id)
    return render(request,"newapp/editprofile.html", {'user':event})

def updateprofile(request, id):
    newuid=request.POST['eid']
    newuname=request.POST['ename']
    newstartdate=request.POST['start_date']
    newenddate=request.POST['end_date']
    newuemail=request.POST['eemail']
    newucontact=request.POST['econtact']
    newecoord=request.POST['event_coordinator']
    newdept=request.POST['dept']
    newvenue=request.POST['v']
    event=Events.objects.get(eid=id)
    event.eid=newuid
    event.ename=newuname
    event.start_date = newstartdate
    event.end_date = newenddate
    event.eemail=newuemail
    event.econtact=newucontact
    event.event_coordinator = newecoord
    event.dept = newdept
    event.v= newvenue
    event.save()
    return redirect("/viewusers")



def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_participants')
    return render(request, 'newapp/form.html', {'form': form})


def update_register(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    form = RegistrationForm(instance=registration)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('/view_participants')
    return render(request, 'newapp/form.html', {'form': form})


# AJAX
def load_contests(request):
    event_id = request.GET.get('event_id')
    contests = Contests.objects.filter(event_id=event_id)
    return render(request, 'newapp/contests_dropdown_list_options.html', {'contests': contests})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def view_participants(request):
    participants = Registration.objects.all()

    return render(request,"newapp/view_participants.html",{'userdata': participants})

def delete_participants(request, id):
    us=Registration.objects.filter(participant_id=id)
    us.delete()
    return redirect("/view_participants")

'''def edit_participant(request, id):
    participant=Registration.objects.get(participant_id=id)
    return render(request,"newapp/edit_participant.html", {'user':participant})'''

'''def update_participant(request, id):
    newparticipant_id = request.POST['participant_id']
    newparticipant_name = request.POST['participant_name']
    newcollege = request.POST['college']
    newparticipant_age = request.POST['participant_age']
    newparticipant_gender = request.POST['participant_gender']
    newdept_name = request.POST['dept_name']
    newparticipant_contact = request.POST['participant_contact']
    newparticipant_email = request.POST['participant_email']
    newpayment_status = request.POST['payment_status']
    newregistration_date = request.POST['registration_date']
    newevent = request.POST['event']
    newcontest = request.POST['contest']
    participant = Registration.objects.get(participant_id=id)
    participant.participant_id = newparticipant_id
    participant. participant_name = newparticipant_name
    participant.college = newcollege
    participant.participant_age = newparticipant_age
    participant.participant_gender = newparticipant_gender
    participant.dept_name =  newdept_name
    participant.participant_contact = newparticipant_contact
    participant.participant_email = newparticipant_email
    participant.payment_status = newpayment_status
    participant.registration_date = newregistration_date
    participant.event = newevent
    participant.contest = newcontest
    participant.save()
    return redirect("/view_participants")'''


def sponser_registration(request):
    if request.method == 'POST':
        form = SponsersForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the traffic violation to the database
            messages.success(request, "Sponser Information recorded successfully!")
            return redirect('sponser_registration')  # Redirect to avoid resubmission on page refresh
        else:
            messages.error(request, "There was an error in your submission. Please correct the errors below.")
    else:
        form = SponsersForm()  # Initialize an empty form for GET request

    return render(request, 'newapp/sponser_register.html', {'form': form})

def update_sponsers(request, pk):
    sponser = get_object_or_404(Sponsers, pk=pk)
    form = SponsersForm(instance=sponser)
    if request.method == 'POST':
        form = SponsersForm(request.POST, instance=sponser)
        if form.is_valid():
            form.save()
            return redirect('/view_sponsers')
    return render(request, 'newapp/sponser_register.html', {'form': form})

def view_sponsers(request):
    sponser = Sponsers.objects.all()

    return render(request,"newapp/view_sponsers.html",{'userdata': sponser})

def delete_sponsers(request, id):
    us=Sponsers.objects.filter(sponser_id=id)
    us.delete()
    return redirect("/view_sponsers")


def volunteer_registration(request):
    if request.method == 'POST':
        form = VolunteersForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the traffic violation to the database
            messages.success(request, "Volunteer Information recorded successfully!")
            return redirect('view_volunteers')  # Redirect to avoid resubmission on page refresh
        else:
            messages.error(request, "There was an error in your submission. Please correct the errors below.")
    else:
        form = VolunteersForm()  # Initialize an empty form for GET request

    return render(request, 'newapp/volunteer_register.html', {'form': form})

def update_volunteer(request, pk):
    volunteer = get_object_or_404(Volunteers, pk=pk)
    form = VolunteersForm(instance=volunteer)
    if request.method == 'POST':
        form = VolunteersForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            return redirect('/view_volunteers')
    return render(request, 'newapp/volunteer_register.html', {'form': form})

def view_volunteers(request):
    volunteer = Volunteers.objects.all()
    return render(request,"newapp/view_volunteers.html",{'userdata': volunteer})

def delete_volunteers(request, id):
    us=Volunteers.objects.filter(volunteer_id=id)
    us.delete()
    return redirect("/view_volunteers")


def contests_view(request):
    # Query to retrieve all contests with registration_fee greater than 100
    contests = Contests.objects.filter(registration_fee__gt=100).select_related('event', 'venue')

    # Formatting data for the template
    contest_data = [
        {
            'contest_name': contest.contest_name,
            'registration_fee': contest.registration_fee,
            'event': contest.event.event_name if contest.event else 'N/A',  # Assuming 'event_name' is a field in your Events model
        }
        for contest in contests
    ]

    return render(request, 'newapp/contests.html', {'contest_data': contest_data})