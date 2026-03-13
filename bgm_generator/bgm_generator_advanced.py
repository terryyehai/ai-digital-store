#!/usr/bin/env python3
# 🎵 進階 BGM 生成器 - 專業版
# 包含：結構化生成 + 旋律生成 + 動態編曲

import os
import sys
import random
import argparse

synth_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "synths")
sys.path.insert(0, synth_path)

def get_pysynth_func(name):
    module_name = f"pysynth_{name}"
    mod = __import__(module_name, fromlist=['make_wav'])
    return mod.make_wav


class MusicComposer:
    """音樂創作引擎"""
    
    # 音階音符
    SCALES = {
        "C_major": ["c", "d", "e", "f", "g", "a", "b"],
        "A_minor": ["a", "b", "c", "d", "e", "f", "g"],
    }
    
    # 和弦進行庫
    CHORD_PROGRESSIONS = {
        # Pop
        "pop_1": [("C", 4), ("G", 4), ("Am", 4), ("F", 4)],  # I-V-vi-IV
        "pop_2": [("Am", 4), ("F", 4), ("C", 4), ("G", 4)],  # vi-IV-I-V
        "pop_3": [("C", 4), ("Am", 4), ("F", 4), ("G", 4)],  # I-vi-IV-V
        
        # Jazz
        "jazz_1": [("Dm7", 4), ("G7", 4), ("Cmaj7", 4), ("Dm7", 4)],
        "jazz_2": [("Cmaj7", 4), ("Am7", 4), ("Dm7", 4), ("G7", 4)],
        
        # Classical
        "classical_1": [("C", 4), ("F", 4), ("G", 4), ("C", 4)],
        "classical_2": [("Am", 4), ("Dm", 4), ("E", 4), ("Am", 4)],
        
        # Chinese
        "chinese_1": [("C", 4), ("Em", 4), ("F", 4), ("G", 4)],
        "chinese_2": [("Am", 4), ("Em", 4), ("F", 4), ("G", 4)],
    }
    
    # 歌曲結構
    SONG_STRUCTURES = {
        "simple": ["verse", "chorus", "verse", "chorus", "chorus"],
        "full": ["intro", "verse", "pre_chorus", "chorus", "verse", "chorus", "bridge", "chorus", "outro"],
        "classic": ["verse", "chorus", "verse", "chorus", "bridge", "chorus"],
        "electronic": ["intro", "build", "drop", "build", "drop", "outro"],
    }
    
    # 旋律類型
    MELODY_TYPES = {
        "simple": [0, 0, 2, 4],  # 級進
        "jump": [0, 4, 2, 7],     # 跳躍
        "wave": [0, 2, 4, 2, 0], # 波浪
        "arpeggio": [0, 4, 7, 12], # 琶音
    }
    
    def __init__(self, key="C", tempo=120, style="pop"):
        self.key = key
        self.tempo = tempo
        self.style = style
        self.scale = self.SCALES.get(f"{key}_major", ["c", "d", "e", "f", "g", "a", "b"])
    
    def chord_to_notes(self, chord):
        """和弦轉換為音符"""
        chord_map = {
            "C": ["c", "e", "g"], "Dm": ["d", "f", "a"], "Em": ["e", "g", "b"],
            "F": ["f", "a", "c"], "G": ["g", "b", "d"], "Am": ["a", "c", "e"],
            "Bdim": ["b", "d", "f"],
            "Cmaj7": ["c", "e", "g", "b"], "Dm7": ["d", "f", "a", "c"],
            "G7": ["g", "b", "d", "f"], "Am7": ["a", "c", "e", "g"],
        }
        return chord_map.get(chord, ["c", "e", "g"])
    
    def generate_melody_note(self, chord_notes, melody_type, octave=4):
        """根據和弦生成旋律音符"""
        pattern = self.MELODY_TYPES.get(melody_type, [0, 2, 4])
        note_idx = random.choice(pattern)
        note_idx = note_idx % len(chord_notes)
        
        note = chord_notes[note_idx]
        
        # 隨機八度變化
        if random.random() > 0.7:
            octave_offset = random.choice([-1, 1])
            octave += octave_offset
        
        return f"{note}{octave}"
    
    def generate_section(self, section_type, chords, melody_type="simple", length=4):
        """生成一個段落"""
        song = []
        
        # 段落專用參數
        section_params = {
            "intro": {"octave": 3, "volume": 0.8, "melody": "simple"},
            "verse": {"octave": 4, "volume": 1.0, "melody": "simple"},
            "pre_chorus": {"octave": 4, "volume": 1.1, "melody": "jump"},
            "chorus": {"octave": 5, "volume": 1.2, "melody": "jump"},
            "bridge": {"octave": 4, "volume": 1.0, "melody": "wave"},
            "outro": {"octave": 3, "volume": 0.7, "melody": "simple"},
            "build": {"octave": 4, "volume": 1.0, "melody": "arpeggio"},
            "drop": {"octave": 5, "volume": 1.3, "melody": "jump"},
        }
        
        params = section_params.get(section_type, {"octave": 4, "volume": 1.0, "melody": "simple"})
        
        # 每個和弦重複
        for _ in range(length):
            for chord, beat in chords:
                chord_notes = self.chord_to_notes(chord)
                
                # 生成旋律音符
                melody_note = self.generate_melody_note(chord_notes, params["melody"], params["octave"])
                
                # 節奏變化
                note_value = beat
                if section_type in ["build", "drop"]:
                    note_value = max(2, beat - 2)  # 更快
                
                song.append((melody_note, note_value))
        
        return song
    
    def create_song(self, structure="full", progression="pop_1"):
        """創建完整歌曲"""
        # 獲取和弦進行
        chords = self.CHORD_PROGRESSIONS.get(progression, self.CHORD_PROGRESSIONS["pop_1"])
        
        # 獲取結構
        structure_template = self.SONG_STRUCTURES.get(structure, self.SONG_STRUCTURES["simple"])
        
        # 根據段落類型調整長度
        section_lengths = {
            "intro": 2,
            "verse": 4,
            "pre_chorus": 2,
            "chorus": 4,
            "bridge": 2,
            "outro": 2,
            "build": 2,
            "drop": 4,
        }
        
        full_song = []
        
        for section in structure_template:
            length = section_lengths.get(section, 4)
            section_song = self.generate_section(section, chords, length=length)
            full_song.extend(section_song)
        
        return full_song


