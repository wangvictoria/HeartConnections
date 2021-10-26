from django.shortcuts import render
from .forms import ProfileForm
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView

# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {}
    return render(request, 'index.html', context)


class ProfileFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

class ProfileCreateView(CreateView):
    model = Profile
    form = ProfileForm
    form.save()

class ProfileUpdateView(UpdateView):
    model = Profile
    form = ProfileForm
    form.save()

class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-delete')