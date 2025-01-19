from django.shortcuts import render
from .models import About
from .forms import CollaborateForm

# Create your views here.

def about_me(request):
    """
    Renders the 'About' site page
    """

    if request.method == "POST":
        print("Receiving a POST request here!")
        collaborate_form = CollaboteForm(data=request.POST)
        if collaborate_form.is_valid():
            comment = comment_form.save(commit=False)
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )