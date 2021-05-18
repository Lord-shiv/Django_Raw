from django.shortcuts import render
from .models import Student, Player
from django.db.models import Q
from django.db import connection

# Create your views here.


def student_list_a(request):
    '''give all the data without hesitation'''
    st = Student.objects.all()
    print(st)
    print(st.query)

    return render(request, 'index.html', {'students': st})


def student_list_b(request):
    '''Good but Q has more popularity'''
    st = Student.objects.filter(username__startswith='user') | Student.objects.filter(
        username__startswith='shiv')

    print(st)
    print(st.query)

    return render(request, 'index.html', {'students': st})

################
# Simple OR
################


def student_list_c(request):
    '''we can perform multiple search queries using Q'''
    posts = Student.objects.filter(Q(username__startswith='user') | ~Q(
        username__startswith='sheet') | Q(username__endswith='a'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html', {'students': posts})

################
# Simple EXCLUDE
################


def student_list_d(request):
    ''' Don't think should be there use exclude '''
    # st = Student.objects.exclude(score=20) # score__gt = 20   # score__gte = 20
    # st = Student.objects.exclude(score=20) & Student.objects.exclude(
    #     username__startswith='Ro')
    st = Player.objects.filter(
        ~Q(age__gte=50) & ~Q(favorite__startswith='poco'))

    # gt    greater than
    # gte   greater than or equal to
    # lt    less than
    # lte   less than or equal to

    print(st)
    print(connection.queries)

    return render(request, 'index.html', {'students': st})

################
# Simple UNION
################


def student_list_e(request):
    '''
        Union queries removes duplicate
        values_list ==> return list
        values ==> return dict
    '''
    st = Student.objects.all().values('username').union(
        Player.objects.all().values('username'))

    print(st)
    print(connection.queries)

    return render(request, 'index.html', {'students': st})

################
# SELECT & OUTPUT INDIVIDUAL FIELDS
################


def student_list_f(request):
    st = Player.objects.filter(favorite='cricket').only('age')

    print(st)
    print(connection.queries)

    return render(request, 'index.html', {'students': st})


################
# Simple PERFORMING RAW QUERIES
################

def student_list_g(request):
    sql = "SELECT * FROM app_hello_student WHERE score > 20"
    st = Student.objects.raw(sql)[2:5]
    # st = Student.objects.raw(
    #     "SELECT * FROM app_hello_student WHERE score > 20")

    print(st)
    print(connection.queries)

    return render(request, 'index.html', {'students': st})

################
# Simple BYPASSING ORM
################


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def student_list(request):
    cursor = connection.cursor()
    # count(*) will return number of rows
    cursor.execute("SELECT * FROM app_hello_player where username='Rohit'")
    r = dictfetchall(cursor)  # cursor.fetchall()  # fetchone()
    print(r)
    return render(request, 'index.html', {'students': r})
