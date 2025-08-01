from FormAnswer import FormAnswer

class Form:
    def __init__(self, header_text, name_header_text, email_header_text) -> None:
        self.header = f'//*[@role="heading" and contains(text(), "{header_text}")]'
        # inputs
        self.name = self.create_input_xpath(name_header_text)
        self.email = self.create_input_xpath(email_header_text)
        self.checkbox = None
        
        # answers
        self.answers = []
        """ list[class: FormAnswer]"""

    def create_input_xpath(self, input_header_text):
        return f'//*[@role="heading"]//*[contains(text(), "{input_header_text}")]//following::input[1]'

    def fill_out_form(self, name_input, email_input):
        answer = FormAnswer(name=name_input, email=email_input)
        self.answers.append(answer)