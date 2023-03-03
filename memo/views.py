from django.shortcuts import render
import datetime
# Create your views here.

def Memo(request):
    template_name = "memo.html"
    
    dt_now = datetime.datetime.now()
    print(dt_now)

    title = request.POST.get("TITLE")
    text = request.POST.get("TEXT")

    if text == None:
        title="入力してください"
        text="入力してください"
        text_count=0
    else:
        list = [char for char in text]
        count=0
        for i in range(len(list)):
            if list[i] == "　" or list[i]==" "or list[i] == "\r" or list[i] == "\n":
                count+=1
        text_count=len(text)-count



    return render(request, template_name, {"title":title, "text_count":text_count, "text":text, "dt_now":dt_now})
