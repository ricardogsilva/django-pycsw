from django.db import models


# TODO - we may not need all these fields
# investigate how the searching is done
# TODO - Add the remaining indexes
class Record(models.Model):
    """
    Most of the fileds are nullable in order to allow external
    manipulation of the database by PyCSW
    """

    identifier = models.CharField(
        max_length=255,
        db_index=True,
        help_text="Maps to pycsw:Identifier"
    )
    typename = models.CharField(
        max_length=100,
        default="gmd:MD_Metadata",
        db_index=True,
        help_text="Maps to pycsw:Typename"
    )
    schema = models.CharField(
        max_length=100,
        default="http://www.isotc211.org/2005/gmd",
        help_text="Maps to pycsw:Schema",
        db_index=True,
    )
    metadata_source = models.CharField(
        max_length=255,
        default="local",
        help_text='maps to pycsw:MdSource',
        db_index=True
    )
    insert_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Maps to pycsw:InsertDate'
    )
    xml = models.TextField(
        default='<gmd:MD_Metadata '
                'xmlns:gmd="http://www.isotc211.org/2005/gmd"/>',
        help_text=' Maps to pycsw:XML'
    )
    any_text = models.TextField(
        help_text='Maps to pycsw:AnyText'
    )
    # TODO - Could import pycountry and perform validation on the language
    # TODO - Perhaps including all languages in a checkbox is overkill...
    # code sample:
    # import pycountry
    # [(k, v.name) for k, v in pycountry.languages.indices[
    #     "iso639_3_code"].iteritems()]
    language = models.CharField(
        max_length=3,
        default='eng',
        blank=True,
        null=True,
        help_text="Maps to pycsw:Language"
    )
    title = models.CharField(
        max_length=255,
        null=True,
        help_text='Maps to pycsw:Title'
    )
    abstract = models.TextField(
        blank=True,
        null=True,
        help_text='Maps to pycsw:Abstract'
    )
    # TODO - Use django-taggit in conjunction with a custom field
    # in order to have a nicer representation but still save them as
    # a csv string
    keywords = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Maps to pycsw:Keywords'
    )
    keywords_types = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Maps to pycsw:Keywordstype'
    )
    format = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="Maps to pycsw:Format"
    )
    source = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Maps to pycsw:Source'
    )
    date = models.DateTimeField(
        null=True, blank=True,
        help_text='Maps to pycsw:Date, pycsw:Modified, pycsw:RevisionData, '
                  'pycsw:CreationDate and pycsw:PublicationDate'
    )
    type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Type'
    )
    bounding_box = models.TextField(
        null=True,
        blank=True,
        help_text='Maps to pycsw:BoundingBox'
    )
    crs = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:CRS'
    )
    alternate_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text='Maps to pycsw:AlternateTitle'
    )
    organization_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:OrganizationName'
    )
    security_constraints = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:SecurityConstraints'
    )
    parent_identifier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:ParentIdentifier'
    )
    topic_category = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:TopicCategory'
    )
    resource_language = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        help_text='Maps to pycsw:ResourceLanguage'
    )
    geographic_description_code = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Maps to pycsw:GeographicDescriptionCode'
    )
    denominator = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Denominator'
    )
    distance_value = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text='Maps to pycsw:DistanceValue'
    )
    distance_uom = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text='Maps to pycsw:DistanceUOM'
    )
    temporal_extent_begin = models.DateTimeField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:TempExtent_begin'
    )
    temporal_extent_end = models.DateTimeField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:TempExtent_end'
    )
    service_type = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Maps to pycsw:ServiceType'
    )
    service_type_version = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Maps to pycsw:ServiceTypeVersion'
    )
    operation = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Operation'
    )
    coupling_type = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Maps to pycsw:CouplingType'
    )
    operates_on = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:OperatesOn'
    )
    operates_on_identifier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:OperatesOnIdentifier'
    )
    operates_on_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:OperatesOnName'
    )
    degree = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Degree'
    )
    access_constraints = models.TextField(
        null=True,
        blank=True,
        help_text='Maps to pycsw:AccessConstraints'
    )
    other_constraints = models.TextField(
        null=True,
        blank=True,
        help_text='Maps to pycsw:OtherConstraints'
    )
    classification = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Classification'
    )
    condition_applying_to_access_and_use = models.TextField(
        null=True,
        blank=True,
        help_text='Maps to pycsw:ConditionApplyingToAccessAndUse'
    )
    lineage = models.TextField(
        null=True,
        blank=True,
        help_text='Maps to pycsw:Lineage'
    )
    responsible_party_role = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:ResponsiblePartyRole'
    )
    specification_title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:SpecificationTitle'
    )
    specification_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Maps to pycsw:SpecificationDate'
    )
    specification_date_type = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        help_text='Maps to pycsw:SpecificationDateType'
    )
    creator = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Creator'
    )
    publisher = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Publisher'
    )
    contributor = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Contributor'
    )
    relation = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Relation'
    )
    links = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='Maps to pycsw:Links'
    )

    def __str__(self):
        return self.identifier
