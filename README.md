# Azure Batch Transcription using Python through Databricks

## Outcome & Overview
Referencing a Blob Storage (in Azure) containing voice recordings, we want to be able to call the [Speech to Text Cognitive Service](https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/) in Azure to transcribe the respective recordings in parallel (batch), and save the transcript into another Blob Storage container.

## Setup

__Navigate to Azure Portal and create the following services under a common Resource Group.__
- Storage Account (with two Blob Storage containers named `recordings` and `transcriptions` for our input and output files respectively)
- Cognitive Services (Speech Service)

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

2. Create a new cell below and paste the below, carefully adding the keys and URLs copied earlier, into their respective variables:
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

__Note:__ If you want the transcription saved into the `transcription` container, you need to specify the `"destinationContainerUrl": "<SAS URI to transcriptions container>"` in the `properties = {}` object inside the `transcribe()` function.

## Resources

- [Azure Batch Transcription using Python](https://github.com/Azure-Samples/cognitive-services-speech-sdk/tree/master/samples/batch/python)
- [Installing pip library from GitHub (inline)](https://docs.databricks.com/libraries/notebooks-python-libraries.html#pip-install-vcs)
- [Installing pip library from GitHub Subdirectory Example (#6)](https://pip.pypa.io/en/stable/reference/pip_install/#examples)
- [Question: Installing Client Library in Databricks](https://forums.databricks.com/questions/39492/install-api-client-library-in-databricks.html)
