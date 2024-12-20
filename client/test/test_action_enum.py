# coding: utf-8

"""
    Authoring API

    Experimental API to edit xblocks and course content.       Danger: Do not use on running courses!        - How to gain access: Please email the owners of this openedx service.       - How to use: This API uses oauth2 authentication with the     access token endpoint: `http://localhost:18000/oauth2/access_token`.     Please see separately provided documentation.       - How to test: You must be logged in as course author for whatever course you want to test with.     You can use the [Swagger UI](https://localhost:18000/authoring-api/ui/) to \"Try out\" the API with your test course. To do this, you must select the \"Local\" server.       - Public vs. Local servers: The \"Public\" server is where you can reach the API externally. The \"Local\" server is     for development with a local edx-platform version,  and for use via the [Swagger UI](https://localhost:18010/authoring-api/ui/).       - Swaggerfile: [Download link](https://localhost:18000/authoring-api/schema/)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.action_enum import ActionEnum

class TestActionEnum(unittest.TestCase):
    """ActionEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActionEnum(self):
        """Test ActionEnum"""
        # inst = ActionEnum()

if __name__ == '__main__':
    unittest.main()
