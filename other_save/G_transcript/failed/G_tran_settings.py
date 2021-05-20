 
#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the REST API for batch
processing.
Example usage:
    python transcribe.py resources/audio.raw
    python transcribe.py gs://cloud-samples-tests/speech/brooklyn.flac
"""

import argparse


# [START speech_transcribe_sync]
def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech_v1p1beta1 as speech
    #from google.cloud import speech
    import io
    import sys
    import json
    from oauth2client.service_account import ServiceAccountCredentials

    # with open('/home/ralfik555/Desktop/G_transcript/key.json') as f:
    #     data_cred = json.load(f)

    # credentials = ServiceAccountCredentials.from_json_keyfile_dict(data_cred)


    client = speech.SpeechClient()


    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        enable_speaker_diarization= True,
        diarization_speaker_count= 5,
        sample_rate_hertz=48000,
        language_code="en-US",
        audio_channel_count = 2
    )
    # [END speech_python_migration_config]

    # [START speech_python_migration_sync_response]
    response = client.recognize(config=config, audio=audio)

    # [END speech_python_migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.

    sys.stdout = open("save.txt", "w")
    
    #print(u"Transcript: {}".format(response.results[0].alternatives[0].transcript))


    for w in response.results[0].alternatives[0].words:
        print("{} : {}".format(w.speaker_tag, w.word))

    # for result in response.results:
    #     # The first alternative is the most likely one for this portion.
    #     print(u"Transcript: {}".format(result.alternatives[0].transcript))

    sys.stdout.close()  




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("path", help="File or GCS path for audio file to be recognized")
    args = parser.parse_args()
    transcribe_file(args.path)