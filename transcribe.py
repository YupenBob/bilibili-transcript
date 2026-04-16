import sys
import json

model_name = sys.argv[1] if len(sys.argv) > 1 else "small"
audio_file = "audio.wav"

try:
    from faster_whisper import WhisperModel
    print(f"Loading faster-whisper model: {model_name}")
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    print(f"Transcribing {audio_file} with model={model_name}")
    segments, info = model.transcribe(audio_file, language="zh")
    full_text = "".join([seg.text for seg in segments])
    segment_list = []
    for seg in segments:
        segment_list.append({
            "start": seg.start,
            "end": seg.end,
            "text": seg.text
        })
    print(f"Done: {len(segment_list)} segments, {len(full_text)} chars")
    result = {"text": full_text, "segments": segment_list, "language": "zh"}
except Exception as e:
    print(f"faster-whisper failed: {e}, trying openai-whisper")
    import whisper
    model = whisper.load_model(model_name)
    print(f"Transcribing {audio_file} with model={model_name}")
    result = model.transcribe(audio_file, language="zh", verbose=False)
    full_text = result["text"]

with open("transcript_full.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

with open("transcript_segmented.txt", "w", encoding="utf-8") as f:
    for s in result.get("segments", []):
        start = s.get("start", 0)
        end = s.get("end", 0)
        text = s.get("text", "").strip() if isinstance(s, dict) else s.text.strip()
        f.write(f"[{start:.2f}s -> {end:.2f}s] {text}\n")

with open("transcript.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Files written: transcript_full.txt, transcript_segmented.txt, transcript.json")
