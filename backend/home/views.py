from django.shortcuts import render
from forum.models import Topic
from devices.models import Device
from forms import TopicPostForm
from django.shortcuts import render, redirect
from django.views.generic import View


def home(request):
    topics = Topic.objects.filter(device=None).order_by('-date')[:5]
    popular_phones = Device.objects.filter(type=Device.PHONE).order_by('-views')[:5]
    popular_tablets = Device.objects.filter(type=Device.TABLET).order_by('-views')[:5]
    context = {
        "topics": topics,
        "popular_phones": popular_phones,
        "popular_tablets": popular_tablets,
    }
    return render(request, 'home/index.html', context)


class NewTopicFormView(View):
    form_class = TopicPostForm
    template_name = 'home/new_topic.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST)

        if user is not None:
            topic = form.save(commit=False)
            topic.author = user
            topic.body = request.POST['body']
            topic.hearts = 0
            topic.save()
            return redirect('/home')

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
