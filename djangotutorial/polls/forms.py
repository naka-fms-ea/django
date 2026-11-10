from django import forms


# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)
#
#
# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)


class QuestionAddForm(forms.Form):
    question_text = forms.CharField(label='Question text')
    choice_0 = forms.CharField(label='choice #1')
    choice_1 = forms.CharField(label='choice #2', required=False)
    choice_2 = forms.CharField(label='choice #3', required=False)
    choice_3 = forms.CharField(label='choice #4', required=False)
    choice_4 = forms.CharField(label='choice #5', required=False)


#class ChoixForm(forms.Form):
#    CHOIX = [
#        ("choix1", "Première possibilité"),
#        ("choix2", "Deuxième possibilité"),
#        ("choix3", "Troisième possibilité"),
#        ("choix4", "Quatrième possibilité"),
#        ("choix5", "Cinquième possibilité"),
#    ]

#   choix_utilisateur = forms.ChoiceField(
#       label="Veuillez sélectionner une réponse :",
#       choices=CHOIX,
#       widget=forms.RadioSelect,
#        required=True
#    )