from django.views import generic
from django.urls import reverse
from guests.models import Entry
from stats.models import SiteStats

class IndexView(generic.ListView):
    template_name = 'guests/index.html'

    def get_queryset(self):
        return Entry.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats, _ = SiteStats.objects.get_or_create(pk=1)
        stats.counter += 1
        stats.save()
        print(stats.counter)
        context['guest_number'] = stats.counter
        return context


class NewEntryView(generic.CreateView):
    model = Entry
    fields = ["author", "text"]
    template_name = 'guests/new.html'

    def get_success_url(self):
        return reverse('main')