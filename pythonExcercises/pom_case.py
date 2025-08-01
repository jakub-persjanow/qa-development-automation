# Page Object Model
# Reprezentacja programistyczna widoków aplikacji
# Aplikacja ma login screen -> Framework ma login screen POM
# Apliakcja ma form -> Framework ma form POM

# Business Object Model
# Reprezentacja programistyczna struktur aplikacji
# Aplikacja ma w bazie danych tabelę users -> Framework ma obiekt users BOM
# Aplikacja ma formualrz -> framework ma obiekt fomularz oraz obiekt odpowiedzi jako form BOM i form_answer BOM -> form jest klasą rodzic, a form_answer jest klasą dziedziczoną (dzieckiem)

# class Form:
#     def __init__(self) -> None:
#         self.input = ""
#         # tu wszystkie informacje dot. formularza
        
#         self.answers = []
#         """ list[class: FormAnswer]"""

# class FormAnswer(Form):
#     def __init__(self) -> None:
#         super().__init__()


# class User:
#     def __init__(self) -> None:
#         self.name = ""
#         self.lname = ""
#         # tu wszystkie kolumny tabeli z bazy


class GoogleForm:
    def __init__(self, header_text, name_header_text, email_header_text) -> None:
        self.header = f'//*[@role="heading" and contains(text(), "{header_text}")]'
        # inputs
        self.name = self.create_input_xpath(name_header_text)
        self.email = self.create_input_xpath(email_header_text)
        self.checkbox = None
        
        # answers
        self.answers = []
        """ list[class: GoogleFormAnswer]"""

    def create_input_xpath(self, input_header_text):
        return f'//*[@role="heading"]//*[contains(text(), "{input_header_text}")]//following::input[1]'

    def fill_out_form(self, name_input, email_input):
        answer = GoogleFormAnswers(name=name_input, email=email_input)
        self.answers.append(answer)

class GoogleFormAnswers:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

if __name__ == "__main__":
    gf1 = GoogleForm(header_text="Test Form", 
                        name_header_text="Name", 
                        email_header_text="Email")

    gf1.fill_out_form("jakub", "jakub@test.com")
    gf1.fill_out_form("demian", "demian@test.com")

    for answer in gf1.answers:
        print(answer.name + " " + answer.email)