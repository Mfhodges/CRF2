from course.models import School
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from configparser import ConfigParser


config = ConfigParser()
config.read('config/config.ini')


opendata_crf_school_mappings= {'DM':"DM",'ED':"GSE",'EG':"SEAS",'VM':"VET",'AN':"AN",'FA':"FA",'AS':"SAS",'WH':"WH",'MD':"PSOM",'PV':"PC",'SW':"SP2",'LW':"LW","NU":"NURS"}

school_data = [
{"abbreviation":"AN", "name": "Annenberg School For Communication", "visibility": True,"opendata_abbr":"AN","canvas_subaccount":99243},
{"abbreviation":"SAS", "name": "Arts & Sciences", "visibility": True,"opendata_abbr":"AS","canvas_subaccount":99237},
{"abbreviation": "DM", "name":"Dental Medicine", "visibility": True,"opendata_abbr":"DM","canvas_subaccount":99241},
{"abbreviation": "GSE", "name":"Graduate School Of Education", "visibility": False,"opendata_abbr":"ED","canvas_subaccount":82192},
{"abbreviation": "SEAS", "name":"Engineering", "visibility": True,"opendata_abbr":"EG","canvas_subaccount":99238},
{"abbreviation": "FA", "name":"Design", "visibility": True,"opendata_abbr":"FA","canvas_subaccount":99244},
{"abbreviation": "LW", "name":"Law", "visibility": True,"opendata_abbr":"LW"},
{"abbreviation": "PSOM", "name":"Perelman School Of Medicine", "visibility": True,"opendata_abbr":"MD","canvas_subaccount":99242},
{"abbreviation": "NURS", "name":"Nursing", "visibility": True,"opendata_abbr":"NU","canvas_subaccount":99239},
{"abbreviation": "PC", "name":"Provost Center", "visibility": True,"opendata_abbr":"PV"},
{"abbreviation": "SS", "name":"Summer Sessions", "visibility": True,"opendata_abbr":"SS"},
{"abbreviation": "SP2", "name":"Social Policy & Practice", "visibility": True,"opendata_abbr":"SW","canvas_subaccount":99240},
{"abbreviation": "VET", "name":"Veterinary Medicine", "visibility": True,"opendata_abbr":"VT","canvas_subaccount":132153},
{"abbreviation": "WH", "name":"Wharton", "visibility": True,"opendata_abbr":"WH","canvas_subaccount":81471}
]



class Command(BaseCommand):
    help = 'add schools (see file for data)'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('-p', '--prefix', type=str, help='Define a username prefix')
        #parser.add_argument('-a', '--admin', action='store_true', help='Create an admin account')
        parser.add_argument('-q', '--quick', action='store_true', help='Quick add local store of schools')

    def handle(self, *args, **kwargs):
        #courseware = kwargs['courseware']

        """
        FROM MODELS
        name = models.CharField(max_length=50,unique=True)
        abbreviation = models.CharField(max_length=10,unique=True,primary_key=True)
        visible = models.BooleanField(default=True)
        opendata_abbr = models.CharField(max_length=2)
        canvas_subaccount = models.IntegerField(null=True)
        """
        for school in school_data:
            if School.objects.filter(abbreviation=school['abbreviation']).exists()==False:
                if school.get("canvas_subaccount"):
                    print(school)
                    School.objects.create(name=school['name'],abbreviation=school["abbreviation"],visible=school["visibility"],opendata_abbr=school["opendata_abbr"],canvas_subaccount=school["canvas_subaccount"])
                else:
                    School.objects.create(name=school['name'],abbreviation=school["abbreviation"],visible=school["visibility"],opendata_abbr=school["opendata_abbr"])
            else:
                print("SCHool already exists: "+ school["name"])
