from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.



monthly_challenges_text ={
    "january" : "eat no meat for the entire month",
    "february": "walk for at least 20 minitues a day",
    "march": "this is march",
    "april": "this is april",
    "may": "tsis is may",
    "june": "thsi is june",
    "july": "thsi is july",
    "august": "this is august",
    "september": "this is september",
    "october" : "this is october",
    "november": "this is november",
    "december": None
}

def index(request):
    #list_items = ""
    months = list(monthly_challenges_text.keys())

    return render(request,"challenges/index.html",{
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args =[month])
    #     list_items  += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenges(request,month):
    try:
        challenges_text = monthly_challenges_text[month]
        return render(request, "challenges/challenge.html",
                      {"text" : challenges_text,
                        "month" : month})
        #responce_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(responce_data)
    except:
        raise Http404()
        # response_date = render_to_string("404.html")
        # return HttpResponseNotFound(response_date)

# def january(request):
#     return HttpResponse("eat no meat for the entire month")

# def february(request):
#     return HttpResponse("walk for at least 20 minitues a day ")

# def march(request):
#     return HttpResponse("walk for at least 20 minitues a day ")


def monthly_challenge_number(request, month):

    list_of_month = list(monthly_challenges_text.keys())
    if month > len(list_of_month):
        return HttpResponseNotFound(" you are entered month is invalid")
    redirect_month = list_of_month[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

# def monthly_challenges_old(request,month):

#     text = None
#     if month == "january":
#         text = "eat no meat for the entire month"
#     elif month == "february":
#         text = "walk for at least 20 minitues a day"
#     elif month == "march":
#         text = "this is march"
#     elif month == "april":
#         text = "this is april"
#     elif month == "may":
#         text = "its my birthday month"
#     else:
#         return HttpResponseNotFound("this month not found")
#     return HttpResponse(text)

