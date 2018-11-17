from django.db import models

# Emplacements et tarifs
class Emplacement(models.Model):
    emplacement_type = models.CharField(max_length=200, help_text='Saisir un type d\'emplacement')
    emplacement_price_a_day = models.CharField(max_length=10, help_text='Saisir le prix de l\'emplacement à la journée')
    emplacement_summary = models.CharField(max_length=2000, help_text='Saisir un résumé de l\'emplacement')

    def __str__(self):
        return self.emplacement_type


class Media(models.Model):
    titre = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(max_length=255, upload_to='media/upload/')

    def __str__(self):
        return self.titre

# Home onepage
class HomePage(models.Model):
    # header
    header_title1 = models.CharField(max_length=40, help_text='Le premier titre du header')
    header_title2 = models.CharField(max_length=30, help_text='Le deuxième titre du header')
    header_summary = models.CharField(max_length=2000, help_text='Le resumé du header (250 caractères conseillé)')
    header_button1 = models.CharField(max_length=20, help_text='Le texte du premier bouton dans le header (celui de gauche)', default='BOUTON 1')
    header_button2 = models.CharField(max_length=20, help_text='Le texte du deuxieme bouton dans le header (celui de droite)', default='BOUTON 2')

    # features1
    features1_1_title = models.CharField(max_length=40, help_text='Le titre de la feature 1 (bloc 1)')
    features1_1_text = models.CharField(max_length=40, help_text='Le texte de la feature 1 (bloc 1)')
    features1_2_title = models.CharField(max_length=40, help_text='Le titre de la feature 2 (bloc 1)')
    features1_2_text = models.CharField(max_length=40, help_text='Le texte de la feature 2 (bloc 1)')
    features1_3_title = models.CharField(max_length=40, help_text='Le titre de la feature 3 (bloc 1)')
    features1_3_text = models.CharField(max_length=40, help_text='Le texte de la feature 3 (bloc 1)')
    features1_4_title = models.CharField(max_length=40, help_text='Le titre de la feature 4 (bloc 1)')
    features1_4_text = models.CharField(max_length=40, help_text='Le texte de la feature 4 (bloc 1)')
    # features2
    features2_1_title = models.CharField(max_length=40, help_text='Le titre de la feature 1 (bloc 2)')
    features2_1_text = models.CharField(max_length=40, help_text='Le texte de la feature 1 (bloc 2)')
    features2_2_title = models.CharField(max_length=40, help_text='Le titre de la feature 2 (bloc 2)')
    features2_2_text = models.CharField(max_length=40, help_text='Le texte de la feature 2 (bloc 2)')
    features2_3_title = models.CharField(max_length=40, help_text='Le titre de la feature 3 (bloc 2)')
    features2_3_text = models.CharField(max_length=40, help_text='Le texte de la feature 3 (bloc 2)')
    features2_4_title = models.CharField(max_length=40, help_text='Le titre de la feature 4 (bloc 2)')
    features2_4_text = models.CharField(max_length=40, help_text='Le texte de la feature 4 (bloc 2)')
    features2_5_title = models.CharField(max_length=40, help_text='Le titre de la feature 4 (bloc 2)')
    features2_5_text = models.CharField(max_length=40, help_text='Le texte de la feature 4 (bloc 2)')
    # Citation
    citation_title = models.CharField(max_length=40, help_text='Le titre de la citation')
    citation_auteur = models.CharField(max_length=40, help_text='L\'auteur de la citation')
    # Contact
    contact_titre = models.CharField(max_length=40, help_text='Le titre du formulaire de contact')
    contact_texte = models.CharField(max_length=40, help_text='Le texte du formulaire de contact')
    adress = models.CharField(max_length=40, help_text='L\'adresse du formulaire de contact')
    email = models.CharField(max_length=40, help_text='L\'email du formulaire de contact')
    phone = models.CharField(max_length=40, help_text='Le numéro de téléphone du formulaire de contact')
    # email_receptrice = models.CharField(max_length=40, help_text='L\'adresse mail sur laquel vous resevrez les mails des visiteurs')

    def __str__(self):
        sep = " __sep_char__ "
        return (self.header_title1 + sep + self.header_title2 + sep + self.header_summary + sep + self.header_button1 + sep + self.header_button2 + sep +
                self.features1_1_title  + sep + self.features1_1_text  + sep + self.features1_2_title  + sep + self.features1_2_text  + sep +
                self.features1_3_title + sep + self.features1_3_text  + sep + self.features1_4_title  + sep + self.features1_4_text + sep +
                self.features2_1_title  + sep + self.features2_1_text + sep + self.features2_2_title  + sep + self.features2_2_text  + sep +
                self.features2_3_title + sep + self.features2_3_text  + sep + self.features2_4_title + sep + self.features2_4_text  + sep +
                self.features2_5_title  + sep + self.features2_5_text + sep +
                self.citation_title  + sep + self.citation_auteur + sep +
                self.contact_titre  + sep + self.contact_texte  + sep + self.adress + sep + self.email  + sep + self.phone)
