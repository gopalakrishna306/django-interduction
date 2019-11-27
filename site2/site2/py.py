from django.http import HttpResponse

def index(reqest):
    return  HttpResponse("hai iam gopalakrishna ")

def contact(reqest):
    return  HttpResponse("9652320676 ")

def mail(reqest):
    return  HttpResponse("gopalakrishna306@gmail.com ")

def address(reqest):
    return  HttpResponse("hydereabd")