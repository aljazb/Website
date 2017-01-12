from django.shortcuts import render
from forum.models import Topic
from devices.models import Device
from forum.forms import TopicPostForm
from django.shortcuts import render, redirect
from django.views.generic import View

DEFAULT_TOPIC_COUNT = 5
EXPAND_COUNT = 5


def home(request, show_count=DEFAULT_TOPIC_COUNT):
    """Returns the home page

    The method filters phones and tablets by a number of views they have and shows the top 5
    The topics get shown based on their publish date. By default 5 are displayed, but that can be expended by clicking show more

    Keyword arguments:
    request -- HttpRequest object
    show_count -- the number of topics that are currently displayed
    """
    if show_count is None:
        show_count = DEFAULT_TOPIC_COUNT
    topics = Topic.objects.filter(device=None).order_by('-date')[:show_count]
    popular_phones = Device.objects.filter(type=Device.PHONE).order_by('-views')[:5]
    popular_tablets = Device.objects.filter(type=Device.TABLET).order_by('-views')[:5]
    context = {
        "topics": topics,
        "popular_phones": popular_phones,
        "popular_tablets": popular_tablets,
    }
    return render(request, 'home/index.html', context)


def show_more(request, show_count=DEFAULT_TOPIC_COUNT):
    """Generates the url that specifies how many topics should be displayed and redirects to that page

    Keyword arguments:
    request -- HttpRequest object
    show_count -- the number of topics that are currently displayed
    """
    if show_count is None:
        show_count = DEFAULT_TOPIC_COUNT
    return redirect('/home/' + str(int(show_count)+EXPAND_COUNT))


class NewTopicFormView(View):
    """Returns the rendered page that is used for writing new topics

    The method checks whether the request is GET (the user requested a page used to write a new topic) and POST (the user posted a new topic)
    The POST method checks if the user is logged in and in that case saves the topic to the database and redirects to that page
    """
    form_class = TopicPostForm
    template_name = 'forum/new_topic.html'

    def get(self, request):
        """Returns the rendered page that is used for writing new topics"""
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Checks if the user is logged in and in that case saves the topic to the database and redirects to that page"""
        user = request.user
        form = self.form_class(request.POST)

        if user is not None:
            topic = form.save(commit=False)
            topic.author = user
            topic.body = request.POST['body']
            topic.hearts = 0
            topic.save()
            return redirect('/forum/' + str(topic.id))

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
