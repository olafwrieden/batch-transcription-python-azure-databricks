# coding: utf-8

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class WebHookUpdate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'web_url': 'str',
        'properties': 'WebHookPropertiesUpdate',
        'events': 'object',
        'display_name': 'str',
        'description': 'str',
        'custom_properties': 'dict(str, str)'
    }

    attribute_map = {
        'web_url': 'webUrl',
        'properties': 'properties',
        'events': 'events',
        'display_name': 'displayName',
        'description': 'description',
        'custom_properties': 'customProperties'
    }

    def __init__(self, web_url=None, properties=None, events=None, display_name=None, description=None, custom_properties=None, _configuration=None):  # noqa: E501
        """WebHookUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._web_url = None
        self._properties = None
        self._events = None
        self._display_name = None
        self._description = None
        self._custom_properties = None
        self.discriminator = None

        if web_url is not None:
            self.web_url = web_url
        if properties is not None:
            self.properties = properties
        if events is not None:
            self.events = events
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def web_url(self):
        """Gets the web_url of this WebHookUpdate.  # noqa: E501

        The registered URL that will be used to send the POST requests for the registered events to.  # noqa: E501

        :return: The web_url of this WebHookUpdate.  # noqa: E501
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this WebHookUpdate.

        The registered URL that will be used to send the POST requests for the registered events to.  # noqa: E501

        :param web_url: The web_url of this WebHookUpdate.  # noqa: E501
        :type: str
        """

        self._web_url = web_url

    @property
    def properties(self):
        """Gets the properties of this WebHookUpdate.  # noqa: E501

        Additional configuration options when updating a webhook.  # noqa: E501

        :return: The properties of this WebHookUpdate.  # noqa: E501
        :rtype: WebHookPropertiesUpdate
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this WebHookUpdate.

        Additional configuration options when updating a webhook.  # noqa: E501

        :param properties: The properties of this WebHookUpdate.  # noqa: E501
        :type: WebHookPropertiesUpdate
        """

        self._properties = properties

    @property
    def events(self):
        """Gets the events of this WebHookUpdate.  # noqa: E501

        A value indicating the webhook event kinds.  # noqa: E501

        :return: The events of this WebHookUpdate.  # noqa: E501
        :rtype: object
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this WebHookUpdate.

        A value indicating the webhook event kinds.  # noqa: E501

        :param events: The events of this WebHookUpdate.  # noqa: E501
        :type: object
        """

        self._events = events

    @property
    def display_name(self):
        """Gets the display_name of this WebHookUpdate.  # noqa: E501

        The name of the object.  # noqa: E501

        :return: The display_name of this WebHookUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this WebHookUpdate.

        The name of the object.  # noqa: E501

        :param display_name: The display_name of this WebHookUpdate.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this WebHookUpdate.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this WebHookUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebHookUpdate.

        The description of the object.  # noqa: E501

        :param description: The description of this WebHookUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def custom_properties(self):
        """Gets the custom_properties of this WebHookUpdate.  # noqa: E501

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :return: The custom_properties of this WebHookUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this WebHookUpdate.

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :param custom_properties: The custom_properties of this WebHookUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(WebHookUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WebHookUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebHookUpdate):
            return True

        return self.to_dict() != other.to_dict()
