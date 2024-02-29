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

from agent.models.agent_list_response import AgentListResponse

class TestAgentListResponse(unittest.TestCase):
    """AgentListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentListResponse:
        """Test AgentListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentListResponse`
        """
        model = AgentListResponse()
        if include_optional:
            return AgentListResponse(
                agents = [
                    agent.models.agent_agent_entity.agentAgentEntity(
                        id = '', 
                        grn = '', 
                        code = '', 
                        firstname = '', 
                        lastname = '', 
                        email = '', 
                        phone = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                page_token = ''
            )
        else:
            return AgentListResponse(
        )
        """

    def testAgentListResponse(self):
        """Test AgentListResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
