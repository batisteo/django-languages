from django.db.models.fields import CharField

class LanguageField(CharField):
    """
    A language field for Django models.
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 3)
        super(CharField, self).__init__(*args, **kwargs)
