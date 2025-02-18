# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.analytics_license_custom_data_field_labels import AnalyticsLicenseCustomDataFieldLabels
import pprint
import six


class AnalyticsVirtualLicense(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 timezone=None,
                 licenses=None,
                 custom_data_fields_count=None,
                 custom_data_field_labels=None):
        # type: (string_types, string_types, string_types, list[AnalyticsVirtualLicenseLicensesListItem], int, AnalyticsLicenseCustomDataFieldLabels) -> None

        self._id = None
        self._name = None
        self._timezone = None
        self._licenses = list()
        self._custom_data_fields_count = None
        self._custom_data_field_labels = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if name is not None:
            self.name = name
        if timezone is not None:
            self.timezone = timezone
        if licenses is not None:
            self.licenses = licenses
        if custom_data_fields_count is not None:
            self.custom_data_fields_count = custom_data_fields_count
        if custom_data_field_labels is not None:
            self.custom_data_field_labels = custom_data_field_labels

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'name': 'string_types',
            'timezone': 'string_types',
            'licenses': 'list[AnalyticsVirtualLicenseLicensesListItem]',
            'custom_data_fields_count': 'int',
            'custom_data_field_labels': 'AnalyticsLicenseCustomDataFieldLabels'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'name': 'name',
            'timezone': 'timezone',
            'licenses': 'licenses',
            'custom_data_fields_count': 'customDataFieldsCount',
            'custom_data_field_labels': 'customDataFieldLabels'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this AnalyticsVirtualLicense.

        Analytics Virtual License Key/Id

        :return: The id of this AnalyticsVirtualLicense.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this AnalyticsVirtualLicense.

        Analytics Virtual License Key/Id

        :param id_: The id of this AnalyticsVirtualLicense.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this AnalyticsVirtualLicense.

        Name of the Analytics Virtual License

        :return: The name of this AnalyticsVirtualLicense.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this AnalyticsVirtualLicense.

        Name of the Analytics Virtual License

        :param name: The name of this AnalyticsVirtualLicense.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

    @property
    def timezone(self):
        # type: () -> string_types
        """Gets the timezone of this AnalyticsVirtualLicense.

        The timezone of the Analytics Virtual License

        :return: The timezone of this AnalyticsVirtualLicense.
        :rtype: string_types
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        # type: (string_types) -> None
        """Sets the timezone of this AnalyticsVirtualLicense.

        The timezone of the Analytics Virtual License

        :param timezone: The timezone of this AnalyticsVirtualLicense.
        :type: string_types
        """

        if timezone is not None:
            if not isinstance(timezone, string_types):
                raise TypeError("Invalid type for `timezone`, type has to be `string_types`")

        self._timezone = timezone

    @property
    def licenses(self):
        # type: () -> list[AnalyticsVirtualLicenseLicensesListItem]
        """Gets the licenses of this AnalyticsVirtualLicense.

        List of Analytics Licenses

        :return: The licenses of this AnalyticsVirtualLicense.
        :rtype: list[AnalyticsVirtualLicenseLicensesListItem]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        # type: (list) -> None
        """Sets the licenses of this AnalyticsVirtualLicense.

        List of Analytics Licenses

        :param licenses: The licenses of this AnalyticsVirtualLicense.
        :type: list[AnalyticsVirtualLicenseLicensesListItem]
        """

        if licenses is not None:
            if not isinstance(licenses, list):
                raise TypeError("Invalid type for `licenses`, type has to be `list[AnalyticsVirtualLicenseLicensesListItem]`")

        self._licenses = licenses

    @property
    def custom_data_fields_count(self):
        # type: () -> int
        """Gets the custom_data_fields_count of this AnalyticsVirtualLicense.

        The number of customData fields available

        :return: The custom_data_fields_count of this AnalyticsVirtualLicense.
        :rtype: int
        """
        return self._custom_data_fields_count

    @custom_data_fields_count.setter
    def custom_data_fields_count(self, custom_data_fields_count):
        # type: (int) -> None
        """Sets the custom_data_fields_count of this AnalyticsVirtualLicense.

        The number of customData fields available

        :param custom_data_fields_count: The custom_data_fields_count of this AnalyticsVirtualLicense.
        :type: int
        """

        if custom_data_fields_count is not None:
            if not isinstance(custom_data_fields_count, int):
                raise TypeError("Invalid type for `custom_data_fields_count`, type has to be `int`")

        self._custom_data_fields_count = custom_data_fields_count

    @property
    def custom_data_field_labels(self):
        # type: () -> AnalyticsLicenseCustomDataFieldLabels
        """Gets the custom_data_field_labels of this AnalyticsVirtualLicense.

        Labels for Custom Data fields

        :return: The custom_data_field_labels of this AnalyticsVirtualLicense.
        :rtype: AnalyticsLicenseCustomDataFieldLabels
        """
        return self._custom_data_field_labels

    @custom_data_field_labels.setter
    def custom_data_field_labels(self, custom_data_field_labels):
        # type: (AnalyticsLicenseCustomDataFieldLabels) -> None
        """Sets the custom_data_field_labels of this AnalyticsVirtualLicense.

        Labels for Custom Data fields

        :param custom_data_field_labels: The custom_data_field_labels of this AnalyticsVirtualLicense.
        :type: AnalyticsLicenseCustomDataFieldLabels
        """

        if custom_data_field_labels is not None:
            if not isinstance(custom_data_field_labels, AnalyticsLicenseCustomDataFieldLabels):
                raise TypeError("Invalid type for `custom_data_field_labels`, type has to be `AnalyticsLicenseCustomDataFieldLabels`")

        self._custom_data_field_labels = custom_data_field_labels

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalyticsVirtualLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
