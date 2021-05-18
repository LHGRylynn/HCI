import random
import time
import win32api
import speech_recognition as sr

## speech recognition
def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_sphinx(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


##  turning up/down the volume of the windows system
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

def turnUp():
    vl = volume.GetMasterVolumeLevel()
    if(vl<-32):
        volume.SetMasterVolumeLevel(-30, None)
    elif(vl<-20):
        volume.SetMasterVolumeLevel(-19, None)
    elif(vl<-15):
        volume.SetMasterVolumeLevel(-14, None)
    elif(vl<-9):
        volume.SetMasterVolumeLevel(-8, None)
    elif(vl<-4):
        volume.SetMasterVolumeLevel(-3, None)
    else:
        volume.SetMasterVolumeLevel(0, None)

def turnDown():
    vl = volume.GetMasterVolumeLevel()
    if(vl>-2):
        volume.SetMasterVolumeLevel(-3, None)
    elif(vl>-8):
        volume.SetMasterVolumeLevel(-9, None)
    elif(vl>-12):
        volume.SetMasterVolumeLevel(-15, None)
    elif(vl>-22):
        volume.SetMasterVolumeLevel(-33, None)
    else:
        volume.SetMasterVolumeLevel(-65, None)
