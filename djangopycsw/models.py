from django.db import models

class Record(models.Model):
    identifier = models.CharField(
        max_length=255, help_text="Maps to pycsw:Identifier")
    typename = models.CharField(
        max_length=100, default="gmd:MD_Metadata",
        help_text="Maps to pycsw:Typename"
    )
    schema = models.CharField(
        max_length=100, default="http://www.isotc211.org/2005/gmd",
        help_text="Maps to pycsw:Schema"
    )
    metadata_source = models.CharField(max_length=255, default="local",
                                       help_text='maps to pycsw:MdSource')
    insert_date = models.DateTimeField(
        auto_now_add=True, help_text='Maps to pycsw:InsertDate')
    xml = models.TextField(
        default='<gmd:MD_Metadata '
                'xmlns:gmd="http://www.isotc211.org/2005/gmd"/>',
        help_text=' Maps to pycsw:XML'
    )
    any_text = models.TextField(help_text='Maps to pycsw:AnyText')
    #language = 'pycsw:Language': 'language',
    #title = models.CharField(max_length=255, help_text='Maps to pycsw:Title')
    #abstract = 'pycsw:Abstract': 'abstract',
    #keywords = 'pycsw:Keywords': 'keyword_csv',
    #keyword_type = 'pycsw:KeywordType': 'keywordstype',
    #format = 'pycsw:Format': 'spatial_representation_type_string',
    #source = 'pycsw:Source': 'source',
    #date = 'pycsw:Date': 'date',
    #modified = 'pycsw:Modified': 'date',
    #type = 'pycsw:Type': 'csw_type',
    #bounding_box = 'pycsw:BoundingBox': 'csw_wkt_geometry',
    #crs = 'pycsw:CRS': 'crs',
    #alternate_title = 'pycsw:AlternateTitle': 'title_alternate',
    #revision_date = 'pycsw:RevisionDate': 'date',
    #creation_date = 'pycsw:CreationDate': 'date',
    #publication_date = 'pycsw:PublicationDate': 'date',
    #organization_name = 'pycsw:OrganizationName': 'uuid',
    #security_constraints = 'pycsw:SecurityConstraints': 'securityconstraints',
    #parent_identifier = 'pycsw:ParentIdentifier': 'parentidentifier',
    #topic_category = 'pycsw:TopicCategory': 'topiccategory',
    #resource_language = 'pycsw:ResourceLanguage': 'resourcelanguage',
    #geographic_description_code = 'pycsw:GeographicDescriptionCode': 'geodescode',
    #denominator = 'pycsw:Denominator': 'denominator',
    #distance_value = 'pycsw:DistanceValue': 'distancevalue',
    #distance_uom = 'pycsw:DistanceUOM': 'distanceuom',
    #temporal_extent_begin = 'pycsw:TempExtent_begin': 'temporal_extent_start',
    #temporal_extent_end = 'pycsw:TempExtent_end': 'temporal_extent_end',
    #service_type = 'pycsw:ServiceType': 'servicetype',
    #service_type_version = 'pycsw:ServiceTypeVersion': 'servicetypeversion',
    #operation = 'pycsw:Operation': 'operation',
    #coupling_type = 'pycsw:CouplingType': 'couplingtype',
    #operates_on = 'pycsw:OperatesOn': 'operateson',
    #operates_on_identifier = 'pycsw:OperatesOnIdentifier': 'operatesonidentifier',
    #operates_on_name = 'pycsw:OperatesOnName': 'operatesoname',
    #degree = 'pycsw:Degree': 'degree',
    #access_constraints = 'pycsw:AccessConstraints': 'accessconstraints',
    #other_constraints = 'pycsw:OtherConstraints': 'otherconstraints',
    #classification = 'pycsw:Classification': 'classification',
    #condition_applying_to_access_and_use = 'pycsw:ConditionApplyingToAccessAndUse': 'conditionapplyingtoaccessanduse',
    #lineage = 'pycsw:Lineage': 'lineage',
    #responsible_party_role = 'pycsw:ResponsiblePartyRole': 'responsiblepartyrole',
    #specification_title = 'pycsw:SpecificationTitle': 'specificationtitle',
    #specification_date = 'pycsw:SpecificationDate': 'specificationdate',
    #specification_date_type = 'pycsw:SpecificationDateType': 'specificationdatetype',
    #creator = 'pycsw:Creator': 'creator',
    #publisher = 'pycsw:Publisher': 'publisher',
    #contributor = 'pycsw:Contributor': 'contributor',
    #relation = 'pycsw:Relation': 'relation',
    #links = 'pycsw:Links': 'download_links',

