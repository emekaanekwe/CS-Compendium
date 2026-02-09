import whisper
import json  # Added for debugging

# Load model
model = whisper.load_model("large-v3")
lecture = "AI/Personal_Projects/whisper_transcriber/ml81.mp3"

# Transcribe with accent optimization
transcribed_lecture = model.transcribe(
    lecture,
    language="english",
    task="transcribe",
    temperature=0.0,
    fp16=False,
    verbose=True
)

# DEBUG: Check what's in the result
print(f"Type of transcribed_lecture: {type(transcribed_lecture)}")
print(f"Keys in transcribed_lecture: {list(transcribed_lecture.keys())}")

# Fix 1: Safely extract text
if isinstance(transcribed_lecture, dict):
    # If it's a dictionary, try different possible keys
    if "text" in transcribed_lecture:
        text_content = transcribed_lecture["text"]
    elif "transcription" in transcribed_lecture:
        text_content = transcribed_lecture["transcription"]
    else:
        # Try to get first value that looks like text
        for key, value in transcribed_lecture.items():
            if isinstance(value, str) and len(value) > 10:
                text_content = value
                break
        else:
            text_content = str(transcribed_lecture)
elif isinstance(transcribed_lecture, str):
    text_content = transcribed_lecture
else:
    # If it's a list or something else
    text_content = str(transcribed_lecture)

# Convert to string if it's a list
if isinstance(text_content, list):
    # Join list elements with spaces
    text_content = " ".join(str(item) for item in text_content if item)
elif not isinstance(text_content, str):
    text_content = str(text_content)

# Save result
with open("ml_8_1.txt", "w") as f:
    f.write(text_content)  # Now guaranteed to be a string

# Save raw result for debugging
with open("transcript_debug.json", "w") as f:
    json.dump(transcribed_lecture, f, indent=2, default=str)

# Handle segments - check if they exist and are in expected format
if "segments" in transcribed_lecture and transcribed_lecture["segments"]:
    print("\nTimestamps:")
    for segment in transcribed_lecture["segments"]:
        if isinstance(segment, dict) and "start" in segment and "end" in segment and "text" in segment:
            print(f"{segment['start']:.2f}s - {segment['end']:.2f}s: {segment['text']}")
        else:
            print(f"Segment format unexpected: {segment}")
else:
    print("No segments found in result")

print(f"\nTranscription saved to transcript.txt")
print(f"Debug info saved to transcript_debug.json")