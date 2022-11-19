from django.contrib.auth.decorators import login_required


# Create your views here.
def profile(request):
    """Display the user's profile"""
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)