from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.db.models import Q
from .models import Course
from .forms import inputScoreForm, addCourseForm
from .scoringAlgo import calculateScores


courseInfo = [
                {
                    'name': "Tollygunge Club",
                    'city': 'Kolkata',
                    'country': 'India',
                    'par': [4, 3, 4, 4, 4, 3, 5, 3, 4, 5, 3, 4, 5, 4, 4, 4, 4, 3],
                    'strokeIndex': [7, 17, 3, 11, 1, 13, 9, 15, 5, 14, 16, 10, 4, 12, 6, 2, 8, 18]
                },

                {
                    'name': "Royal Calcutta Golf Club",
                    'city': 'Kolkata',
                    'country': 'India',
                    'par': [4, 3, 4, 5, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 5, 4, 4, 4],
                    'strokeIndex': [11, 17, 3, 13, 9, 5, 1, 15, 7, 2, 8, 14, 16, 4, 12, 18, 10, 6]
                }
            ]


def home(request):
    context = {
        #'courseInfo': courseInfo
        'courseInfo': Course.objects.all()
    }
    #print(context)
    return render(request, 'courses/home.html', context)


def about(request):
    return render(request, 'courses/about.html')


def search(request):

    query = request.GET.get('q')
    if query:
        results = Course.objects.filter(Q(name__icontains=query) | Q(country__icontains=query) | Q(city__icontains=query))
    else:
        results = []
    context = {
        # 'courseInfo': courseInfo
        'courseInfo': results
    }

    return render(request, 'courses/search.html', context)


def calculate(request):

    scoring = {}

    if request.method == 'POST':
        #print("POST")
        form = inputScoreForm(request.POST)
        #print(form.is_valid())
        #print(form)
        if form.is_valid():
            course = form.cleaned_data['courseChoice']
            handicap = form.cleaned_data['handicap']
            score = form.cleaned_data['score']

            courseInfo = course
            playerInfo = {'score': score, 'handicap': handicap}

            #print(type(courseInfo.strokeIndex[1]))

            scoring = calculateScores(courseInfo, playerInfo)

            #print(scoring)

            #print("Valid")

    #query = request.GET.get('q')
    form = inputScoreForm()

    #if query:
        #results = Course.objects.filter(
            #Q(name__icontains=query) | Q(country__icontains=query) | Q(city__icontains=query))
    #else:
        #results = []

    context = {
        # 'courseInfo': courseInfo
        #'courseInfo': results,
        'form': form,
        'scoring': scoring
    }
    return render(request, 'courses/calculate.html', context)


def addCourse(request):
    if request.method == 'POST':
        form = addCourseForm(request.POST)
        if form.is_valid():
            form.save()
            #print("Valid")

    form = addCourseForm()

    context = {
        'form': form
    }
    return render(request, 'courses/addCourse.html', context)

'''
class CourseDetailView(DetailView):
    model = Course


class CourseCreateView(CreateView):
    model = Course
    fields = ['name', 'city', 'country', 'strokeIndex', 'par']

    def get_object(self):
        return get_object_or_404(User, pk=request.session['user_id'])
'''