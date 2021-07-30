from django.shortcuts import render, HttpResponse

def order(request, order_id):
    return HttpResponse(f"pass the order ID and get the formatted JSON with the required information {order_id}")

def orders(request):
    return HttpResponse("pass multiple order IDs in string format, separated by comma (,) and return the info of those orders.")

def dates(request):
    return HttpResponse("pass two dates and return the ids of the orders between those dates")

def shipping(request):
    return HttpResponse("return all orders with the given key (city, state, country) and string as value.")

def search(request):
    return HttpResponse("search for the term given in multiple parts of the order, and return the results")
