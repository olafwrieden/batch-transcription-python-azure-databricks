# Azure Batch Transcription using Python in Databricks

## Outcome & Overview
Referencing a Blob Storage (in Azure) containing voice recordings, we want to be able to call the [Speech to Text Cognitive Service](https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/) in Azure to transcribe the respective recordings in parallel (batch), and save the transcript into another Blob Storage container.

## Setup

![Azure Resources](https://i.imgur.com/juD5Z2g.png)

__Navigate to Azure Portal and create the following services under a common Resource Group.__
- Storage Account (with two Blob Storage containers named `recordings` and `transcriptions` for our input and output files respectively)
- Cognitive Services (Speech Service)
- Azure Databricks Service

__Collect the following details:__
1. Copy the `Subscription Key` and and `ServiceRegion (Location)` from your Speech Service's Keys and Endpoint tab.
2. Navigate to the recordings container and create a Shared Access Signature (SAS) with `Read` and `List` permissions. Copy the Blob SAS URL.
3. Navigate to the transcriptions container and create a Shared Access Signature (SAS) with `Write` permissions. Copy the Blob SAS URL.

__Create a new Databricks Workspace__
1. In a new Databricks Notebook, create a new cell and paste:
```python
# Install requests library
%pip install requests

# Install Speech to Text API
%pip install -e "git+https://github.com/olafwrieden/python-batch-transcription-library/#egg=subdir&subdirectory=python-client"
```

2. Create a new cell underneath the above and paste the below, carefully adding the keys and URLs copied earlier, into their respective variables:
```python
import logging
import sys
import requests
import time
import swagger_client as cris_client

# Configure Logging
logging.basicConfig(stream=sys.stdout, level=logging.VERBOSE, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p %Z")

# TODO: Paste your keys and URLs into their respective variables

# Your subscription key and region for the speech service
SUBSCRIPTION_KEY = # "YourSubscriptionKey"
SERVICE_REGION = # "YourServiceRegion"

NAME = "Phone Call Transcriptions"
DESCRIPTION = "Demo of container-based phone call transcriptions."

LOCALE = "en-US"
RECORDINGS_BLOB_URI = # "<Your SAS URI to a single recording to transcribe (not container)>"

# Provide the URI of a container with audio files for transcribing all of them with a single request
RECORDINGS_CONTAINER_URI = # "<Your SAS Uri to a container of audio files>"
```

3. Create a third cell beneath the above, then paste the following methods:
```python
def transcribe_from_single_blob(uri, properties):
    """
    Transcribe a single audio file located at `uri` using the settings specified in `properties`
    using the base model for the specified locale.
    """
    transcription_definition = cris_client.Transcription(
        display_name=NAME,
        description=DESCRIPTION,
        locale=LOCALE,
        content_urls=[uri],
        properties=properties
    )

    return transcription_definition

def transcribe_from_container(uri, properties):
    """
    Transcribe all files in the container located at `uri` using the settings specified in `properties`
    using the base model for the specified locale.
    """
    transcription_definition = cris_client.Transcription(
        display_name=NAME,
        description=DESCRIPTION,
        locale=LOCALE,
        content_container_url=uri,
        properties=properties
    )

    return transcription_definition
    
def _paginate(api, paginated_object):
    """
    The autogenerated client does not support pagination. This function returns a generator over
    all items of the array that the paginated object `paginated_object` is part of.
    """
    yield from paginated_object.values
    typename = type(paginated_object).__name__
    auth_settings = ["apiKeyHeader", "apiKeyQuery"]
    while paginated_object.next_link:
        link = paginated_object.next_link[len(
            api.api_client.configuration.host):]
        paginated_object, status, headers = api.api_client.call_api(link, "GET",
                                                                    response_type=typename, auth_settings=auth_settings)

        if status == 200:
            yield from paginated_object.values
        else:
            raise Exception(
                f"could not receive paginated data: status {status}")
```

4. Create a fourth cell underneath the above, and paste the batch transcription function:
```python
def transcribe():
    logging.info("Starting transcription client...")

    # configure API key authorization: subscription_key
    configuration = cris_client.Configuration()
    configuration.api_key["Ocp-Apim-Subscription-Key"] = SUBSCRIPTION_KEY
    configuration.host = f"https://{SERVICE_REGION}.api.cognitive.microsoft.com/speechtotext/v3.0"

    # create the client object and authenticate
    client = cris_client.ApiClient(configuration)

    # create an instance of the transcription api class
    api = cris_client.DefaultApi(api_client=client)

    # Specify transcription properties by passing a dict to the properties parameter. See
    # https://docs.microsoft.com/azure/cognitive-services/speech-service/batch-transcription#configuration-properties
    # for supported parameters.
    properties = {
        "punctuationMode": "DictatedAndAutomatic",
        "profanityFilterMode": "Masked",
        "wordLevelTimestampsEnabled": True,
        "diarizationEnabled": True,
        "destinationContainerUrl": "<Your SAS URI to a the transcripts container where outputs are to be saved>", # TODO: Supply SAS URI
        "timeToLive": "PT1H"
    }
    
    # =========================================================================================
    # CHOOSE YOUR TRANSCRIPTION METHOD
    # =========================================================================================
    # Use base models for transcription. Comment this block if you are using a custom model.
    # transcription_definition = transcribe_from_single_blob(RECORDINGS_BLOB_URI, properties)

    # Uncomment this block to use custom models for transcription.
    # transcription_definition = transcribe_with_custom_model(api, RECORDINGS_BLOB_URI, properties)

    # Uncomment this block to transcribe all files from a container.
    transcription_definition = transcribe_from_container(RECORDINGS_CONTAINER_URI, properties)
    # =========================================================================================

    created_transcription, status, headers = api.create_transcription_with_http_info(
        transcription=transcription_definition)

    # get the transcription Id from the location URI
    transcription_id = headers["location"].split("/")[-1]

    # Log information about the created transcription. If you should ask for support, please
    # include this information.
    logging.info(
        f"Created new transcription with id '{transcription_id}' in region {SERVICE_REGION}")

    logging.info("Checking status.")

    completed = False

    while not completed:
        # wait for 5 seconds before refreshing the transcription status
        time.sleep(5)

        transcription = api.get_transcription(transcription_id)
        logging.info(f"Transcriptions status: {transcription.status}")

        if transcription.status in ("Failed", "Succeeded"):
            completed = True

        if transcription.status == "Succeeded":
            pag_files = api.get_transcription_files(transcription_id)
            for file_data in _paginate(api, pag_files):
                if file_data.kind != "Transcription":
                    continue

                audiofilename = file_data.name
                results_url = file_data.links.content_url
                results = requests.get(results_url)
                logging.info(
                    f"Results for {audiofilename}:\n{results.content.decode('utf-8')}")
        elif transcription.status == "Failed":
            logging.info(
                f"Transcription failed: {transcription.properties.error.message}")

if __name__ == "__main__":
    transcribe()
```

5. Run each of the four cells sequentially at least once to install the libraries and register your methods. Then simply call the `transcribe()` method by running the last snippet. You should see the output in the terminal as the process runs. You should see transcriptions in your output folder ('transcripts') in Azure.

### Not seeing the transcription saved in your container?
__Note:__ If you want the transcription saved into the `transcription` container, please ensure you specify the `"destinationContainerUrl": "<SAS URI to transcriptions container>"` in the `properties = {}` object inside the `transcribe()` function.

## Resources

- [Azure Batch Transcription using Python](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/samples/batch/python)
- [Installing pip library from GitHub (inline)](https://docs.databricks.com/libraries/notebooks-python-libraries.html#pip-install-vcs)
- [Installing pip library from GitHub Subdirectory Example (#6)](https://pip.pypa.io/en/stable/reference/pip_install/#examples)
- [Question: Installing Client Library in Databricks](https://forums.databricks.com/questions/39492/install-api-client-library-in-databricks.html)
