# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.muxing import Muxing
from bitmovin_api_sdk.models.stream_conditions_mode import StreamConditionsMode
import pprint
import six


class ChunkedTextMuxing(Muxing):
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
                 segment_length=None,
                 segment_naming=None,
                 segment_naming_template=None,
                 start_offset=None,
                 segments_muxed=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, list[MuxingStream], list[EncodingOutput], int, int, int, list[Ignoring], StreamConditionsMode, float, string_types, string_types, int, int) -> None
        super(ChunkedTextMuxing, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, streams=streams, outputs=outputs, avg_bitrate=avg_bitrate, min_bitrate=min_bitrate, max_bitrate=max_bitrate, ignored_by=ignored_by, stream_conditions_mode=stream_conditions_mode)

        self._segment_length = None
        self._segment_naming = None
        self._segment_naming_template = None
        self._start_offset = None
        self._segments_muxed = None
        self.discriminator = None

        if segment_length is not None:
            self.segment_length = segment_length
        if segment_naming is not None:
            self.segment_naming = segment_naming
        if segment_naming_template is not None:
            self.segment_naming_template = segment_naming_template
        if start_offset is not None:
            self.start_offset = start_offset
        if segments_muxed is not None:
            self.segments_muxed = segments_muxed

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(ChunkedTextMuxing, self), 'openapi_types'):
            types = getattr(super(ChunkedTextMuxing, self), 'openapi_types')

        types.update({
            'segment_length': 'float',
            'segment_naming': 'string_types',
            'segment_naming_template': 'string_types',
            'start_offset': 'int',
            'segments_muxed': 'int'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(ChunkedTextMuxing, self), 'attribute_map'):
            attributes = getattr(super(ChunkedTextMuxing, self), 'attribute_map')

        attributes.update({
            'segment_length': 'segmentLength',
            'segment_naming': 'segmentNaming',
            'segment_naming_template': 'segmentNamingTemplate',
            'start_offset': 'startOffset',
            'segments_muxed': 'segmentsMuxed'
        })
        return attributes

    @property
    def segment_length(self):
        # type: () -> float
        """Gets the segment_length of this ChunkedTextMuxing.

        Length of the segments in seconds (required)

        :return: The segment_length of this ChunkedTextMuxing.
        :rtype: float
        """
        return self._segment_length

    @segment_length.setter
    def segment_length(self, segment_length):
        # type: (float) -> None
        """Sets the segment_length of this ChunkedTextMuxing.

        Length of the segments in seconds (required)

        :param segment_length: The segment_length of this ChunkedTextMuxing.
        :type: float
        """

        if segment_length is not None:
            if not isinstance(segment_length, (float, int)):
                raise TypeError("Invalid type for `segment_length`, type has to be `float`")

        self._segment_length = segment_length

    @property
    def segment_naming(self):
        # type: () -> string_types
        """Gets the segment_naming of this ChunkedTextMuxing.

        Segment naming template

        :return: The segment_naming of this ChunkedTextMuxing.
        :rtype: string_types
        """
        return self._segment_naming

    @segment_naming.setter
    def segment_naming(self, segment_naming):
        # type: (string_types) -> None
        """Sets the segment_naming of this ChunkedTextMuxing.

        Segment naming template

        :param segment_naming: The segment_naming of this ChunkedTextMuxing.
        :type: string_types
        """

        if segment_naming is not None:
            if not isinstance(segment_naming, string_types):
                raise TypeError("Invalid type for `segment_naming`, type has to be `string_types`")

        self._segment_naming = segment_naming

    @property
    def segment_naming_template(self):
        # type: () -> string_types
        """Gets the segment_naming_template of this ChunkedTextMuxing.

        Segment naming template with placeholders which will be replaced during the encoding. The result will be saved in segmentNaming. {rand:4} gets replaced with an alphanumeric string of length specified after the colon. Defaults to 32. If this field is set, segmentNaming must not be specified.

        :return: The segment_naming_template of this ChunkedTextMuxing.
        :rtype: string_types
        """
        return self._segment_naming_template

    @segment_naming_template.setter
    def segment_naming_template(self, segment_naming_template):
        # type: (string_types) -> None
        """Sets the segment_naming_template of this ChunkedTextMuxing.

        Segment naming template with placeholders which will be replaced during the encoding. The result will be saved in segmentNaming. {rand:4} gets replaced with an alphanumeric string of length specified after the colon. Defaults to 32. If this field is set, segmentNaming must not be specified.

        :param segment_naming_template: The segment_naming_template of this ChunkedTextMuxing.
        :type: string_types
        """

        if segment_naming_template is not None:
            if not isinstance(segment_naming_template, string_types):
                raise TypeError("Invalid type for `segment_naming_template`, type has to be `string_types`")

        self._segment_naming_template = segment_naming_template

    @property
    def start_offset(self):
        # type: () -> int
        """Gets the start_offset of this ChunkedTextMuxing.

        Offset of MPEG-TS timestamps in seconds. This only affects streams with [WebVttConfiguration](#/Encoding/PostEncodingConfigurationsSubtitlesWebVtt). If set, the X-TIMESTAMP-MAP will be added as described in the [HLS specification](https://datatracker.ietf.org/doc/html/rfc8216#section-3.5). For example, if set to 10 seconds, *X-TIMESTAMP-MAP=MPEGTS:900000,LOCAL:00:00:00.000* will be added after each *WEBVTT* header. The default for ChunkedTextMuxing is that the X-TIMESTAMP-MAP will not be written. Important to note is that the default for `startOffset` for [TsMuxings](#/Encoding/PostEncodingEncodingsMuxingsTsByEncodingId) and [ProgressiveTsMuxings](#/Encoding/PostEncodingEncodingsMuxingsProgressiveTsByEncodingId) is 10 seconds. If the output of this muxing is used for HLS together with video/audio streams using TsMuxings and ProgressiveTsMuxings, this value should be set to the same `startOffset`.

        :return: The start_offset of this ChunkedTextMuxing.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        # type: (int) -> None
        """Sets the start_offset of this ChunkedTextMuxing.

        Offset of MPEG-TS timestamps in seconds. This only affects streams with [WebVttConfiguration](#/Encoding/PostEncodingConfigurationsSubtitlesWebVtt). If set, the X-TIMESTAMP-MAP will be added as described in the [HLS specification](https://datatracker.ietf.org/doc/html/rfc8216#section-3.5). For example, if set to 10 seconds, *X-TIMESTAMP-MAP=MPEGTS:900000,LOCAL:00:00:00.000* will be added after each *WEBVTT* header. The default for ChunkedTextMuxing is that the X-TIMESTAMP-MAP will not be written. Important to note is that the default for `startOffset` for [TsMuxings](#/Encoding/PostEncodingEncodingsMuxingsTsByEncodingId) and [ProgressiveTsMuxings](#/Encoding/PostEncodingEncodingsMuxingsProgressiveTsByEncodingId) is 10 seconds. If the output of this muxing is used for HLS together with video/audio streams using TsMuxings and ProgressiveTsMuxings, this value should be set to the same `startOffset`.

        :param start_offset: The start_offset of this ChunkedTextMuxing.
        :type: int
        """

        if start_offset is not None:
            if not isinstance(start_offset, int):
                raise TypeError("Invalid type for `start_offset`, type has to be `int`")

        self._start_offset = start_offset

    @property
    def segments_muxed(self):
        # type: () -> int
        """Gets the segments_muxed of this ChunkedTextMuxing.

        Number of segments which have been encoded

        :return: The segments_muxed of this ChunkedTextMuxing.
        :rtype: int
        """
        return self._segments_muxed

    @segments_muxed.setter
    def segments_muxed(self, segments_muxed):
        # type: (int) -> None
        """Sets the segments_muxed of this ChunkedTextMuxing.

        Number of segments which have been encoded

        :param segments_muxed: The segments_muxed of this ChunkedTextMuxing.
        :type: int
        """

        if segments_muxed is not None:
            if not isinstance(segments_muxed, int):
                raise TypeError("Invalid type for `segments_muxed`, type has to be `int`")

        self._segments_muxed = segments_muxed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(ChunkedTextMuxing, self), "to_dict"):
            result = super(ChunkedTextMuxing, self).to_dict()
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
        if not isinstance(other, ChunkedTextMuxing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
