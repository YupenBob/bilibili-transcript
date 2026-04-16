import whisper
import json
import sys

model = whisper.load_model(sys.argv[1] if len(sys.argv) > 1 else "base")
result = model.transcribe("audio.wav", language="zh", verbose=False)

with open("transcript_full.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

segments = result.get("segments", [])
with open("transcript_segmented.txt", "w", encoding="utf-8") as f:
    for seg in segments:
        start = seg.get("start", 0)
        end = seg.get("end", 0)
        text = seg.get("text", "").strip()
        f.write(f"[{start:.2f}s -> {end:.2f}s] {text}\n")

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Done: {len(segments)} segments")
