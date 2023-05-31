from django.shortcuts import render, redirect
from .forms import EmailModelForm
from .models import EmailList
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
# Create your views here.
@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='signin')
def create_group(request):
    all_entry = EmailList.objects.filter(sender = request.user)
    if request.method == 'POST':
        form = EmailModelForm(request.POST)
        if form.is_valid():
            sender = request.user
            name = request.POST.get('name')
            email = request.POST.get('email')
            s = EmailList(sender=sender, name=name, email=email)
            s.save()
        return redirect('create_group')
    else:
        form = EmailModelForm()
    context = {
        'form' : form,
        'all_entry' : all_entry
    }
    return render(request, 'creategroup.html',context)

@login_required(login_url='signin')
def editEmailList(request, pk):
    email_obj = EmailList.objects.get(id = pk)
    editform = EmailModelForm(instance=email_obj)
    if request.method == 'POST':
        editform = EmailModelForm(request.POST, instance=email_obj)
        if editform.is_valid():
            editform.save()
            return redirect('email_list_page')
    context = {
        'editform' : editform
    }
    return render(request, 'editEmailList.html', context)

@login_required(login_url='signin')
def deleteEmailList(request, pk):
    delete_obj = EmailList.objects.get(id = pk)
    
    if request.method == 'POST':
        delete_obj.delete()
        return redirect('email_list_page')
    context = {
        'delete_obj' : delete_obj
    }    
    return render(request, 'deleteEmailList.html', context)




@login_required(login_url='signin')
def email_list_page(request):
    all_entry = EmailList.objects.filter(sender = request.user)
    return render(request, 'emaillist.html', {'all_entry' : all_entry})



@login_required(login_url='signin')
def emaildashboard(request):
    all_entry = EmailList.objects.filter(sender = request.user)
    if request.method == 'POST':
        email = request.POST.getlist('email')
        subject = request.POST.get('subject')
        email_body = request.POST.get('email_body')
        attachment = request.FILES['attachment']
        mail_sending = EmailMultiAlternatives(
            subject,
            email_body,
            'bikaspandey92@gmail.com',
            (email)
        )
        mail_sending.attach(attachment.name, attachment.read(), attachment.content_type)
        mail_sending.send()
        return redirect('mailsent')
    context = {
        'all_entry' : all_entry
    }
    return render(request, 'emaildashboard.html',context)

@login_required(login_url='signin')
def mailsent(request):
    
    return render(request, 'thankyou.html')