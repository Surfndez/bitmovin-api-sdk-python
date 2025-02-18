# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six


class TextMuxing(Muxing):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 streams=None,
                 outputs=None,
                 avg_bitrate=None,
                 min_bitrate=None,
                 max_bitrate=None,
                 ignored_by=None,
                 stream_conditions_mode=None,
                 filename=None,
                 start_offset=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, string_types, int) -> None
        super(TextMuxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._filename = None
        self._start_offset = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if start_offset is not None:
            self.start_offset = start_offset

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(TextMuxing, self), 'openapi_types'):
            types = getattr(super(TextMuxing, self), 'openapi_types')

        types.update({
            'filename': 'string_types',
            'start_offset': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(TextMuxing, self), 'attribute_map'):
            attributes = getattr(super(TextMuxing, self), 'attribute_map')

        attributes.update({
            'filename': 'filename',
            'start_offset': 'startOffset'
        })
        return attributes

    @property
    def filename(self):
        # type: () -> string_types
        """Gets the filename of this TextMuxing.

        The output file name (required)

        :return: The filename of this TextMuxing.
        :rtype: string_types
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        # type: (string_types) -> None
        """Sets the filename of this TextMuxing.

        The output file name (required)

        :param filename: The filename of this TextMuxing.
        :type: string_types
        """

        if filename is not None:
            if not isinstance(filename, string_types):
                raise TypeError("Invalid type for `filename`, type has to be `string_types`")

        self._filename = filename

    @property
    def start_offset(self):
        # type: () -> int
        """Gets the start_offset of this TextMuxing.

        Offset of MPEG-TS timestamps in seconds. This only affects streams with [WebVttConfiguration](#/Encoding/PostEncodingConfigurationsSubtitlesWebVtt). If set, the X-TIMESTAMP-MAP will be added as described in the [HLS specification](https://datatracker.ietf.org/doc/html/rfc8216#section-3.5). For example, if set to 10 seconds, *X-TIMESTAMP-MAP=MPEGTS:900000,LOCAL:00:00:00.000* will be added after each *WEBVTT* header. The default for TextMuxing is that the X-TIMESTAMP-MAP will not be written. Important to note is that the default for `startOffset` for [TsMuxings](#/Encoding/PostEncodingEncodingsMuxingsTsByEncodingId) and [ProgressiveTsMuxings](#/Encoding/PostEncodingEncodingsMuxingsProgressiveTsByEncodingId) is 10 seconds. If the output of this muxing is used for HLS together with video/audio streams using TsMuxings and ProgressiveTsMuxings, this value should be set to the same `startOffset`.

        :return: The start_offset of this TextMuxing.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        # type: (int) -> None
        """Sets the start_offset of this TextMuxing.

        Offset of MPEG-TS timestamps in seconds. This only affects streams with [WebVttConfiguration](#/Encoding/PostEncodingConfigurationsSubtitlesWebVtt). If set, the X-TIMESTAMP-MAP will be added as described in the [HLS specification](https://datatracker.ietf.org/doc/html/rfc8216#section-3.5). For example, if set to 10 seconds, *X-TIMESTAMP-MAP=MPEGTS:900000,LOCAL:00:00:00.000* will be added after each *WEBVTT* header. The default for TextMuxing is that the X-TIMESTAMP-MAP will not be written. Important to note is that the default for `startOffset` for [TsMuxings](#/Encoding/PostEncodingEncodingsMuxingsTsByEncodingId) and [ProgressiveTsMuxings](#/Encoding/PostEncodingEncodingsMuxingsProgressiveTsByEncodingId) is 10 seconds. If the output of this muxing is used for HLS together with video/audio streams using TsMuxings and ProgressiveTsMuxings, this value should be set to the same `startOffset`.

        :param start_offset: The start_offset of this TextMuxing.
        :type: int
        """

        if start_offset is not None:
            if not isinstance(start_offset, int):
                raise TypeError("Invalid type for `start_offset`, type has to be `int`")

        self._start_offset = start_offset

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(TextMuxing, self), "to_dict"):
            result = super(TextMuxing, self).to_dict()
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
        if not isinstance(other, TextMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
