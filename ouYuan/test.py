# _*_ coding : utf-8 _*_
# @Time : 2023-04-08 16:48
# @Author : Kmoon_Hs
# @File : test


import pyaudio
import wave

import requests as requests


def start_audio(time = 5,save_file="test.wav"):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 16000
	RECORD_SECONDS = time  #需要录制的时间
	WAVE_OUTPUT_FILENAME = save_file	#保存的文件名

	p = pyaudio.PyAudio()	#初始化
	print("ON")

	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)#创建录音文件
	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)#开始录音

	print("OFF")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')	#保存
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

# start_audio()

from fastapi import FastAPI,UploadFile,File
from typing import List

app=FastAPI()


async def save_files(files):
	for file in files:
		"type:<class 'coroutine'>"
		cont=await file.read()
		with open(f'myfiles/{file.filename}','wb') as f:
			f.write(cont)
	return 'success'

@app.post('/',summary='上传文件')
async def upload_files(files:List[UploadFile]=File(...)):
	return await save_files(files)

if __name__ == '__main__':
	import uvicorn
	uvicorn.run('test:app',host='127.0.0.1',port=8999)
