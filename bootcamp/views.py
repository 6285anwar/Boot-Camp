from django.shortcuts import redirect

def app(request):
    return redirect('/app/')

def appadmin(request):
    return redirect('/appadmin/')

def appuser(request):
    return redirect('/appuser/')

