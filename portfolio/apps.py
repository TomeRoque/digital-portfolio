from django.apps import AppConfig



class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'


class CadeirasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cadeiras'
