# agent_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: version not set
- Package version: 1.2.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-agent.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-agent.git`)

Then import the package:
```python
import agent
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import agent
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import agent
from agent.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://agent.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = agent.Configuration(
    host = "https://agent.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with agent.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = agent.AgentApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    body = agent.AgentCreateAgentRequest() # AgentCreateAgentRequest | 

    try:
        api_response = api_instance.agent_create_agent(tenant_id, body)
        print("The response of AgentApi->agent_create_agent:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentApi->agent_create_agent: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://agent.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentApi* | [**agent_create_agent**](docs/AgentApi.md#agent_create_agent) | **POST** /v1/{tenantId}/agent/create | 
*AgentApi* | [**agent_get_agent**](docs/AgentApi.md#agent_get_agent) | **GET** /v1/{tenantId}/agent/{id} | 
*AgentApi* | [**agent_list_agents**](docs/AgentApi.md#agent_list_agents) | **POST** /v1/{tenantId}/agent/list/page-size/{pageSize} | 
*AgentApi* | [**agent_update_agent**](docs/AgentApi.md#agent_update_agent) | **PUT** /v1/{tenantId}/agent/{id} | 


## Documentation For Models

 - [AgentAgentEntity](docs/AgentAgentEntity.md)
 - [AgentCreateAgentRequest](docs/AgentCreateAgentRequest.md)
 - [AgentListAgentsRequest](docs/AgentListAgentsRequest.md)
 - [AgentListResponse](docs/AgentListResponse.md)
 - [AgentSortOrder](docs/AgentSortOrder.md)
 - [AgentUpdateAgentRequest](docs/AgentUpdateAgentRequest.md)
 - [AgentUpdatePayload](docs/AgentUpdatePayload.md)
 - [ListRequestFilters](docs/ListRequestFilters.md)
 - [ListRequestSort](docs/ListRequestSort.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [SortSortField](docs/SortSortField.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="geminiAuthorization"></a>
### geminiAuthorization

- **Type**: API key
- **API key parameter name**: X-Gem-Token
- **Location**: HTTP header


## Author




