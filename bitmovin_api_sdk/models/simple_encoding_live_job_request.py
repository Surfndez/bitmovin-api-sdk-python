# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.simple_encoding_live_cloud_region import SimpleEncodingLiveCloudRegion
from bitmovin_api_sdk.models.simple_encoding_live_job_input import SimpleEncodingLiveJobInput
import pprint
import six


class SimpleEncodingLiveJobRequest(object):
    @poscheck_model
    def __init__(self,
                 input_=None,
                 outputs=None,
                 cloud_region=None,
                 name=None):
        # type: (SimpleEncodingLiveJobInput, list[SimpleEncodingLiveJobUrlOutput], SimpleEncodingLiveCloudRegion, string_types) -> None

        self._input = None
        self._outputs = list()
        self._cloud_region = None
        self._name = None
        self.discriminator = None

        if input_ is not None:
            self.input = input_
        if outputs is not None:
            self.outputs = outputs
        if cloud_region is not None:
            self.cloud_region = cloud_region
        if name is not None:
            self.name = name

    @property
    def openapi_types(self):
        types = {
            'input': 'SimpleEncodingLiveJobInput',
            'outputs': 'list[SimpleEncodingLiveJobUrlOutput]',
            'cloud_region': 'SimpleEncodingLiveCloudRegion',
            'name': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'input': 'input',
            'outputs': 'outputs',
            'cloud_region': 'cloudRegion',
            'name': 'name'
        }
        return attributes

    @property
    def input(self):
        # type: () -> SimpleEncodingLiveJobInput
        """Gets the input of this SimpleEncodingLiveJobRequest.


        :return: The input of this SimpleEncodingLiveJobRequest.
        :rtype: SimpleEncodingLiveJobInput
        """
        return self._input

    @input.setter
    def input(self, input_):
        # type: (SimpleEncodingLiveJobInput) -> None
        """Sets the input of this SimpleEncodingLiveJobRequest.


        :param input_: The input of this SimpleEncodingLiveJobRequest.
        :type: SimpleEncodingLiveJobInput
        """

        if input_ is not None:
            if not isinstance(input_, SimpleEncodingLiveJobInput):
                raise TypeError("Invalid type for `input`, type has to be `SimpleEncodingLiveJobInput`")

        self._input = input_

    @property
    def outputs(self):
        # type: () -> list[SimpleEncodingLiveJobUrlOutput]
        """Gets the outputs of this SimpleEncodingLiveJobRequest.

        output of the live encoding job (required)

        :return: The outputs of this SimpleEncodingLiveJobRequest.
        :rtype: list[SimpleEncodingLiveJobUrlOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this SimpleEncodingLiveJobRequest.

        output of the live encoding job (required)

        :param outputs: The outputs of this SimpleEncodingLiveJobRequest.
        :type: list[SimpleEncodingLiveJobUrlOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[SimpleEncodingLiveJobUrlOutput]`")

        self._outputs = outputs

    @property
    def cloud_region(self):
        # type: () -> SimpleEncodingLiveCloudRegion
        """Gets the cloud_region of this SimpleEncodingLiveJobRequest.

        The cloud region that will be used for the live encoding. This value has to be set.

        :return: The cloud_region of this SimpleEncodingLiveJobRequest.
        :rtype: SimpleEncodingLiveCloudRegion
        """
        return self._cloud_region

    @cloud_region.setter
    def cloud_region(self, cloud_region):
        # type: (SimpleEncodingLiveCloudRegion) -> None
        """Sets the cloud_region of this SimpleEncodingLiveJobRequest.

        The cloud region that will be used for the live encoding. This value has to be set.

        :param cloud_region: The cloud_region of this SimpleEncodingLiveJobRequest.
        :type: SimpleEncodingLiveCloudRegion
        """

        if cloud_region is not None:
            if not isinstance(cloud_region, SimpleEncodingLiveCloudRegion):
                raise TypeError("Invalid type for `cloud_region`, type has to be `SimpleEncodingLiveCloudRegion`")

        self._cloud_region = cloud_region

    @property
    def name(self):
        # type: () -> string_types
        """Gets the name of this SimpleEncodingLiveJobRequest.

        This property will be used for naming the encoding.

        :return: The name of this SimpleEncodingLiveJobRequest.
        :rtype: string_types
        """
        return self._name

    @name.setter
    def name(self, name):
        # type: (string_types) -> None
        """Sets the name of this SimpleEncodingLiveJobRequest.

        This property will be used for naming the encoding.

        :param name: The name of this SimpleEncodingLiveJobRequest.
        :type: string_types
        """

        if name is not None:
            if not isinstance(name, string_types):
                raise TypeError("Invalid type for `name`, type has to be `string_types`")

        self._name = name

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
        if not isinstance(other, SimpleEncodingLiveJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
