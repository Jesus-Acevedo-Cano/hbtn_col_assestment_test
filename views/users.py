from django.shortcuts import render, HttpResponse

def all_users(request):
    return HttpResponse("list all users basic info")

def user_id(request):
    return HttpResponse(" list the user info from the given user id")

def user_orders(request):
    return HttpResponse("return orders from that specific user")
