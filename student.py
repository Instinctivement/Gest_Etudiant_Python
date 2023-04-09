import re
from dateutil.parser import parse

class Student:
  def __init__(self, infos, semestre1=0.0, semestre2=0.0, general=0.0):
        self.firstName = infos["firstName"]
        self.secondName = infos["secondName"]
        self.birthday = infos["birthday"]
        self.academicYear = infos["academicYear"]
        self.level = infos["level"]
        self.comment = infos["comment"]
        self.semestre1 = semestre1
        self.semestre2 = semestre2
        self.general = general

  def verify_length(self):
      """Vérifier que les champs firstName, secondName et comment ne dépassent pas une certaine longueur"""
      MAX_NAME_LENGTH = 50
      MAX_COMMENT_LENGTH = 500

      if len(self.firstName) < 2 or len(self.firstName) > MAX_NAME_LENGTH or not re.match("^[a-zA-Z0-9]*$", self.firstName):
          raise ValueError(f"Le champ 'firstName' doit faire moins de {MAX_NAME_LENGTH} caractères et ne peut contenir que des lettres et des chiffres")
      if len(self.secondName) < 2 or len(self.secondName) > MAX_NAME_LENGTH or not re.match("^[a-zA-Z0-9]*$", self.firstName):
          raise ValueError(f"Le champ 'secondName' doit faire moins de {MAX_NAME_LENGTH} caractères et ne peut contenir que des lettres et des chiffres")
      if len(self.comment) > MAX_COMMENT_LENGTH:
          raise ValueError(f"Le champ 'comment' doit faire moins de {MAX_COMMENT_LENGTH} caractères")

  def verify_date_format(self):
      """Vérifier que la date de naissance est au bon format"""
      date = parse(self.birthday)
      if date.year > 2005:
        raise ValueError(f"La date de naissance ne peut pas être après 2005.")
      if not re.match(r'^\d{4}-\d{4}$', self.academicYear):
        raise ValueError(f"Le format de l'année scolaire est incorrect. Entrez la date au format AAAA-AAAA.")
        
        
  def verify_integrity(self):
      """Vérifier l'intégrité des données de l'étudiant"""
      self.verify_length()
      self.verify_date_format()
      
  def show_student(self):
    print(f"\t\tPrenom           : {self.firstName}")
    print(f"\t\tNom              : {self.secondName}")
    print(f"\t\tbirthday         : {self.birthday}")
    print(f"\t\tAnnée academique : {self.academicYear}")
    print(f"\t\tNiveau           : {self.level}")
    print(f"\t\tcomment          : {self.comment}")
    print(f"\t\tSemestre 2       : {self.semestre1}")
    print(f"\t\tSemestre 1       : {self.semestre2}")
    print(f"\t\tGeneral          : {self.general}")
    print("\n\n")
    
  def parse_attribut_to_array(self):
    data = (self.firstName, self.secondName, self.birthday, self.academicYear, self.level, self.comment, self.semestre1, self.semestre2, self.general)
    return data
