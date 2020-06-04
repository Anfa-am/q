import q
import main
import json
import asyncio
import websockets
import wave
import time
import noisereduce as nr
import numpy as np
import samplerate as sr
from pyaudio import PyAudio, Stream, paInt16
from contextlib import asynccontextmanager, contextmanager, AsyncExitStack
from typing import AsyncGenerator, Generator
from threading import Thread
import engines.blockout

server = 'localhost:2700'
loop = asyncio.get_event_loop()
listening = True
recording = True

denoiser = engines.blockout.RNNoise()
resampler = sr.Resampler()

def listen1():
    global recording
    while True:
        try:
            user_input = input("Type something to begin...\n")

            if(user_input == 'start'):
                recording = True
                start()

            if(user_input == 'stop'):
                print('stopping')
                recording = False
            # main.hear(user_input)

        except (KeyboardInterrupt, EOFError, SystemExit):
            break

@contextmanager
def _pyaudio() -> Generator[PyAudio, None, None]:
    p = PyAudio()
    try:
        yield p
    finally:
        p.terminate()

@contextmanager
def _pyaudio_open_stream(p: PyAudio, *args, **kwargs) -> Generator[Stream, None, None]:
    p.input_device_index = 0
    s = p.open(*args, **kwargs)
    try:
        yield s
    finally:
        s.close()

@asynccontextmanager
async def _polite_websocket(ws: websockets.WebSocketClientProtocol) -> AsyncGenerator[websockets.WebSocketClientProtocol, None]:
    try:
        yield ws
    finally:
        await ws.send('{"eof" : 1}')
        print(await ws.recv())

async def transcribe(uri):
    async with AsyncExitStack() as stack:
        global recording
        ws = await stack.enter_async_context(websockets.connect(uri))
        ws = await stack.enter_async_context(_polite_websocket(ws))
        pi = _pyaudio()
        p = stack.enter_context(pi)
        s = stack.enter_context(_pyaudio_open_stream(p,
            format = paInt16, 
            channels = 1,
            rate = 48000,
            input = True, 
            frames_per_buffer = 480))

        frames = []

        while listening:
            data = s.read(480)

            if len(data) == 0:
                break

            denoised_data = denoiser.process_frame(data)
            asr_prep = np.fromstring(denoised_data, dtype=np.int16)
            for_stt = resampler.process(asr_prep, (16000/48000)).tobytes()

            await ws.send(for_stt)
            print(await ws.recv())

            frames.append(for_stt)

            if(recording == False):
                print('stopping')

                wf = wave.open('./me.wav', 'w')
                wf.setnchannels(1)
                wf.setsampwidth(p.get_sample_size(paInt16))
                wf.setframerate(16000)
                wf.writeframes(b''.join(frames))
                wf.close()

                stop_listen()

def stop_listen():
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

def listen():
    try:
        loop.run_until_complete(transcribe(f'ws://' + server))
    except (Exception, KeyboardInterrupt) as e:
        print(e)
        stop_listen()

def start(): 
    hearing = Thread(target = listen)
    hearing.setDaemon(True)

    hearing1 = Thread(target = listen1)
    hearing1.setDaemon(True)

    hearing.start()
    hearing1.start()

    while True:
        time.sleep(0.01)
        pass

if __name__ == "engines.listen":
    print('listening')
    start()
    
