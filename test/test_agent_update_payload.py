# coding: utf-8

"""
    agent/service.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from agent.models.agent_update_payload import AgentUpdatePayload

class TestAgentUpdatePayload(unittest.TestCase):
    """AgentUpdatePayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentUpdatePayload:
        """Test AgentUpdatePayload
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentUpdatePayload`
        """
        model = AgentUpdatePayload()
        if include_optional:
            return AgentUpdatePayload(
                firstname = '',
                lastname = '',
                email = '',
                phone = ''
            )
        else:
            return AgentUpdatePayload(
        )
        """

    def testAgentUpdatePayload(self):
        """Test AgentUpdatePayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
