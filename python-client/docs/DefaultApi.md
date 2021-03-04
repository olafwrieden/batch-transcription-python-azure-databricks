# swagger_client.DefaultApi

All URIs are relative to *https://westus.api.cognitive.microsoft.com/speechtotext/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_model_to_subscription**](DefaultApi.md#copy_model_to_subscription) | **POST** /models/{id}/copyto | Copy Model
[**create_dataset**](DefaultApi.md#create_dataset) | **POST** /datasets | Create Dataset
[**create_endpoint**](DefaultApi.md#create_endpoint) | **POST** /endpoints | Create Endpoint
[**create_evaluation**](DefaultApi.md#create_evaluation) | **POST** /evaluations | Create Evaluation
[**create_hook**](DefaultApi.md#create_hook) | **POST** /webhooks | Create Web Hook
[**create_model**](DefaultApi.md#create_model) | **POST** /models | Create Model
[**create_project**](DefaultApi.md#create_project) | **POST** /projects | Create Project
[**create_transcription**](DefaultApi.md#create_transcription) | **POST** /transcriptions | Create Transcription
[**delete_base_model_log**](DefaultApi.md#delete_base_model_log) | **DELETE** /endpoints/base/{locale}/files/logs/{logId} | Delete Base Model Endpoint Log
[**delete_base_model_logs**](DefaultApi.md#delete_base_model_logs) | **DELETE** /endpoints/base/{locale}/files/logs | Delete All Base Model Endpoint Logs
[**delete_dataset**](DefaultApi.md#delete_dataset) | **DELETE** /datasets/{id} | Delete Dataset
[**delete_endpoint**](DefaultApi.md#delete_endpoint) | **DELETE** /endpoints/{id} | Delete Endpoint
[**delete_endpoint_log**](DefaultApi.md#delete_endpoint_log) | **DELETE** /endpoints/{id}/files/logs/{logId} | Delete Custom Model Endpoint Log
[**delete_endpoint_logs**](DefaultApi.md#delete_endpoint_logs) | **DELETE** /endpoints/{id}/files/logs | Delete All Custom Model Endpoint Logs
[**delete_evaluation**](DefaultApi.md#delete_evaluation) | **DELETE** /evaluations/{id} | Delete Evaluation
[**delete_hook**](DefaultApi.md#delete_hook) | **DELETE** /webhooks/{id} | Delete Web Hook
[**delete_model**](DefaultApi.md#delete_model) | **DELETE** /models/{id} | Delete Model
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /projects/{id} | Delete Project
[**delete_transcription**](DefaultApi.md#delete_transcription) | **DELETE** /transcriptions/{id} | Delete Transcription
[**get_base_model**](DefaultApi.md#get_base_model) | **GET** /models/base/{id} | Get Base Model
[**get_base_model_log**](DefaultApi.md#get_base_model_log) | **GET** /endpoints/base/{locale}/files/logs/{logId} | Get Base Model Endpoint Log
[**get_base_model_logs**](DefaultApi.md#get_base_model_logs) | **GET** /endpoints/base/{locale}/files/logs | Get Base Model Endpoint Logs
[**get_base_model_manifest**](DefaultApi.md#get_base_model_manifest) | **GET** /models/base/{id}/manifest | Get Base Model Manifest
[**get_base_models**](DefaultApi.md#get_base_models) | **GET** /models/base | Get Base Models
[**get_dataset**](DefaultApi.md#get_dataset) | **GET** /datasets/{id} | Get Dataset
[**get_dataset_file**](DefaultApi.md#get_dataset_file) | **GET** /datasets/{id}/files/{fileId} | Get Dataset File
[**get_dataset_files**](DefaultApi.md#get_dataset_files) | **GET** /datasets/{id}/files | Get Dataset Files
[**get_datasets**](DefaultApi.md#get_datasets) | **GET** /datasets | Get Datasets
[**get_datasets_for_project**](DefaultApi.md#get_datasets_for_project) | **GET** /projects/{id}/datasets | Get Datasets for Project
[**get_endpoint**](DefaultApi.md#get_endpoint) | **GET** /endpoints/{id} | Get Endpoint
[**get_endpoint_log**](DefaultApi.md#get_endpoint_log) | **GET** /endpoints/{id}/files/logs/{logId} | Get Custom Model Endpoint Log
[**get_endpoint_logs**](DefaultApi.md#get_endpoint_logs) | **GET** /endpoints/{id}/files/logs | Get Custom Model Endpoint Logs
[**get_endpoints**](DefaultApi.md#get_endpoints) | **GET** /endpoints | Get Endpoints
[**get_endpoints_for_project**](DefaultApi.md#get_endpoints_for_project) | **GET** /projects/{id}/endpoints | Get Endpoints for Project
[**get_evaluation**](DefaultApi.md#get_evaluation) | **GET** /evaluations/{id} | Get Evaluation
[**get_evaluation_file**](DefaultApi.md#get_evaluation_file) | **GET** /evaluations/{id}/files/{fileId} | Get Evaluation File
[**get_evaluation_files**](DefaultApi.md#get_evaluation_files) | **GET** /evaluations/{id}/files | Get Evaluation Files
[**get_evaluations**](DefaultApi.md#get_evaluations) | **GET** /evaluations | Get Evaluations
[**get_evaluations_for_project**](DefaultApi.md#get_evaluations_for_project) | **GET** /projects/{id}/evaluations | Get Evaluations for Project
[**get_health_status**](DefaultApi.md#get_health_status) | **GET** /healthstatus | Get Health Status
[**get_hook**](DefaultApi.md#get_hook) | **GET** /webhooks/{id} | Get Web Hook
[**get_hooks**](DefaultApi.md#get_hooks) | **GET** /webhooks | Get Web Hooks
[**get_model**](DefaultApi.md#get_model) | **GET** /models/{id} | Get Model
[**get_model_manifest**](DefaultApi.md#get_model_manifest) | **GET** /models/{id}/manifest | Get Custom Model Manifest
[**get_models**](DefaultApi.md#get_models) | **GET** /models | Get Custom Models
[**get_models_for_project**](DefaultApi.md#get_models_for_project) | **GET** /projects/{id}/models | Get Models for Project
[**get_project**](DefaultApi.md#get_project) | **GET** /projects/{id} | Get Project
[**get_projects**](DefaultApi.md#get_projects) | **GET** /projects | Get Projects
[**get_supported_locales_for_datasets**](DefaultApi.md#get_supported_locales_for_datasets) | **GET** /datasets/locales | Get Supported Locales for Datasets
[**get_supported_locales_for_endpoints**](DefaultApi.md#get_supported_locales_for_endpoints) | **GET** /endpoints/locales | Get Supported Locales for Endpoints
[**get_supported_locales_for_evaluations**](DefaultApi.md#get_supported_locales_for_evaluations) | **GET** /evaluations/locales | Get Supported Locales for Evaluations
[**get_supported_locales_for_models**](DefaultApi.md#get_supported_locales_for_models) | **GET** /models/locales | Get Supported Locales for Models
[**get_supported_locales_for_transcriptions**](DefaultApi.md#get_supported_locales_for_transcriptions) | **GET** /transcriptions/locales | Get Supported Locales for Transcriptions
[**get_supported_project_locales**](DefaultApi.md#get_supported_project_locales) | **GET** /projects/locales | Get Supported Locales for Projects
[**get_transcription**](DefaultApi.md#get_transcription) | **GET** /transcriptions/{id} | Get Transcription
[**get_transcription_file**](DefaultApi.md#get_transcription_file) | **GET** /transcriptions/{id}/files/{fileId} | Get Transcription File
[**get_transcription_files**](DefaultApi.md#get_transcription_files) | **GET** /transcriptions/{id}/files | Get Transcription Files
[**get_transcriptions**](DefaultApi.md#get_transcriptions) | **GET** /transcriptions | Get Transcriptions
[**get_transcriptions_for_project**](DefaultApi.md#get_transcriptions_for_project) | **GET** /projects/{id}/transcriptions | Get Transcriptions for Project
[**ping_hook**](DefaultApi.md#ping_hook) | **POST** /webhooks/{id}/ping | Ping Web Hook
[**test_hook**](DefaultApi.md#test_hook) | **POST** /webhooks/{id}/test | Test Web Hook
[**update_dataset**](DefaultApi.md#update_dataset) | **PATCH** /datasets/{id} | Update Dataset
[**update_endpoint**](DefaultApi.md#update_endpoint) | **PATCH** /endpoints/{id} | Update Endpoint
[**update_evaluation**](DefaultApi.md#update_evaluation) | **PATCH** /evaluations/{id} | Update Evaluation
[**update_hook**](DefaultApi.md#update_hook) | **PATCH** /webhooks/{id} | Update Web Hook
[**update_model**](DefaultApi.md#update_model) | **PATCH** /models/{id} | Update Model
[**update_project**](DefaultApi.md#update_project) | **PATCH** /projects/{id} | Update Project
[**update_transcription**](DefaultApi.md#update_transcription) | **PATCH** /transcriptions/{id} | Update Transcription
[**upload_dataset_from_form**](DefaultApi.md#upload_dataset_from_form) | **POST** /datasets/upload | Create Dataset from Form


# **copy_model_to_subscription**
> Model copy_model_to_subscription(id, model_copy=model_copy)

Copy Model

This method can be used to copy a model from one location to another. If the target subscription  key belongs to a subscription created for another location, the model will be copied to that location.  Only adapted models are allowed to copy to another subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the model that will be copied.
model_copy = swagger_client.ModelCopy() # ModelCopy | The body contains the subscription key of the target subscription. (optional)

try:
    # Copy Model
    api_response = api_instance.copy_model_to_subscription(id, model_copy=model_copy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->copy_model_to_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the model that will be copied. | 
 **model_copy** | [**ModelCopy**](ModelCopy.md)| The body contains the subscription key of the target subscription. | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset**
> Dataset create_dataset(dataset=dataset)

Create Dataset

Uploads and creates a new dataset by getting the data from a specified URL.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
dataset = swagger_client.Dataset() # Dataset | Definition for the new dataset. (optional)

try:
    # Create Dataset
    api_response = api_instance.create_dataset(dataset=dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | [**Dataset**](Dataset.md)| Definition for the new dataset. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_endpoint**
> Endpoint create_endpoint(endpoint=endpoint)

Create Endpoint

Creates a new endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
endpoint = swagger_client.Endpoint() # Endpoint | The details of the endpoint. (optional)

try:
    # Create Endpoint
    api_response = api_instance.create_endpoint(endpoint=endpoint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | [**Endpoint**](Endpoint.md)| The details of the endpoint. | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_evaluation**
> Evaluation create_evaluation(evaluation=evaluation)

Create Evaluation

Creates a new evaluation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
evaluation = swagger_client.Evaluation() # Evaluation | The details of the new evaluation. (optional)

try:
    # Create Evaluation
    api_response = api_instance.create_evaluation(evaluation=evaluation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation** | [**Evaluation**](Evaluation.md)| The details of the new evaluation. | [optional] 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hook**
> WebHook create_hook(web_hook=web_hook)

Create Web Hook

If the property secret in the configuration is present and contains a non-empty string, it will be used to create a SHA256 hash of the payload with  the secret as HMAC key. This hash will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.                When calling back into the registered URL, the request will contain a X-MicrosoftSpeechServices-Event header containing one of the registered event  types. There will be one request per registered event type.                After successfully registering the web hook, it will not be usable until a challenge/response is completed. To do this, a request with the event type  challenge will be made with a query parameter called validationToken. Respond to the challenge with a 200 OK containing the value of the validationToken  query parameter as the response body. When the challenge/response is successfully completed, the web hook will begin receiving events.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
web_hook = swagger_client.WebHook() # WebHook | The details of the new web hook. (optional)

try:
    # Create Web Hook
    api_response = api_instance.create_hook(web_hook=web_hook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook** | [**WebHook**](WebHook.md)| The details of the new web hook. | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_model**
> Model create_model(model=model)

Create Model

Creates a new model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
model = swagger_client.Model() # Model | The details of the new model. (optional)

try:
    # Create Model
    api_response = api_instance.create_model(model=model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**Model**](Model.md)| The details of the new model. | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> Project create_project(project=project)

Create Project

Creates a new project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project = swagger_client.Project() # Project | The details of the project. (optional)

try:
    # Create Project
    api_response = api_instance.create_project(project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)| The details of the project. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transcription**
> Transcription create_transcription(transcription=transcription)

Create Transcription

Creates a new transcription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
transcription = swagger_client.Transcription() # Transcription | The details of the new transcription. (optional)

try:
    # Create Transcription
    api_response = api_instance.create_transcription(transcription=transcription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transcription** | [**Transcription**](Transcription.md)| The details of the new transcription. | [optional] 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_base_model_log**
> delete_base_model_log(locale, log_id)

Delete Base Model Endpoint Log

Deletes one audio or transcription log that have been stored when using the default base model of a given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
log_id = 'log_id_example' # str | The identifier of the log.

try:
    # Delete Base Model Endpoint Log
    api_instance.delete_base_model_log(locale, log_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_base_model_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **log_id** | **str**| The identifier of the log. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_base_model_logs**
> delete_base_model_logs(locale, end_date=end_date)

Delete All Base Model Endpoint Logs

Deletion process is done asynchronously and can take up to one day depending on the amount of log files.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
end_date = 'end_date_example' # str | The end date of the audio logs deletion (specific day, UTC).              Expected format: \"yyyy-mm-dd\". for instance, \"2019-09-20\" results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. (optional)

try:
    # Delete All Base Model Endpoint Logs
    api_instance.delete_base_model_logs(locale, end_date=end_date)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_base_model_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **end_date** | **str**| The end date of the audio logs deletion (specific day, UTC).              Expected format: \&quot;yyyy-mm-dd\&quot;. for instance, \&quot;2019-09-20\&quot; results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(id)

Delete Dataset

Deletes the specified dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the dataset.

try:
    # Delete Dataset
    api_instance.delete_dataset(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the dataset. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint**
> delete_endpoint(id)

Delete Endpoint

Deletes the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.

try:
    # Delete Endpoint
    api_instance.delete_endpoint(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_log**
> delete_endpoint_log(id, log_id)

Delete Custom Model Endpoint Log

Deletes one audio or transcription log that have been stored for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.
log_id = 'log_id_example' # str | The identifier of the log.

try:
    # Delete Custom Model Endpoint Log
    api_instance.delete_endpoint_log(id, log_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_endpoint_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 
 **log_id** | **str**| The identifier of the log. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_endpoint_logs**
> delete_endpoint_logs(id, end_date=end_date)

Delete All Custom Model Endpoint Logs

The deletion process is done asynchronously and can take up to one day depending on the amount of log files.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.
end_date = 'end_date_example' # str | The end date of the audio logs deletion (specific day, UTC).              Expected format: \"yyyy-mm-dd\". for instance, \"2019-09-20\" results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. (optional)

try:
    # Delete All Custom Model Endpoint Logs
    api_instance.delete_endpoint_logs(id, end_date=end_date)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_endpoint_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 
 **end_date** | **str**| The end date of the audio logs deletion (specific day, UTC).              Expected format: \&quot;yyyy-mm-dd\&quot;. for instance, \&quot;2019-09-20\&quot; results in deleting all logs on September 20h, 2019 and before.              Deletes all existing logs when date is not specified. | [optional] 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_evaluation**
> delete_evaluation(id)

Delete Evaluation

Deletes the evaluation identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the evaluation.

try:
    # Delete Evaluation
    api_instance.delete_evaluation(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the evaluation. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hook**
> delete_hook(id)

Delete Web Hook

Deletes the web hook registration identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the web hook.

try:
    # Delete Web Hook
    api_instance.delete_hook(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the web hook. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> delete_model(id)

Delete Model

Deletes the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the model.

try:
    # Delete Model
    api_instance.delete_model(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the model. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)

Delete Project

Deletes the project identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.

try:
    # Delete Project
    api_instance.delete_project(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transcription**
> delete_transcription(id)

Delete Transcription

Deletes the specified transcription task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the transcription.

try:
    # Delete Transcription
    api_instance.delete_transcription(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the transcription. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base_model**
> Model get_base_model(id)

Get Base Model

Gets the base model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the base model.

try:
    # Get Base Model
    api_response = api_instance.get_base_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_base_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the base model. | 

### Return type

[**Model**](Model.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base_model_log**
> File get_base_model_log(locale, log_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Base Model Endpoint Log

Gets a specific audio or transcription log for the default base model in a given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
log_id = 'log_id_example' # str | The identifier of the log.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Base Model Endpoint Log
    api_response = api_instance.get_base_model_log(locale, log_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_base_model_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **log_id** | **str**| The identifier of the log. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base_model_logs**
> PaginatedFiles get_base_model_logs(locale, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)

Get Base Model Endpoint Logs

Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
locale = 'locale_example' # str | The language used to select the default base model.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)
skip_token = 'skip_token_example' # str | Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. (optional)
top = 56 # int | Format - int32. Number of files that will be included (between 1 and 5000). (optional)

try:
    # Get Base Model Endpoint Logs
    api_response = api_instance.get_base_model_logs(locale, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_base_model_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The language used to select the default base model. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 
 **skip_token** | **str**| Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. | [optional] 
 **top** | **int**| Format - int32. Number of files that will be included (between 1 and 5000). | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base_model_manifest**
> ModelManifest get_base_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Base Model Manifest

Returns an manifest for this base model which can be used in an on-premise container.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The ID of the model to generate a manifest for.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Base Model Manifest
    api_response = api_instance.get_base_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_base_model_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The ID of the model to generate a manifest for. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**ModelManifest**](ModelManifest.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base_models**
> PaginatedModels get_base_models(skip=skip, top=top)

Get Base Models

Gets the list of base models for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of base models that will be skipped. (optional)
top = 56 # int | Format - int32. Number of base models that will be included after skipping. (optional)

try:
    # Get Base Models
    api_response = api_instance.get_base_models(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_base_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of base models that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of base models that will be included after skipping. | [optional] 

### Return type

[**PaginatedModels**](PaginatedModels.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(id)

Get Dataset

Gets the dataset identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the dataset.

try:
    # Get Dataset
    api_response = api_instance.get_dataset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_file**
> File get_dataset_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Dataset File

Gets one specific file (identified with fileId) from a dataset (identified with id).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the dataset.
file_id = 'file_id_example' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Dataset File
    api_response = api_instance.get_dataset_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dataset_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the dataset. | 
 **file_id** | **str**| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_files**
> PaginatedFiles get_dataset_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)

Get Dataset Files

Gets the files of the dataset identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the dataset.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)
skip = 56 # int | Format - int32. Number of files that will be skipped. (optional)
top = 56 # int | Format - int32. Number of files that will be included after skipping. (optional)

try:
    # Get Dataset Files
    api_response = api_instance.get_dataset_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_dataset_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the dataset. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 
 **skip** | **int**| Format - int32. Number of files that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of files that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> PaginatedDatasets get_datasets(skip=skip, top=top)

Get Datasets

Gets a list of datasets for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)

try:
    # Get Datasets
    api_response = api_instance.get_datasets(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedDatasets**](PaginatedDatasets.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets_for_project**
> PaginatedDatasets get_datasets_for_project(id, skip=skip, top=top)

Get Datasets for Project

Gets the list of datasets for specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of datasets that will be skipped. (optional)
top = 56 # int | Format - int32. Number of datasets that will be included after skipping. (optional)

try:
    # Get Datasets for Project
    api_response = api_instance.get_datasets_for_project(id, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_datasets_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedDatasets**](PaginatedDatasets.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint**
> Endpoint get_endpoint(id)

Get Endpoint

Gets the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.

try:
    # Get Endpoint
    api_response = api_instance.get_endpoint(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_log**
> File get_endpoint_log(id, log_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Custom Model Endpoint Log

Gets a specific audio or transcription log for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.
log_id = 'log_id_example' # str | The identifier of the log.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Custom Model Endpoint Log
    api_response = api_instance.get_endpoint_log(id, log_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_endpoint_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 
 **log_id** | **str**| The identifier of the log. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoint_logs**
> PaginatedFiles get_endpoint_logs(id, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)

Get Custom Model Endpoint Logs

Gets the list of audio and transcription logs that have been stored for a given endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)
skip_token = 'skip_token_example' # str | Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. (optional)
top = 56 # int | Format - int32. Number of files that will be included (between 1 and 5000). (optional)

try:
    # Get Custom Model Endpoint Logs
    api_response = api_instance.get_endpoint_logs(id, sas_validity_in_seconds=sas_validity_in_seconds, skip_token=skip_token, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_endpoint_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 
 **skip_token** | **str**| Token to skip logs that were already retrieved in previous requests. Pagination starts from beginning when not defined. | [optional] 
 **top** | **int**| Format - int32. Number of files that will be included (between 1 and 5000). | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints**
> PaginatedEndpoints get_endpoints(skip=skip, top=top)

Get Endpoints

Gets the list of endpoints for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of endpoints that will be skipped. (optional)
top = 56 # int | Format - int32. Number of endpoints that will be included after skipping. (optional)

try:
    # Get Endpoints
    api_response = api_instance.get_endpoints(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of endpoints that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of endpoints that will be included after skipping. | [optional] 

### Return type

[**PaginatedEndpoints**](PaginatedEndpoints.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_endpoints_for_project**
> PaginatedEndpoints get_endpoints_for_project(id, skip=skip, top=top)

Get Endpoints for Project

Gets the list of endpoints for specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of endpoints that will be skipped. (optional)
top = 56 # int | Format - int32. Number of endpoints that will be included after skipping. (optional)

try:
    # Get Endpoints for Project
    api_response = api_instance.get_endpoints_for_project(id, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_endpoints_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of endpoints that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of endpoints that will be included after skipping. | [optional] 

### Return type

[**PaginatedEndpoints**](PaginatedEndpoints.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation**
> Evaluation get_evaluation(id)

Get Evaluation

Gets the evaluation identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the evaluation.

try:
    # Get Evaluation
    api_response = api_instance.get_evaluation(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the evaluation. | 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation_file**
> File get_evaluation_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Evaluation File

Gets one specific file (identified with fileId) from an evaluation (identified with id).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the evaluation.
file_id = 'file_id_example' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Evaluation File
    api_response = api_instance.get_evaluation_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_evaluation_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the evaluation. | 
 **file_id** | **str**| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation_files**
> PaginatedFiles get_evaluation_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)

Get Evaluation Files

Gets the files of the evaluation identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the evaluation.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)
skip = 56 # int | Format - int32. Number of files that will be skipped. (optional)
top = 56 # int | Format - int32. Number of files that will be included after skipping. (optional)

try:
    # Get Evaluation Files
    api_response = api_instance.get_evaluation_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_evaluation_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the evaluation. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 
 **skip** | **int**| Format - int32. Number of files that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of files that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluations**
> PaginatedEvaluations get_evaluations(skip=skip, top=top)

Get Evaluations

Gets the list of evaluations for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of evaluations that will be skipped. (optional)
top = 56 # int | Format - int32. Number of evaluations that will be included after skipping. (optional)

try:
    # Get Evaluations
    api_response = api_instance.get_evaluations(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_evaluations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of evaluations that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of evaluations that will be included after skipping. | [optional] 

### Return type

[**PaginatedEvaluations**](PaginatedEvaluations.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluations_for_project**
> PaginatedEvaluations get_evaluations_for_project(id, skip=skip, top=top)

Get Evaluations for Project

Gets the list of evaluations for specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of evaluations that will be skipped. (optional)
top = 56 # int | Format - int32. Number of evaluations that will be included after skipping. (optional)

try:
    # Get Evaluations for Project
    api_response = api_instance.get_evaluations_for_project(id, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_evaluations_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of evaluations that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of evaluations that will be included after skipping. | [optional] 

### Return type

[**PaginatedEvaluations**](PaginatedEvaluations.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_health_status**
> HealthStatus get_health_status()

Get Health Status

Returns the overall health of the service and optionally of the different subcomponents.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Health Status
    api_response = api_instance.get_health_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_health_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthStatus**](HealthStatus.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hook**
> WebHook get_hook(id)

Get Web Hook

Gets the web hook registration identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the web hook.

try:
    # Get Web Hook
    api_response = api_instance.get_hook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the web hook. | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hooks**
> PaginatedWebHooks get_hooks(skip=skip, top=top)

Get Web Hooks

Gets the list of web hook registrations for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of hooks that will be skipped. (optional)
top = 56 # int | Format - int32. Number of hooks that will be included after skipping. (optional)

try:
    # Get Web Hooks
    api_response = api_instance.get_hooks(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of hooks that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of hooks that will be included after skipping. | [optional] 

### Return type

[**PaginatedWebHooks**](PaginatedWebHooks.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model**
> Model get_model(id)

Get Model

Gets the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the model.

try:
    # Get Model
    api_response = api_instance.get_model(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the model. | 

### Return type

[**Model**](Model.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_manifest**
> ModelManifest get_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Custom Model Manifest

Returns an manifest for this model which can be used in an on-premise container.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The ID of the model to generate a manifest for.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Custom Model Manifest
    api_response = api_instance.get_model_manifest(id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_model_manifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The ID of the model to generate a manifest for. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**ModelManifest**](ModelManifest.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> PaginatedModels get_models(skip=skip, top=top)

Get Custom Models

Gets the list of custom models for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of models that will be skipped. (optional)
top = 56 # int | Format - int32. Number of models that will be included after skipping. (optional)

try:
    # Get Custom Models
    api_response = api_instance.get_models(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of models that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of models that will be included after skipping. | [optional] 

### Return type

[**PaginatedModels**](PaginatedModels.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models_for_project**
> PaginatedModels get_models_for_project(id, skip=skip, top=top)

Get Models for Project

Gets the list of models for specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of models that will be skipped. (optional)
top = 56 # int | Format - int32. Number of models that will be included after skipping. (optional)

try:
    # Get Models for Project
    api_response = api_instance.get_models_for_project(id, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_models_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of models that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of models that will be included after skipping. | [optional] 

### Return type

[**PaginatedModels**](PaginatedModels.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id)

Get Project

Gets the project identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.

try:
    # Get Project
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 

### Return type

[**Project**](Project.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> PaginatedProjects get_projects(skip=skip, top=top)

Get Projects

Gets the list of projects for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of projects that will be skipped. (optional)
top = 56 # int | Format - int32. Number of projects that will be included after skipping. (optional)

try:
    # Get Projects
    api_response = api_instance.get_projects(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of projects that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of projects that will be included after skipping. | [optional] 

### Return type

[**PaginatedProjects**](PaginatedProjects.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_datasets**
> ApiSpeechtotextV30DatasetsLocalesGet200ApplicationJsonResponse get_supported_locales_for_datasets()

Get Supported Locales for Datasets

Gets a list of supported locales for data imports.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Supported Locales for Datasets
    api_response = api_instance.get_supported_locales_for_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_supported_locales_for_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSpeechtotextV30DatasetsLocalesGet200ApplicationJsonResponse**](ApiSpeechtotextV30DatasetsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_endpoints**
> ApiSpeechtotextV30EndpointsLocalesGet200ApplicationJsonResponse get_supported_locales_for_endpoints()

Get Supported Locales for Endpoints

Gets a list of supported locales for endpoint creations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Supported Locales for Endpoints
    api_response = api_instance.get_supported_locales_for_endpoints()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_supported_locales_for_endpoints: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSpeechtotextV30EndpointsLocalesGet200ApplicationJsonResponse**](ApiSpeechtotextV30EndpointsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_evaluations**
> ApiSpeechtotextV30EvaluationsLocalesGet200ApplicationJsonResponse get_supported_locales_for_evaluations()

Get Supported Locales for Evaluations

Gets a list of supported locales for evaluations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Supported Locales for Evaluations
    api_response = api_instance.get_supported_locales_for_evaluations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_supported_locales_for_evaluations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSpeechtotextV30EvaluationsLocalesGet200ApplicationJsonResponse**](ApiSpeechtotextV30EvaluationsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_models**
> ApiSpeechtotextV30ModelsLocalesGet200ApplicationJsonResponse get_supported_locales_for_models()

Get Supported Locales for Models

Gets a list of supported locales for model adaptation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Supported Locales for Models
    api_response = api_instance.get_supported_locales_for_models()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_supported_locales_for_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSpeechtotextV30ModelsLocalesGet200ApplicationJsonResponse**](ApiSpeechtotextV30ModelsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_transcriptions**
> ApiSpeechtotextV30TranscriptionsLocalesGet200ApplicationJsonResponse get_supported_locales_for_transcriptions()

Get Supported Locales for Transcriptions

Gets a list of supported locales for offline transcriptions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Supported Locales for Transcriptions
    api_response = api_instance.get_supported_locales_for_transcriptions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_supported_locales_for_transcriptions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSpeechtotextV30TranscriptionsLocalesGet200ApplicationJsonResponse**](ApiSpeechtotextV30TranscriptionsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_project_locales**
> ApiSpeechtotextV30ProjectsLocalesGet200ApplicationJsonResponse get_supported_project_locales()

Get Supported Locales for Projects

Gets the list of supported locales.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

try:
    # Get Supported Locales for Projects
    api_response = api_instance.get_supported_project_locales()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_supported_project_locales: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSpeechtotextV30ProjectsLocalesGet200ApplicationJsonResponse**](ApiSpeechtotextV30ProjectsLocalesGet200ApplicationJsonResponse.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcription**
> Transcription get_transcription(id)

Get Transcription

Gets the transcription identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the transcription.

try:
    # Get Transcription
    api_response = api_instance.get_transcription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the transcription. | 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcription_file**
> File get_transcription_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Get Transcription File

Gets one specific file (identified with fileId) from a transcription (identified with id).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the transcription.
file_id = 'file_id_example' # str | Format - uuid. The identifier of the file.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)

try:
    # Get Transcription File
    api_response = api_instance.get_transcription_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transcription_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the transcription. | 
 **file_id** | **str**| Format - uuid. The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcription_files**
> PaginatedFiles get_transcription_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)

Get Transcription Files

Gets the files of the transcription identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the transcription.
sas_validity_in_seconds = 56 # int | Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. (optional)
skip = 56 # int | Format - int32. Number of files that will be skipped. (optional)
top = 56 # int | Format - int32. Number of files that will be included after skipping. (optional)

try:
    # Get Transcription Files
    api_response = api_instance.get_transcription_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transcription_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the transcription. | 
 **sas_validity_in_seconds** | **int**| Format - int32. The duration in seconds that an SAS url should be valid. The default duration is 12 hours. | [optional] 
 **skip** | **int**| Format - int32. Number of files that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of files that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcriptions**
> PaginatedTranscriptions get_transcriptions(skip=skip, top=top)

Get Transcriptions

Gets a list of transcriptions for the authenticated subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
skip = 56 # int | Format - int32. Number of transcriptions that will be skipped. (optional)
top = 56 # int | Format - int32. Number of transcriptions that will be included after skipping. (optional)

try:
    # Get Transcriptions
    api_response = api_instance.get_transcriptions(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transcriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Format - int32. Number of transcriptions that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of transcriptions that will be included after skipping. | [optional] 

### Return type

[**PaginatedTranscriptions**](PaginatedTranscriptions.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transcriptions_for_project**
> PaginatedTranscriptions get_transcriptions_for_project(id, skip=skip, top=top)

Get Transcriptions for Project

Gets the list of transcriptions for specified project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.
skip = 56 # int | Format - int32. Number of transcriptions that will be skipped. (optional)
top = 56 # int | Format - int32. Number of transcriptions that will be included after skipping. (optional)

try:
    # Get Transcriptions for Project
    api_response = api_instance.get_transcriptions_for_project(id, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transcriptions_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 
 **skip** | **int**| Format - int32. Number of transcriptions that will be skipped. | [optional] 
 **top** | **int**| Format - int32. Number of transcriptions that will be included after skipping. | [optional] 

### Return type

[**PaginatedTranscriptions**](PaginatedTranscriptions.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_hook**
> ping_hook(id)

Ping Web Hook

The request body of the POST request sent to the registered web hook URL is of the same shape as in the GET request for a specific hook.  The Swagger Schema ID of the model is WebHookV3.                The request will contain a X-MicrosoftSpeechServices-Event header with the value ping. If the web hook was registered with  a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with  the secret as HMAC key. The hash is base64 encoded.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the web hook to ping.

try:
    # Ping Web Hook
    api_instance.ping_hook(id)
except ApiException as e:
    print("Exception when calling DefaultApi->ping_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the web hook to ping. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_hook**
> test_hook(id)

Test Web Hook

The payload will be generated from the last entity that would have invoked the web hook. If no entity is present for none of the registered event types,  the POST will respond with 204. If a test request can be made, it will respond with 200.  The request will contain a X-MicrosoftSpeechServices-Event header with the respective registered event type.  If the web hook was registered with a secret it will contain a X-MicrosoftSpeechServices-Signature header with an SHA256 hash of the payload with  the secret as HMAC key. The hash is base64 encoded.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the web hook to ping.

try:
    # Test Web Hook
    api_instance.test_hook(id)
except ApiException as e:
    print("Exception when calling DefaultApi->test_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the web hook to ping. | 

### Return type

void (empty response body)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(id, dataset_update=dataset_update)

Update Dataset

Updates the mutable details of the dataset identified by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the dataset.
dataset_update = swagger_client.DatasetUpdate() # DatasetUpdate | The updated values for the dataset. (optional)

try:
    # Update Dataset
    api_response = api_instance.update_dataset(id, dataset_update=dataset_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the dataset. | 
 **dataset_update** | [**DatasetUpdate**](DatasetUpdate.md)| The updated values for the dataset. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_endpoint**
> Endpoint update_endpoint(id, endpoint_update=endpoint_update)

Update Endpoint

Updates the metadata of the endpoint identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the endpoint.
endpoint_update = swagger_client.EndpointUpdate() # EndpointUpdate | The updated values for the endpoint. (optional)

try:
    # Update Endpoint
    api_response = api_instance.update_endpoint(id, endpoint_update=endpoint_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the endpoint. | 
 **endpoint_update** | [**EndpointUpdate**](EndpointUpdate.md)| The updated values for the endpoint. | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_evaluation**
> Evaluation update_evaluation(id, evaluation_update=evaluation_update)

Update Evaluation

Updates the mutable details of the evaluation identified by its id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the evaluation.
evaluation_update = swagger_client.EvaluationUpdate() # EvaluationUpdate | The object containing the updated fields of the evaluation. (optional)

try:
    # Update Evaluation
    api_response = api_instance.update_evaluation(id, evaluation_update=evaluation_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the evaluation. | 
 **evaluation_update** | [**EvaluationUpdate**](EvaluationUpdate.md)| The object containing the updated fields of the evaluation. | [optional] 

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hook**
> WebHook update_hook(id, web_hook_update=web_hook_update)

Update Web Hook

If the property secret in the configuration is omitted or contains an empty string, future callbacks won't contain X-MicrosoftSpeechServices-Signature  headers. If the property contains a non-empty string, it will be used to create a SHA256 hash of the payload with the secret as HMAC key. This hash  will be set as X-MicrosoftSpeechServices-Signature header when calling back into the registered URL.                If the URL changes,  the web hook will stop receiving events until a  challenge/response is completed. To do this, a request with the event type challenge will be made with a query parameter called validationToken.  Respond to the challenge with a 200 OK containing the value of the validationToken query parameter as the response body. When the challenge/response  is successfully completed, the web hook will begin receiving events.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the web hook.
web_hook_update = swagger_client.WebHookUpdate() # WebHookUpdate | The updated values for the web hook. (optional)

try:
    # Update Web Hook
    api_response = api_instance.update_hook(id, web_hook_update=web_hook_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the web hook. | 
 **web_hook_update** | [**WebHookUpdate**](WebHookUpdate.md)| The updated values for the web hook. | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> Model update_model(id, model_update=model_update)

Update Model

Updates the metadata of the model identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the model.
model_update = swagger_client.ModelUpdate() # ModelUpdate | The updated values for the model. (optional)

try:
    # Update Model
    api_response = api_instance.update_model(id, model_update=model_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the model. | 
 **model_update** | [**ModelUpdate**](ModelUpdate.md)| The updated values for the model. | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(id, project_update=project_update)

Update Project

Updates the project identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the project.
project_update = swagger_client.ProjectUpdate() # ProjectUpdate | The updated values for the project. (optional)

try:
    # Update Project
    api_response = api_instance.update_project(id, project_update=project_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the project. | 
 **project_update** | [**ProjectUpdate**](ProjectUpdate.md)| The updated values for the project. | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transcription**
> Transcription update_transcription(id, transcription_update=transcription_update)

Update Transcription

Updates the mutable details of the transcription identified by its ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Format - uuid. The identifier of the transcription.
transcription_update = swagger_client.TranscriptionUpdate() # TranscriptionUpdate | The updated values for the transcription. (optional)

try:
    # Update Transcription
    api_response = api_instance.update_transcription(id, transcription_update=transcription_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_transcription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Format - uuid. The identifier of the transcription. | 
 **transcription_update** | [**TranscriptionUpdate**](TranscriptionUpdate.md)| The updated values for the transcription. | [optional] 

### Return type

[**Transcription**](Transcription.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset_from_form**
> Dataset upload_dataset_from_form(project=project, display_name=display_name, description=description, locale=locale, kind=kind, custom_properties=custom_properties, data=data, email=email)

Create Dataset from Form

Uploads data and creates a new dataset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = swagger_client.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
project = 'project_example' # str | The optional string representation of the url of a project. If set, the dataset will be associated with that project. (optional)
display_name = 'display_name_example' # str | The name of this data import (required). (optional)
description = 'description_example' # str | Optional description of this data import. (optional)
locale = 'locale_example' # str | The locale of this data import (required). (optional)
kind = 'kind_example' # str | The kind of the data import (required). (optional)
custom_properties = 'custom_properties_example' # str | The optional custom properties of this entity. The maximum allowed key length is 64 characters, the maximum allowed value length is 256 characters and the count of allowed entries is 10. (optional)
data = '/path/to/file.txt' # file | For acoustic data imports, a zip file containing the audio data and a text file containing the transcriptions for the audio data. for language data imports, a text file containing the language or pronunciation data. Required in both cases. (optional)
email = 'email_example' # str | An optional string containing the email address to send email notifications to in case the operation completes. The value will be removed after successfully sending the email. (optional)

try:
    # Create Dataset from Form
    api_response = api_instance.upload_dataset_from_form(project=project, display_name=display_name, description=description, locale=locale, kind=kind, custom_properties=custom_properties, data=data, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->upload_dataset_from_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| The optional string representation of the url of a project. If set, the dataset will be associated with that project. | [optional] 
 **display_name** | **str**| The name of this data import (required). | [optional] 
 **description** | **str**| Optional description of this data import. | [optional] 
 **locale** | **str**| The locale of this data import (required). | [optional] 
 **kind** | **str**| The kind of the data import (required). | [optional] 
 **custom_properties** | **str**| The optional custom properties of this entity. The maximum allowed key length is 64 characters, the maximum allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
 **data** | **file**| For acoustic data imports, a zip file containing the audio data and a text file containing the transcriptions for the audio data. for language data imports, a text file containing the language or pronunciation data. Required in both cases. | [optional] 
 **email** | **str**| An optional string containing the email address to send email notifications to in case the operation completes. The value will be removed after successfully sending the email. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[apiKeyHeader](../README.md#apiKeyHeader), [apiKeyQuery](../README.md#apiKeyQuery)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

