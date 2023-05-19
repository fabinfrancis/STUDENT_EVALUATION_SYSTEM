# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from student_management_app.models import CustomUser,tutor as Tutor,StudentResult,Students
from student_management_app.EmailBackEnd import EmailBackEnd


def tutor_dash(request):
    return render(request, 'tutordash.html')


def home(request):
    return render(request, 'index.html')



def home_only(request):
    return render(request, 'home.html')


def loginPage(request):
    return render(request, 'login.html')



def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            elif user_type == '4':
                # return HttpResponse("Student Login")
                return redirect('tutor_dash')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def view_tutor(request):
    tutor = Tutor.objects.filter(user_id=request.user.id)
    for i in tutor:
        print(i.student_id.id)

    return render(request, 'tutor_view.html', {
    "tutor": tutor
    })


def view_mark(request,id):
    cr = Students.objects.get(admin=id)
    var=StudentResult.objects.filter(student_id_id=cr.id)
    if var:
        return render(request, 'tutor_view_mark.html', {
            "var": var
        })
    else:
        return render(request, 'tutor_view_mark.html')

def profile_tutor(request):
    tutor = CustomUser.objects.get(id=request.user.id)
    print(tutor)
    if tutor:
        return render(request, 'tutor_view_profile.html', {
            "tutor": tutor
        })
    else:
        return render(request, 'tutor_view_profile.html')

