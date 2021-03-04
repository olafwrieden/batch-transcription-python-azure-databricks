# TranscriptionProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diarization_enabled** | **bool** | A value indicating whether diarization (speaker separation) is requested. | [optional] 
**word_level_timestamps_enabled** | **bool** | A value indicating whether word level timestamps are requested. | [optional] 
**duration** | **str** | The duration of the transcription. The duration is encoded as ISO 8601 duration  (\&quot;PnYnMnDTnHnMnS\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Durations). | [optional] 
**channels** | **list[int]** | A collection of the requested channel numbers.  In the default case, the channels 0 and 1 are considered. | [optional] 
**destination_container_url** | **str** | The requested destination container. | [optional] 
**punctuation_mode** | **str** | The requested punctuation mode. | [optional] 
**profanity_filter_mode** | **str** | The requested profanity filter mode. | [optional] 
**time_to_live** | **str** | How long the transcription will be kept in the system. Once the transcription reaches the time to live  after completion (successful or failed) it will be automatically deleted. Not setting this value or setting  to 0 will disable automatic deletion.  The duration is encoded as ISO 8601 duration (\&quot;PnYnMnDTnHnMnS\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Durations). | [optional] 
**email** | **str** | The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email. | [optional] 
**error** | [**EntityError**](EntityError.md) | The details of the error in case the entity is in a failed state. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


