from django.shortcuts import render
from .forms import SignUpForm,ContactForm,ScoreboardForm,AnswerForm
# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from .models import Scoreboard,Answer
from django.http import HttpResponseRedirect
def hackathon(request):
    obj = Scoreboard.objects.filter(username=request.user)
    ans_li = [0]
    for i in obj:
        ans_li.append(i.score)
    #print(max(ans_li))
    return render(request,'uiet/hackathon.html',{'name':request.user,'score':max(ans_li)})
def register(request):
    if request.method=="POST":
        request.session['score']=0
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            first_name=fm.cleaned_data['first_name']
            email=fm.cleaned_data['email']
            username=request.POST['username']
            answer=""
            obj=Answer(name=first_name,answer=answer)
            obj.save()
            messages.success(request,'You have successfully signed up . You can login now')
            reg = Scoreboard(name=first_name,username=username,answer=answer, score=request.session['score'])
            reg.save()
    else:
        fm=SignUpForm()
    return render(request,'uiet/register.html',{'form':fm})
def log_in(request):
    if not request.user.is_authenticated :
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            #if 'score' not  in request.session:
                #print("Chala")

            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)

                    #print("User",request.user)
                    a = Scoreboard.objects.filter(username=request.user)

                    #print("log_in", a[0].score)
                    ans_li = [0]
                    for i in a:
                        ans_li.append(i.score)
                    request.session['score']=max(ans_li)
                    return HttpResponseRedirect('/')

            else :
                messages.error(request,"Username and password do not match in our database.")
        else:
            fm=AuthenticationForm()

        return render(request,'uiet/login.html',{'form':fm})
    else :
        return HttpResponseRedirect('/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
def contact(request):
    if request.method=="POST":
        fm=ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"We will answer you shortly")
    else:
        fm=ContactForm()
    obj = Scoreboard.objects.filter(username=request.user)
    ans_li = [0]
    for i in obj:
        ans_li.append(i.score)
    return render(request,'uiet/contact.html',{'form':fm,'score':max(ans_li)})
def scoreboard(request):
    obj=Scoreboard.objects.filter(username=request.user)
    ans_li=[]
    for i in obj:
        ans_li.append(i.score)
    obj=Scoreboard.objects.all()
    ans_li=[]
    for i in obj:
        obj1=Scoreboard.objects.filter(username=i.name)
        min_li=[i.name]
        for k in obj1:
            if k.score not in min_li :
                min_li.append(k.score)
        ans_li.append(min_li)
    # print(ans_li)
    rohan=[]
    for i in ans_li:
        # print(i)
        if i not in rohan:
           rohan.append(i)
    # print(rohan)
    final_dict={}
    for i in rohan:
        # print(i)
        sub_li=[0]
        for j in range(1,len(i)) :
            sub_li.append(i[j])
        final_dict[i[0]]=max(sub_li)
    # print(final_dict)
    #for i in final_dict:
        #print(i,final_dict[i])
    obj = Scoreboard.objects.filter(username=request.user)
    ans_li = [0]
    for i in obj:
        ans_li.append(i.score)
    from collections import OrderedDict
    dd = OrderedDict(sorted(final_dict.items(),reverse=True, key=lambda x: x[1]))
    return render(request,'uiet/scoreboard.html',{'final_dict':dd,'score':max(ans_li)})
def crypto(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=ScoreboardForm(request.POST)
            name=request.user
            username=request.user.username
            answer=request.POST['answer']
            ans_obj=Answer.objects.filter(username=username)
            ans_obj=list(ans_obj)
            li=[]
            for i in ans_obj:
                #print(i.answer)
                li.append(i.answer)
            if answer not in li :
                reg=Answer(name=request.user,username=request.user.username,answer=answer)
                reg.save()
                ans_obj.append(answer)
                if answer=="Rohan-Flag-1":
                    request.session['score']+=20

                elif answer=="Rohan-Flag-2":
                    request.session['score']+=30

                elif answer=="Rohan-Flag-3":
                    request.session['score']+=50

            # print(request.session['li'])
            reg=Scoreboard(name=name,username=username,answer=answer,score=request.session['score'])
            reg.save()
            return HttpResponseRedirect('/crypto/')

        else:
            fm=ScoreboardForm()
        obj = Scoreboard.objects.filter(username=request.user)
        ans_li = [0]
        for i in obj:
            ans_li.append(i.score)
        return render(request,'uiet/crypto.html',{'form':fm,'score':max(ans_li)})
    else:
        messages.error(request,"You must login first")
        return HttpResponseRedirect('/login')
def networking(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=ScoreboardForm(request.POST)
            name=request.user
            username=request.user.username
            answer=request.POST['answer']
            ans_obj=Answer.objects.filter(username=username)
            ans_obj=list(ans_obj)
            li=[]
            for i in ans_obj:
                #print(i.answer)
                li.append(i.answer)
            if answer not in li :
                reg=Answer(name=request.user,username=request.user.username,answer=answer)
                reg.save()
                ans_obj.append(answer)
                if answer=="NRohan-Flag-1":
                    request.session['score']+=20

                elif answer=="NRohan-Flag-2":
                    request.session['score']+=30

                elif answer=="NRohan-Flag-3":
                    request.session['score']+=50

            # print(request.session['li'])
            reg=Scoreboard(name=name,username=username,answer=answer,score=request.session['score'])
            reg.save()
            return HttpResponseRedirect('/networking/')

        else:
            fm=ScoreboardForm()
        obj = Scoreboard.objects.filter(username=request.user)
        ans_li = [0]
        for i in obj:
            ans_li.append(i.score)
        return render(request,'uiet/networking.html',{'form':fm,'score':max(ans_li)})
    else:
        messages.error(request,"You must login first")
        return HttpResponseRedirect('/login')
def forensic(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=ScoreboardForm(request.POST)
            name=request.user
            username=request.user.username
            answer=request.POST['answer']
            ans_obj=Answer.objects.filter(username=username)
            ans_obj=list(ans_obj)
            li=[]
            for i in ans_obj:
                #print(i.answer)
                li.append(i.answer)
            if answer not in li :
                reg=Answer(name=request.user,username=request.user.username,answer=answer)
                reg.save()
                ans_obj.append(answer)
                if answer=="FRohan-Flag-1":
                    request.session['score']+=20

                elif answer=="FRohan-Flag-2":
                    request.session['score']+=30

                elif answer=="FRohan-Flag-3":
                    request.session['score']+=50

            # print(request.session['li'])
            reg=Scoreboard(name=name,username=username,answer=answer,score=request.session['score'])
            reg.save()
            return HttpResponseRedirect('/forensic/')

        else:
            fm=ScoreboardForm()
        obj = Scoreboard.objects.filter(username=request.user)
        ans_li = [0]
        for i in obj:
            ans_li.append(i.score)
        return render(request,'uiet/forensic.html',{'form':fm,'score':max(ans_li)})
    else:
        messages.error(request,"You must login first")
        return HttpResponseRedirect('/login')