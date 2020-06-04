import sys
import asyncio
import pathlib
import websockets
import concurrent.futures
from vosk import Model, KaldiRecognizer, SpkModel

model = Model("/opt/kaldi-en/model/mmmh/")
speak = SpkModel("/opt/kaldi-en/spk/")
pool = concurrent.futures.ThreadPoolExecutor()
loop = asyncio.get_event_loop()
rec = KaldiRecognizer(model, speak, 16000);


def process_chunk(rec, message):
    if message == '{"eof" : 1}':
        return rec.FinalResult(), True
    elif rec.AcceptWaveform(message):
        return rec.Result(), False
    else:
        return rec.PartialResult(), False

async def recognize(websocket, path):
    while True:
        message = await websocket.recv()
        response, stop = await loop.run_in_executor(pool, process_chunk, rec, message)
        await websocket.send(response)
        if stop: 
            break

start_server = websockets.serve(recognize, '0.0.0.0', 2700)

loop.run_until_complete(start_server)
loop.run_forever()
