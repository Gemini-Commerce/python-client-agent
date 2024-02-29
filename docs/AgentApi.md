# agent.AgentApi

All URIs are relative to *https://agent.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_create_agent**](AgentApi.md#agent_create_agent) | **POST** /v1/{tenantId}/agent/create | 
[**agent_get_agent**](AgentApi.md#agent_get_agent) | **GET** /v1/{tenantId}/agent/{id} | 
[**agent_list_agents**](AgentApi.md#agent_list_agents) | **POST** /v1/{tenantId}/agent/list/page-size/{pageSize} | 
[**agent_update_agent**](AgentApi.md#agent_update_agent) | **PUT** /v1/{tenantId}/agent/{id} | 


# **agent_create_agent**
> AgentAgentEntity agent_create_agent(tenant_id, body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import agent
from agent.models.agent_agent_entity import AgentAgentEntity
from agent.models.agent_create_agent_request import AgentCreateAgentRequest
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
    except Exception as e:
        print("Exception when calling AgentApi->agent_create_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **body** | [**AgentCreateAgentRequest**](AgentCreateAgentRequest.md)|  | 

### Return type

[**AgentAgentEntity**](AgentAgentEntity.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_get_agent**
> AgentAgentEntity agent_get_agent(tenant_id, id)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import agent
from agent.models.agent_agent_entity import AgentAgentEntity
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
    id = 'id_example' # str | 

    try:
        api_response = api_instance.agent_get_agent(tenant_id, id)
        print("The response of AgentApi->agent_get_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->agent_get_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 

### Return type

[**AgentAgentEntity**](AgentAgentEntity.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_list_agents**
> AgentListResponse agent_list_agents(tenant_id, page_size, body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import agent
from agent.models.agent_list_agents_request import AgentListAgentsRequest
from agent.models.agent_list_response import AgentListResponse
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
    page_size = 56 # int | 
    body = agent.AgentListAgentsRequest() # AgentListAgentsRequest | 

    try:
        api_response = api_instance.agent_list_agents(tenant_id, page_size, body)
        print("The response of AgentApi->agent_list_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->agent_list_agents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **page_size** | **int**|  | 
 **body** | [**AgentListAgentsRequest**](AgentListAgentsRequest.md)|  | 

### Return type

[**AgentListResponse**](AgentListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agent_update_agent**
> AgentAgentEntity agent_update_agent(tenant_id, id, body)



### Example

* Api Key Authentication (Authorization):

```python
import time
import os
import agent
from agent.models.agent_agent_entity import AgentAgentEntity
from agent.models.agent_update_agent_request import AgentUpdateAgentRequest
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
    id = 'id_example' # str | 
    body = agent.AgentUpdateAgentRequest() # AgentUpdateAgentRequest | 

    try:
        api_response = api_instance.agent_update_agent(tenant_id, id, body)
        print("The response of AgentApi->agent_update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->agent_update_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**AgentUpdateAgentRequest**](AgentUpdateAgentRequest.md)|  | 

### Return type

[**AgentAgentEntity**](AgentAgentEntity.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

