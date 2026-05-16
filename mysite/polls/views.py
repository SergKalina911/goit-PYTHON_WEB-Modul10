from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice

# from django.template import loader


# Для синтетичного цукру можна використовувати наступний код, який є більш простим і зрозумілим:
# from django.shortcuts import render

def index(request):
    """ View function for the index page of the polls app. It retrieves the latest 5 questions and
    renders them using the 'polls/index.html' template."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# def index(request):
#     """ View function for the index page of the polls app. It retrieves the latest 5 questions and
#     renders them using the 'polls/index.html' template."""
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def detail(request, question_id):
    """ View function for the detail page of a specific question. It retrieves the question object
    based on the provided question_id and renders it using the 'polls/detail.html' template. If the
    question with the given ID does not exist, a 404 error is raised. This function is responsible
    for displaying the details of a specific poll question, including the question text and its
    associated choices. It uses the get_object_or_404 shortcut to retrieve the question object,
    which simplifies error handling by automatically returning a 404 response if the question does
    not exist. The render function is then used to generate the HTML response based on the
    'polls/detail.html' template and the provided context, allowing for a clean separation of
    concerns between the view logic and the presentation layer. """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#     """ View function for the detail page of a specific question."""
#     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    """ View function for the results page of a specific question. It retrieves the question object
    and renders it using the 'polls/results.html' template. The question object is passed to the
    template context, allowing the template to display the question and its associated choices and
    vote counts. If the question with the given ID does not exist, a 404 error is raised. This
    function is responsible for displaying the results of a specific poll question, including the
    number of votes for each choice. It uses the get_object_or_404 shortcut to retrieve the
    question object, which simplifies error handling by automatically returning a 404 response if
    the question does not exist. The render function is then used to generate the HTML response
    based on the 'polls/results.html' template and the provided context. This allows for a clean
    separation of concerns, where the view handles the logic of retrieving data and rendering the
    template, while the template is responsible for presenting the data to the user.  """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# def results(request, question_id):
#     """ View function for the results page of a specific question."""
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

def vote(request, question_id):
    """ View function for handling the voting action for a specific question. It processes the POST
    data, updates the vote count for the selected choice, and redirects to the results page. If the
    user did not select a choice, it redisplays the voting form with an error message."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
