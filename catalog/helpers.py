from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit
from crispy_forms.bootstrap import FormActions, Div

book_helper = FormHelper()
book_helper.form_tag = True
book_helper.method = 'POST'
book_helper.form_class = 'form-horizontal'
book_helper.form_show_labels = True
book_helper.label_class = 'col-md-2'
book_helper.field_class = 'col-md-10'

book_helper.layout = Layout(
    Div(
        Field('title', css_class='form-control', placeholder='TITLE'),
        Field('author', css_class='form-control', placeholder='AUTHOR'),
        css_class='col-md-6'
    ),
    Div(
        Field('isbn', css_class='form-control', placeholder='ISBN'),
        Field('genre', css_class='form-control'),
        css_class='col-md-6'
    ),
    Div(
        Field('summary', css_class='form-control', placeholder='SUMMARY'),
        css_class='col-md-12'
    ),
    FormActions(
        Submit('save', 'Submit', css_class='btn-success', style="float:right;"), ),
)
