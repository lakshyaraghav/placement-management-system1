from django.db.models.aggregates import Count
from tstudentapp.models import Student, User
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse, response,JsonResponse
from django.db.models import Q
from django.template.loader import get_template
from django.http import FileResponse
from xhtml2pdf import pisa

from math import ceil


# Create your views here.
def is_valid_queryparam(param):
    return param !='' and param is not None

def index(request):

    #topper slider
    student_topper=Student.objects.filter(student_tenth__gte=50)
    n=len(student_topper)
    nslides = n//5 + ceil((n/5)-(n//5))
    #topper slider end



    #form
    student_all=Student.objects.all()
    id_query=request.GET.get('id')
    uname_query=request.GET.get('uname')
    skills_query=request.GET.get('skills')
    branch_query=request.GET.get('branch')
    tenth_min_query=request.GET.get('tenth_count_min')
    twelth_min_query=request.GET.get('twelth_count_min')
    diploma_min_query=request.GET.get('diploma_count_min')
    btech_min_query=request.GET.get('btech_count_min')
    achievement_query=request.GET.get('achievement')
    # print(tenth_min_query)
    
    if is_valid_queryparam(id_query) :
        student_all=student_all.filter(id=id_query)

    if is_valid_queryparam(uname_query) :
        student_all=student_all.filter(student_name__icontains=uname_query)

    if is_valid_queryparam(skills_query) and skills_query !='choose skills..':
        student_all=student_all.filter(technical_skills__icontains=skills_query)

    if is_valid_queryparam(tenth_min_query):
        student_all=student_all.filter(student_tenth__gte=tenth_min_query)

    if is_valid_queryparam(twelth_min_query):
        student_all=student_all.filter(student_twelth__gte=twelth_min_query)

    if is_valid_queryparam(diploma_min_query):
        student_all=student_all.filter(student_diploma__gte=diploma_min_query)
    
    if is_valid_queryparam(btech_min_query):
        student_all=student_all.filter(student_btech__gte=btech_min_query)

    if is_valid_queryparam(branch_query) and branch_query !='choose..':
        student_all=student_all.filter(student_branch__icontains=branch_query)

    if is_valid_queryparam(achievement_query) and achievement_query !='choose..':
        student_all=student_all.filter(student_achievement__icontains=achievement_query)
    
    # if is_valid_queryparam(tenth_min_query):
        # student_all=student_all.filter(student_tenth__gte=tenth_min_query)

    # if is_valid_queryparam(tenth_max_query):
    #     student_all=student_all.filter(student_tenth__lt=tenth_max_query)

    #form-ends
    def get_ip(request):
        address=request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip=address.split(',')[-1].strip()
        else:
            ip=request.META.get('REMOTE_ADDR')
        return ip

    ip=get_ip(request)
    u=User(user=ip)
    result=User.objects.filter(Q(user__icontains=ip))
    if len(result)==1:
        print("user exist")
    elif len(result)>1:
        print("user exists more")
    else:
        u.save()
        print("user is unique")
    count=User.objects.all().count()
    print("total user is ",count)

    data={}
    data['count']=count
    data['student_topper']=student_topper
    data['range']=range(nslides)
    data['student_all']=student_all

    return render(request,'tstudentapp/index.html',data)


def profileView(request,myid):
    student=Student.objects.filter(id=myid)
    
    return render(request,'tstudentapp/profileView.html',{'student':student[0]})

def search_event(request):

    if request.method =="POST" :
        searched=request.POST['searched']
        name= Student.objects.filter(student_name__icontains=searched)
        id_s=Student.objects.filter(id__icontains=searched)
        data={}
        data['searched']=searched
        data['name']=name
        data['id_s']=id_s
        return render(request,'tstudentapp/search_event.html',data)

    else:
        return render(request,'tstudentapp/search_event.html',{})

def profileViewList(request,myid):
    student=Student.objects.filter(id=myid)
    template_path = 'tstudentapp/profileViewList.html'
    context = {'student':student[0]}
    
    template = get_template(template_path)
    html = template.render(context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="student_report.pdf"'



    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def search_results(request):
    if request:
        res=None
        student=request.POST.get('student')
        # print(student)
        qs= Student.objects.filter(student_name__icontains=student)
        id_q=Student.objects.filter(id__icontains=student)
        # print(qs)
        if len(qs)>0 and len(student)>0:
            data=[]
            for pos in qs:
                item={
                    'id':pos.id,
                    'name':pos.student_name,
                    'image': str(pos.student_img.url)
                }
                data.append(item)
            res=data

        elif len(id_q)>0 and len(student)>0:
            data=[]
            for pos in id_q:
                item={
                    'id':pos.id,
                    'name':pos.student_name,
                    'image': str(pos.student_img.url)
                }
                data.append(item)
            res=data
        else:
            res='no suggestions...'

        return JsonResponse({'data':res})
    return JsonResponse({})