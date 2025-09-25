from TTS.api import TTS

# Setup
model_name = "tts_models/en/ljspeech/tacotron2-DDC"
output_path = "output_voice.wav"
text = "Hello, Josephine, Bryan loves you very much."

# Load model
tts = TTS(model_name=model_name)

# Synthesize and save
tts.tts_to_file(text=text, file_path=output_path)
print(f"✅ Voice output saved to {output_path}")
