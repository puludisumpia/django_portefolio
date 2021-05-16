from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact, Project, Technologie
from .forms import ContactForm

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            content = form.cleaned_data.get("content")

            # Sauvegarde dans la base de donnée
            new_contact = Contact(
                name=name,
                email=email,
                content=content
            )
            new_contact.save()

            # Envoi email de confirmation
            body = f"""
                    Bonjour {name},
                    Nous avons reçu votre message et nous mettons 
                    tout en oeuvre pour vous répondre dans les meilleurs.
                """
            send_mail(
                "Confirmation reception de votre message",
                body,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            # Flash messages bootstrap
            messages.success(
                request,
                "Votre message a été envoyé avec succès",
                "success"
            )
            return redirect("index")
        else:
            form = ContactForm()
    else:
        form = ContactForm()

    # Tous les projets et technologies
    projects = Project.objects.order_by("-date")
    technologies = Technologie.objects.all()
    ctx = {
        "projects": projects,
        "technologies": technologies,
        "form": form
    }
    return render(request, ("index.html"), ctx)

