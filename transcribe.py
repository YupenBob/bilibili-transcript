import sys
import json

model_name = sys.argv[1] if len(sys.argv) > 1 else "small"

try:
    from faster_whisper import WhisperModel
    print(f"Loading faster-whisper model: {model_name}")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    print(f"Transcribing audio.wav with model={model_name}")
    result = model.transcribe("audio.wav", language="zh")
except Exception as e:
    print(f"faster-whisper failed: {e}, trying openai-whisper")
    import whisper
    model = whisper.load_model(model_name)
    print(f"Transcribing audio.wav with model={model_name}")
    result = model.transcribe("audio.wav", language="zh", verbose=False)

with open("transcript_full.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

segments = result.get("segments", [])
with open("transcript_segmented.txt", "w", encoding="utf-8") as f:
    for s in segments:
        start = s.get("start", 0)
        end = s.get("end", 0)
        text = s.get("text", "").strip()
        f.write(f"[{start:.2f}s -> {end:.2f}s] {text}\n")

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Done: {len(segments)} segments, {len(result['text'])} chars")
