import vosk
import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import re
import json


with open("config.json", "r") as config:
    # print(config)
    text = config.read()
    config = json.loads(text)

HOTWORD = config["hotword"]



q = queue.Queue()

parser = argparse.ArgumentParser(add_help=False)



def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


samplerate = 44100



def listen():
    try:
        device_info = sd.query_devices(None, 'input')
        model = vosk.Model("model")

        with sd.RawInputStream(samplerate=samplerate, blocksize = 1000, device=None, dtype='int16',
                                channels=1, callback=callback):
                print('#' * 80)
                print('Press Ctrl+C to stop the recording')
                print('#' * 80)

                rec = vosk.KaldiRecognizer(model, samplerate)
                while True:
                    data = q.get()
                    if rec.AcceptWaveform(data):
                        # list of listened words, starts with "text"
                        match = re.findall(r"[^\"]*text|\"\"|\w+", rec.Result())
                        if HOTWORD in match:
                            return {"words" : match, "hotwordIndex" : match.index(HOTWORD)}

    except KeyboardInterrupt:
        print('\nDone')
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))


def main():
    listen()


if __name__ == '__main__':
    main()
