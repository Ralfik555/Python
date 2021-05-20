import io
import os
import sys
import time
from pydub import AudioSegment
from google.cloud import speech_v1p1beta1 as speech #Changed
from google.cloud.speech_v1p1beta1 import SpeakerDiarizationConfig
#from google.cloud.speech_v1p1beta1 import enums #Changed
from google.cloud.speech_v1p1beta1 import types #Changed
import wave
from google.cloud import storage
from convert import frame_rate_channel, stereo_to_mono
from upload import upload_blob


def google_transcribe(audio_file_name):


    frame_rate, channels = frame_rate_channel(audio_file_name)
    
    if channels > 1:
        stereo_to_mono(audio_file_name)
    
    bucket_name = 'clubhouse_audios'
    source_file_name = audio_file_name
    destination_blob_name = 'firstTest.wav'
    
    upload_blob(bucket_name, source_file_name, destination_blob_name)
    
    gcs_uri = 'gs://' + bucket_name + '/' + destination_blob_name
    transcript = ''
    
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)

    # config = types.RecognitionConfig(
    #     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=frame_rate,
    #     language_code='en-US',
    #     enable_speaker_diarization=True,
    #     diarization_speaker_count=2) #Changed

    # config = speech.RecognitionConfig(
    #     encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    #     sample_rate_hertz=frame_rate,
    #     language_code='en-US',
    #     enable_speaker_diarization=True,
    #     diarization_speaker_count=5,
    # )

    diarization_config = SpeakerDiarizationConfig(enable_speaker_diarization = True,min_speaker_count = 3, max_speaker_count = 5)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        language_code='en-US',
        #enable_speaker_diarization=True,
        #diarization_speaker_count=5,
        diarization_config = diarization_config
    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config = config, audio = audio)
    #response = operation.result(timeout=10000)
    response = operation.result(timeout=None)
    result = response.results[-1] #Changed
    words_info = result.alternatives[0].words #Changed
    
    tag=1 #Changed
    speaker="" #Changed
    start = ""
    end = ""
    time_list =[]


    # for word_info in words_info: #Changed
    #     if word_info.speaker_tag==tag: #Changed
    #         speaker=speaker+" "+word_info.word #Changed
    #     else: #Changed
    #         transcript += "speaker {}: {}".format(tag,speaker) + '\n' #Changed
    #         tag=word_info.speaker_tag #Changed
    #         speaker=""+word_info.word #Changed
 
    # transcript += "speaker {}: {}".format(tag,speaker) #Changed
    
    # #delete_blob(bucket_name, destination_blob_name)
    # return transcript

    for word_info in words_info: #Changed
        if word_info.speaker_tag==tag: #Changed
            speaker=speaker+" "+word_info.word #Changed
            start = str(word_info.start_time)[0:7]
            end = str(word_info.end_time)[0:7]
            time_list.append(start)
            time_list.append(end)
        else: #Changed
            if len(time_list) == 0:
                time_list.append("0s")
                time_list.append("0s")
            transcript += "speaker {} {} - {}: {}".format(tag,time_list[0],time_list[-1],speaker) + '\n' #Changed
            tag=word_info.speaker_tag #Changed
            speaker=""+word_info.word #Changed
            time_list = []
            time_list.append(start)
            time_list.append(end)
 
    transcript += "speaker {} {} - {}: {}".format(tag,time_list[0],time_list[-1],speaker) + '\n' #Changed
    
    #delete_blob(bucket_name, destination_blob_name)
    return transcript



file = '/home/ralfik555/Desktop/G_transcript/test_audio.wav'

sys.stdout = open("test_audio.txt", "w")
start_time = time.time()
print(google_transcribe(file))
print("--- %s seconds ---" % (time.time() - start_time))
sys.stdout.close()