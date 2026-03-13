#!/usr/bin/env python3
# 🎵 BGM 生成器 - PySynth 專業版

import os
import sys
import argparse

# 添加路徑
synth_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synths")
sys.path.insert(0, synth_path)

# 動態 import
def get_pysynth_func(name):
    module_name = f"pysynth_{name}"
    mod = __import__(module_name, fromlist=['make_wav'])
    return mod.make_wav

class BGMGenerator:
    """BGM 生成器 - PySynth 專業版"""
    
    # 支援的樂器
    INSTRUMENTS = {
        "piano": ("pysynth_b", "Acoustic Piano"),
        "rhodes": ("pysynth_e", "DX7 Rhodes Piano"),
        "strings": ("pysynth_c", "String/Pad"),
        "lead": ("pysynth_d", "Synth Lead"),
        "guitar": ("pysynth_s", "Guitar/Koto"),
    }
    
    # 經典和弦進行
    CHORD_PROGRESSIONS = {
        "pop": [("C", 4), ("G", 4), ("Am", 4), ("F", 4)],
        "ballad": [("Am", 4), ("F", 4), ("C", 4), ("G", 4)],
        "jazz": [("Dm7", 4), ("G7", 4), ("Cmaj7", 4), ("Dm7", 4)],
        "classical": [("C", 4), ("F", 4), ("G", 4), ("C", 4)],
        "chinese": [("C", 4), ("Em", 4), ("F", 4), ("G", 4)],
    }
    
    def __init__(self, 
                 genre="piano",
                 tempo=120,
                 duration=30,
                 output_dir="./output"):
        
        self.genre = genre
        self.tempo = tempo
        self.duration = duration
        self.output_dir = output_dir
        
        os.makedirs(output_dir, exist_ok=True)
    
    def _note_to_pysynth(self, chord):
        """和弦轉換為 PySynth 音符"""
        # 簡單轉換
        note_map = {
            "C": "c4", "D": "d4", "E": "e4", "F": "f4", 
            "G": "g4", "A": "a4", "B": "b4",
            "Am": "a3", "Dm": "d3", "Em": "e3", "Fm": "f3", "Gm": "g3",
            "Cmaj7": "c4", "Dm7": "d3", "G7": "g3",
        }
        return note_map.get(chord, "c4")
    
    def generate(self, instrument="piano"):
        """生成 BGM"""
        print(f"\n{'='*50}")
        print(f"🎵 BGM 生成器 - PySynth 專業版")
        print(f"{'='*50}")
        
        # 選擇樂器
        inst_module = {
            "piano": get_pysynth_func("b"),
            "rhodes": get_pysynth_func("e"),
            "strings": get_pysynth_func("c"),
            "lead": get_pysynth_func("d"),
            "guitar": get_pysynth_func("s"),
        }
        
        # 預設
        if instrument not in inst_module:
            instrument = "piano"
        
        make_wav = inst_module.get(instrument)
        
        # 選擇和弦進行
        progression = self.CHORD_PROGRESSIONS.get(self.genre, self.CHORD_PROGRESSIONS["pop"])
        
        # 構建歌曲
        song = []
        beats_per_chord = int(240 / self.tempo)  # 每個和弦的拍數
        
        # 重複和弦進行直到時長足夠
        repetitions = int(self.duration * self.tempo / 240) + 1
        
        for _ in range(repetitions):
            for chord in progression:
                note = self._note_to_pysynth(chord[0])
                song.append((note, chord[1]))
        
        # 截斷到目標時長
        song = song[:len(song)//2]  # 簡單截斷
        
        print(f"樂器: {instrument}")
        print(f"和弦: {progression}")
        print(f"音符數: {len(song)}")
        
        # 生成 WAV
        filename = f"bgm_{instrument}_{self.tempo}bpm_{self.duration}s.wav"
        output_path = os.path.join(self.output_dir, filename)
        
        print("🎹 生成中...")
        make_wav(song, fn=output_path, bpm=self.tempo, silent=True)
        
        print(f"✅ 完成: {output_path}")
        
        # 轉 MP3
        mp3_path = output_path.replace(".wav", ".mp3")
        ffmpeg = os.path.expanduser("~/.openclaw/ai-operator/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2")
        
        if os.path.exists(ffmpeg):
            import subprocess
            subprocess.run([
                ffmpeg, "-i", output_path,
                "-acodec", "libmp3lame", "-q:a", "2",
                "-y", mp3_path
            ], capture_output=True)
            print(f"✅ MP3: {mp3_path}")
            return mp3_path
        
        return output_path


def main():
    parser = argparse.ArgumentParser(description="BGM 生成器 - PySynth 專業版")
    parser.add_argument("--instrument", "-i", 
                       default="piano",
                       choices=["piano", "rhodes", "strings", "lead", "guitar"])
    parser.add_argument("--genre", "-g", 
                       default="pop",
                       choices=["pop", "ballad", "jazz", "classical", "chinese"])
    parser.add_argument("--tempo", "-t", type=int, default=120)
    parser.add_argument("--duration", "-d", type=int, default=30)
    parser.add_argument("--output", "-o", default="./output")
    
    args = parser.parse_args()
    
    gen = BGMGenerator(
        genre=args.genre,
        tempo=args.tempo,
        duration=args.duration,
        output_dir=args.output
    )
    
    result = gen.generate(args.instrument)
    print(f"\n📁 輸出: {result}")


if __name__ == "__main__":
    main()
