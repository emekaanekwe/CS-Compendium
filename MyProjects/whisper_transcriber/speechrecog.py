"""  The model can be used with the pipeline class to transcribe audios of arbitrary length:
"""

import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

'''Transcibe FIT5201 Lecture with Strong Chinese Accent'''
# Initialize empty string to hold the transcribed lecture
lecture = "AI/Personal_Projects/whisper_transcriber/ml81.mp3"
transcribed_lecture = pipe(lecture, return_timestamps=True, generate_kwargs={
    "language": "english", 
    "task": "transcribe", 
    "temperature": 0.0, 
    "no_speech_threshold": 0.6})  
# temprature at 0 makes it more deterministic
# no_speech_threshold helps with pauses in speech

'''exapmple usage'''
#dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
#sample = dataset[0]["audio"]

#result = pipe(sample)
#print(result["text"])
