"""
Models for configuration of settings relevant
to instructor tasks.
"""
from config_models.models import ConfigurationModel
from django.db.models import IntegerField


class GradeReportsBatchSizeSetting(ConfigurationModel):
    """
    TBD
    """
    batch_size = IntegerField(default=100)
