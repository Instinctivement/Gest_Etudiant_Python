import re
from dateutil.parser import parse


def char_lenght_error(char, lim):
    if len(char) > lim:
        print("ERREUR: Ce champ ne peut pas dépasser {} caractères".format(lim))
        return False
    else:
        return True
    
def char_nospecial_error(char):
    if not re.match("^[a-zA-Z0-9]*$", char):
        print("ERREUR: Ce champ ne peut contenir que des lettres et des chiffres")
        return False
    else:
        return True
    
def birthday_format_error(birthday):
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', birthday):
        print("ERREUR: Le format de la date de naissance est incorrect. Entrez la date au format JJ/MM/AAAA.")
        return False
    else:
        return True
    
def birthday_limit_error(birthday):
    try:
        date = parse(birthday)
        if date.year > 2005:
            print("ERREUR: La date de naissance ne peut pas être après 2005.")
            return False
        else:
            return True
    except ValueError:
        print("La date de naissance est invalide.")
        
def academicYear_format_error(academicYear):
    if not re.match(r'^\d{4}-\d{4}$', academicYear):
        print("ERREUR: Le format de l'année scolaire est incorrect. Entrez la date au format AAAA-AAAA.")
        return False
    else:
        return True