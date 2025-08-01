from Form import Form

def get_form_object(header_text, name_header_text, email_header_text):
    form_object = Form(header_text=header_text, name_header_text=name_header_text, email_header_text=email_header_text)
    return form_object