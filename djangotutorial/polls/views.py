from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
#from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
#from .forms import NameForm
#from .forms import ChoixForm
from django.core.mail import send_mail
from django.utils import timezone

from .models import Choice, Question

from .forms import QuestionAddForm


NB_MAX_CHOIX = 5


# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    output = ", ".join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    template = loader.get_template("polls/index.html")
#    context = {"latest_question_list": latest_question_list}
#    return HttpResponse(template.render(context, request))

#def index(request):
#    latest_question_list = Question.objects.order_by("-pub_date")[:5]
#    context = {"latest_question_list": latest_question_list}
#    return render(request, "polls/index.html", context)

#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, "polls/detail.html", {"question": question})

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/detail.html", {"question": question})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, "polls/results.html", {"question": question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class AllView(generic.ListView):
    template_name = "polls/all.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")


class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, "name.html", {"form": form})


# fusion et modification des méthodes add et confirm_add # en la seule méthode add
def add(request):
    if request.method == 'POST':
        form = QuestionAddForm(request.POST)
        if form.is_valid():
            question = \
                Question(question_text= form.cleaned_data['question_text'], pub_date=timezone.now())
            question.save()
            # on traite à présent les champs de choix remplis
            # (on s'arrête au premier vide)
            for no_choix in range(NB_MAX_CHOIX):
                nom_champ = 'choice_{}'.format(no_choix)
                choice_text = form.cleaned_data[nom_champ].strip()
                if choice_text:
                    choice = Choice(question=question, choice_text=choice_text)
                    choice.save()
                else:
                    break
            return render(request, 'polls/confirm_add.html')
    else:
        form = QuestionAddForm()
    return render(request, 'polls/add.html', {'form': form})


#def formulaire_choix(request):
#    if request.method == "POST":

#        form = ChoixForm(request.POST)

#       if form.is_valid():
#            choix = form.cleaned_data["choix_utilisateur"]

            # Traitement du choix sélectionné
#           print("Choix sélectionné :", choix)

#            return render(
#                request,
#                "resultat.html",
#                {"choix": choix}
#            )

#    else:
#       form = ChoixForm()

#    return render(
#        request,
#        "formulaire.html",
#        {"form": form}
#    )

#if form.is_valid():
#    subject = form.cleaned_data["subject"]
#    message = form.cleaned_data["message"]
#    sender = form.cleaned_data["sender"]
#    cc_myself = form.cleaned_data["cc_myself"]
#
#    recipients = ["info@example.com"]
#    if cc_myself:
#        recipients.append(sender)
#
#    send_mail(subject, message, sender, recipients)
#    return HttpResponseRedirect("/thanks/")