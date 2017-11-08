"""Settings for pycsw."""

from django.conf import settings
from django.contrib.sites.models import Site
from django.urls import reverse


_DEFAULT_PYCSW_SETTINGS = {
    "server": {
        "home": settings.BASE_DIR,
        "url": "http://{}{}".format(
            Site.objects.get_current().domain,
            reverse("catalogue:endpoint")
        ),
        "mimetype": "application/xml; charset=UTF-8",
        "encoding": "UTF-8",
        "language": "en-US",
        "maxrecords": "50",
        "loglevel": "DEBUG",  # set this through django logging config
        "logfile": "",
        "ogc_schemas_base": "",
        "federatedcatalogues": "",
        "pretty_print": "",
        "gzip_compresslevel": "",
        "domainquerytype": "",
        "domaincounts": "",
        "spatial_ranking": "",
    },
    "manager": {
        "transactions": "",
        "allowed_ips": "",
        "csw_harvest_pagesize": "",
    },
    "metadata:main": {
        "identification_title": "",
        "identification_abstract": "",
        "identification_keywords": "",
        "identification_keywords_type": "",
        "identification_fees": "",
        "identification_accessconstraints": "",
        "provider_name": "",
        "provider_url": "",
        "contact_name": "",
        "contact_position": "",
        "contact_address": "",
        "contact_city": "",
        "contact_stateorprovince": "",
        "contact_postalcode": "",
        "contact_country": "",
        "contact_phone": "",
        "contact_fax": "",
        "contact_email": "",
        "contact_url": "",
        "contact_hours": "",
        "contact_instructions": "",
        "contact_role": "pointOfContact",
    },
    "repository": {
        "database": "",
        "mappings": "",
        "table": "",
        "filter": "",
    },
    "metadata:inspire": {
        "enabled": "",
        "languages_supported": "",
        "default_language": "",
        "date": "",
        "gemet_keywords": "",
        "conformity_service": "",
        "contact_name": "",
        "contact_email": "",
        "temp_extent": "",
    },
}


def get_pycsw_settings():
    pycsw_settings = {}
    for section in _DEFAULT_PYCSW_SETTINGS.keys():
        pycsw_settings[section] = {}
        for key, default_value in _DEFAULT_PYCSW_SETTINGS[section].items():
            try:
                configured_value = settings.PYCSW_SETTINGS[section][key]
            except KeyError:
                configured_value = default_value
            pycsw_settings[section][key] = configured_value
