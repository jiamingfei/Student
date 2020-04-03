from django.shortcuts import render,redirect
import pymysql

def tutor(request):
    db = pymysql.connect("localhost","root","123456","test")
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    cursor.execute("select id,rolename,username,password from tutor")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return render(request,'tutor.html',{'data':data})

def add_tutor(request):
    if request.method=="GET":
        return render(request, 'add_tutor.html')
    else:
        print(request.POST)
        v1 = request.POST.get('rolename')
        v2 = request.POST.get('username')
        v3 = request.POST.get('password')
    db = pymysql.connect("localhost","root","123456","test")
    cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
    cursor.execute("insert into tutor(rolename,username,password) VALUES(%s,%s,%s)",[v1,v2,v3])
    db.commit()
    cursor.close()
    db.close()
    return redirect('/tutor/')

def edit_tutor(request):
    if request.method == "GET":
        nid = request.GET.get("nid")
        db = pymysql.connect("localhost", "root", "123456", "test")
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select id,rolename,username,password from tutor where id=%s",nid)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return render(request,'edit_tutor.html',{"data":data})
    else:
        nid = request.GET.get("nid")
        rolename = request.POST.get("rolename")
        username = request.POST.get("username")
        password = request.POST.get("password")
        db = pymysql.connect("localhost","root","123456","test")
        cursor = db.cursor(cursor = pymysql.cursors.DictCursor)
        cursor.execute("update tutor set rolename=%s,username=%s,password=%s where id=%s",[rolename,username,password,nid])
        db.commit()
        cursor.close()
        db.close()
        return redirect('/tutor/')

def del_tutor(request):
    nid =request.GET.get("nid")
    db = pymysql.connect("localhost","root","123456","test")
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("delete from tutor where id =%s ",nid)
    db.commit()
    cursor.close()
    db.close()
    return redirect('/tutor/')