# Create your views here.
from django.template import Context, loader
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from models import Question

def index(request):
    qns = Question.objects.filter(answered=False).order_by('-votes')
    t = loader.get_template('questions.html')
    c = Context({
            'qns': qns,
            'user' : request.user,
            'STATIC_URL' : "/site_media/static/",
            })
    c.update(csrf(request))
    return HttpResponse(t.render(c))

def submit(request):
    user = request.user
    c = {}
    c.update(csrf(request))
    qn = Question(question=request.POST['question'])
    qn.created_by = user
    qn.selected = False
    qn.answered = False
    qn.save()
    voteup(request, qn.id)
    return HttpResponseRedirect('/moderator')

def voteup(request, qn_id):
    user = request.user
    qn = Question.objects.get(id=qn_id)
    qn.upvote(user)
    return HttpResponseRedirect('/moderator')

def answer(request, qn_id):
    user = request.user
    qn = Question.objects.get(id=qn_id)
    qn.answered = True
    qn.save()
    return HttpResponseRedirect('/moderator')
  
def selected(request):
    qns = Question.objects.filter(answered=False).filter(selected=True).order_by('-votes')
    t = loader.get_template('selected.html')
    c = Context({
            'qns': qns,
            'user' : request.user,
            'STATIC_URL' : "/site_media/static/",
            })
    c.update(csrf(request))
    return HttpResponse(t.render(c))


