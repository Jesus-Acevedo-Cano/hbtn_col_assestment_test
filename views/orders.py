from django.shortcuts import render, HttpResponse

def order(request, orderid):
    return HttpResponse(f"get the formatted JSON with the required information {orderid}")

def orders(request):
    return HttpResponse("pass multiple order IDs and return the info of those orders.")

def dates(request):
    return HttpResponse("pass two dates and return the ids of the orders between those dates")

def shipping(request):
    return HttpResponse("return all orders with the given key and string as value.")

def search(request):
    return HttpResponse("search for the term given, and return the results")
