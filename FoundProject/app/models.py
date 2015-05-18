from django.db import models
from pyswip import Prolog

# Create your models here.


def to_list(results):
    software_list = []
    for result in results:
        software = Software()
        for attr in result.keys():
            setattr(software, attr, result[attr])
            software_list.append(software)


class Software(models.Model):
    ID = models.CharField(max_length=50, primary_key=True)
    Name = models.CharField(max_length=255, null=True, blank=True)
    Category = models.CharField(max_length=255, null=True, blank=True)
    Language = models.CharField(max_length=50, null=True, blank=True)
    License = models.CharField(max_length=50, null=True, blank=True)
    Platform = models.CharField(max_length=50, null=True, blank=True)
    Size = models.CharField(max_length=255, null=True, blank=True)
    Initial_Date = models.CharField(max_length=50, null=True, blank=True)
    Final_Date = models.CharField(max_length=50, null=True, blank=True)
    Value = models.CharField(max_length=50, null=True, blank=True)
    prolog = Prolog()

    @classmethod
    def populate_database(cls):
        cls.prolog.consult('base.pro')
        results = cls.prolog.query("software(ID,Name,Category,Language,License,\
                                Platform,Size,Initial_Date,Final_Date,Value )")
        for result in results:
            software = cls()
            for attr in result.keys():
                setattr(software, attr, result[attr])
                software.save()

    @classmethod
    def refresh_asserts(cls):
        cls.prolog.query("retract(software(_,_,_,_,_,_,_,_,_,_)),fail")
        softwares = cls.objects.all()
        for software in softwares:
            cls.prolog.assertz(
                u"software('" + unicode(software.ID) + u"','"
                + unicode(software.Name) + u"','"
                + unicode(software.Category) + u"','"
                + unicode(software.Language) + u"','"
                + unicode(software.License) + u"','"
                + unicode(software.Platform) + u"','"
                + unicode(software.Size) + u"','"
                + unicode(software.Initial_Date) + u"','"
                + unicode(software.Final_Date) + u"','"
                + unicode(software.Value) + u"')")

    @classmethod
    def all(cls):
        software_list = []
        results = cls.prolog.query("software(ID,Name,Category,Language,License,\
                                Platform,Size,Initial_Date,Final_Date,Value )")
        for result in results:
            software = cls()
            for attr in result.keys():
                setattr(software, attr, result[attr])
            software_list.append(software)

        return software_list

    @classmethod
    def filter(cls, software_id='ID', name='Name', category='Category',
               language='Language', license='License', platform='Platform',
               size='Size', initial_date='Initial_Date', value='Value',
               final_date='Final_Date'):

        # if name == '':
        #     name = 'Name'
        # if category == '':
        #     category = 'Category'
        # if language == '':
        #     language = 'Language'
        # if license == '':
        #     license = 'License'
        # if platform == '':
        #     platform = 'Platform'
        # if size == '':
        #     size = 'Size'
        # if initial_date == '':
        #     initial_date = 'Initial_Date'
        # if value == '':
        #     value = 'Value'
        # if final_date == '':
        #     final_date = 'Final_Date'

        software_list = []
        results = cls.prolog.query(
            u"software(" + unicode(software_id) + u","
            + unicode(name) + u","
            + unicode(category) + u","
            + unicode(language) + u","
            + unicode(license) + u","
            + unicode(platform) + u","
            + unicode(size) + u","
            + unicode(initial_date) + u","
            + unicode(final_date) + u","
            + unicode(value) + u")")
        for result in results:
            software = cls()
            for attr in result.keys():
                setattr(software, attr, result[attr])
            software_list.append(software)

        return software_list

    def __unicode__(self):
        return "%s - %s" % (self.ID, self.Name)