class AdvancedBGMGenerator:
    """進階 BGM 生成器"""
    
    INSTRUMENTS = {
        "piano": ("b", "Acoustic Piano"),
        "rhodes": ("e", "DX7 Rhodes"),
        "strings": ("c", "String/Pad"),
        "lead": ("d", "Synth Lead"),
        "guitar": ("s", "Guitar/Koto"),
    }
    
    STYLES = {
        "pop": {"progression": "pop_1", "structure": "full", "tempo": 120},
        "ballad": {"progression": "classical_2", "structure": "classic", "tempo": 80},
        "jazz": {"progression": "jazz_1", "structure": "simple", "tempo": 100},
        "electronic": {"progression": "pop_1", "structure": "electronic", "tempo": 128},
        "classical": {"progression": "classical_1", "structure": "full", "tempo": 90},
        "chinese": {"progression": "chinese_1", "structure": "classic", "tempo": 70},
    }
    
    def __init__(self, style="pop", tempo=None, instrument="piano", 
                 key="C", structure=None, output_dir="./output"):
        
        self.style = style
        self.instrument = instrument
        self.key = key
        
        # 獲取風格參數
        style_params = self.STYLES.get(style, self.STYLES["pop"])
        self.progression = style_params["progression"]
        self.structure = structure or style_params["structure"]
        self.tempo = tempo or style_params["tempo"]
        
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate(self):
        """生成 BGM"""
        print(f"\n{'='*50}")
        print(f"🎵 進階 BGM 生成器")
        print(f"{'='*50}")
        print(f"風格: {self.style}")
        print(f"樂器: {self.instrument}")
        print(f"結構: {self.structure}")
        print(f"調性: {self.key}")
        print(f"BPM: {self.tempo}")
        
        # 創作曲作者
        composer = MusicComposer(key=self.key, tempo=self.tempo, style=self.style)
        
        # 生成旋律
        print("\n🎼 生成旋律...")
        song = composer.create_song(structure=self.structure, progression=self.progression)
        
        print(f"音符數: {len(song)}")
        
        # 獲取樂器
        inst_code = self.INSTRUMENTS.get(self.instrument, ("b", "Piano"))
        make_wav = get_pysynth_func(inst_code[0])
        
        # 生成音頻
        filename = f"bgm_{self.style}_{self.instrument}_{self.tempo}bpm.wav"
        output_path = os.path.join(self.output_dir, filename)
        
        print("🎹 生成音頻...")
        make_wav(song, fn=output_path, bpm=self.tempo, silent=True)
        
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
            print(f"✅ 完成: {mp3_path}")
            return mp3_path
        
        return output_path


def main():
    parser = argparse.ArgumentParser(description="進階 BGM 生成器")
    
    parser.add_argument("--style", "-s",
                       default="pop",
                       choices=["pop", "ballad", "jazz", "electronic", "classical", "chinese"])
    parser.add_argument("--instrument", "-i",
                       default="piano",
                       choices=["piano", "rhodes", "strings", "lead", "guitar"])
    parser.add_argument("--tempo", "-t", type=int, default=None)
    parser.add_argument("--key", "-k", default="C")
    parser.add_argument("--structure", "-st", default=None)
    parser.add_argument("--duration", "-d", type=int, default=30)
    parser.add_argument("--output", "-o", default="./output")
    
    args = parser.parse_args()
    
    gen = AdvancedBGMGenerator(
        style=args.style,
        instrument=args.instrument,
        tempo=args.tempo,
        key=args.key,
        structure=args.structure,
        output_dir=args.output
    )
    
    result = gen.generate()
    print(f"\n📁 輸出: {result}")


if __name__ == "__main__":
    main()
