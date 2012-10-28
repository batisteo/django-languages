from django.db.models.fields import CharField

class LanguageField(CharField):
    """
    A language field for Django models.
    """
    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)
