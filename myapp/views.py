from django.http import HttpResponse

def data(request):
    return HttpResponse(f"<h1>Это страница Data, ваш метод запроса: {request.method}</h1>")

def test(request):
    return HttpResponse(f"<h1>Это страница Test, ваш метод запроса: {request.method}</h1>")
