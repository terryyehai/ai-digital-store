#!/usr/bin/env python3
# 🎵 專業 BGM 生成器 - 精簡穩定版
# Professional BGM Generator

import os
import sys
import argparse
import numpy as np
from scipy.io import wavfile
import subprocess

# 添加路徑
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rhythm.rhythm_patterns import RhythmFactory
from synths.sound_synthesizer import InstrumentSounds, ChineseInstruments


class BGMGenerator:
    """專業 BGM 生成器"""
    
    # 和弦進行庫
    CHORD_PROGRESSIONS = {
        "pop": [["I", "V", "vi", "IV"], ["I", "IV", "V", "I"], ["I", "vi", "IV", "V"]],
        "electronic": [["I", "V", "vi", "IV"], ["i", "VII", "VI", "v"], ["I", "bVII", "IV", "I"]],
        "ambient": [["I", "IV", "I", "V"], ["i", "v", "i", "iv"], ["I", "iii", "IV", "V"]],
        "jazz": [["ii7", "V7", "Imaj7"], ["Imaj7", "vi7", "ii7", "V7"]],
        "funk": [["I7", "IV7", "I7", "V7"], ["ii7", "V7", "Imaj7", "IV7"]],
        "rock": [["I", "V", "vi", "IV"], ["I", "IV", "V", "I"]],
        "ballad": [["I", "vi", "IV", "V"], ["i", "VI", "iv", "V"]],
        # 中國風
        "chinese": [["I", "V", "vi", "IV"], ["I", "vi", "IV", "V"], ["I", "IV", "V", "vi"]],
        "chinese_classical": [["I", "IV", "V", "I"], ["i", "iv", "V", "i"]],
    }
    
    # 調性對應
    KEY_NOTES = {
        "C": ["C", "D", "E", "F", "G", "A", "B"],
        "G": ["G", "A", "B", "C", "D", "E", "F#"],
        "D": ["D", "E", "F#", "G", "A", "B", "C#"],
        "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
        "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
        "Am": ["A", "B", "C", "D", "E", "F", "G"],
        "Em": ["E", "F#", "G", "A", "B", "C", "D"],
    }
    
    def __init__(self, genre="electronic", mood="energetic", tempo=120, 
                 duration=30, key="C", output_dir="./output"):
        
        self.genre = genre
        self.mood = mood
        self.tempo = tempo
        self.duration = duration
        self.key = key
        self.output_dir = output_dir
        
        self.sample_rate = 44100
        # 根據曲風選擇節奏
        if genre in ["chinese", "chinese_classical"]:
            rhythm_pattern = "ambient"  # 中國風用輕柔節奏
        else:
            rhythm_pattern = genre
        self.pattern = RhythmFactory.get_pattern(rhythm_pattern)()
        self.instruments = InstrumentSounds()
        self.chinese = ChineseInstruments()
        
        # 選擇和弦進行
        progressions = self.CHORD_PROGRESSIONS.get(genre, self.CHORD_PROGRESSIONS["pop"])
        self.chord_prog = progressions[0]
        
        os.makedirs(output_dir, exist_ok=True)
    
    def _get_chord_notes(self, chord):
        """和弦轉音符"""
        # Major 和弦
        major = {"I": 0, "II": 2, "III": 4, "IV": 5, "V": 7, "VI": 9, "VII": 11}
        # Minor 和弦
        minor = {"i": 0, "ii": 2, "iii": 3, "iv": 5, "v": 7, "vi": 8, "vii": 10}
        
        base = chord.replace("7", "").replace("maj", "").replace("m", "")
        
        if chord.islower() or "m" in chord:
            offset = minor.get(base, 0)
            notes = [offset, offset + 4, offset + 7]
        else:
            offset = major.get(base, 0)
            notes = [offset, offset + 4, offset + 7]
        
        # 轉換為實際音符（簡化版）
        return notes
    
    def generate_drums(self):
        """生成鼓組"""
        print("🥁 生成鼓組...")
        
        total_samples = int(self.sample_rate * self.duration)
        drums = np.zeros(total_samples, dtype=np.float32)
        
        total_beats = int(self.tempo * self.duration / 60)
        
        for instrument, pattern in self.pattern.items():
            expanded = (pattern * (total_beats // len(pattern) + 1))[:total_beats]
            
            for beat_idx, trigger in enumerate(expanded):
                if trigger:
                    beat_time = beat_idx * 60.0 / self.tempo
                    
                    if instrument == "kick":
                        sample = self.instruments.kick()
                    elif instrument == "snare":
                        sample = self.instruments.snare()
                    elif instrument == "hihat":
                        sample = self.instruments.hihat()
                    elif instrument == "clap":
                        sample = self.instruments.clap()
                    elif instrument == "tom":
                        sample = self.instruments.tom()
                    else:
                        continue
                    
                    start = int(beat_time * self.sample_rate)
                    end = min(start + len(sample), total_samples)
                    if start < total_samples:
                        drums[start:end] += sample[:end-start]
        
        # 標準化
        drums = drums / np.max(np.abs(drums) + 1e-8) * 0.8
        return drums
    
    def generate_bass(self):
        """生成貝斯"""
        print("🎸 生成貝斯...")
        
        total_samples = int(self.sample_rate * self.duration)
        bass = np.zeros(total_samples, dtype=np.float32)
        
        beats_per_chord = (self.tempo * self.duration / 60) / len(self.chord_prog)
        
        for i, chord in enumerate(self.chord_prog):
            chord_notes = self._get_chord_notes(chord)
            root = chord_notes[0]
            
            # 根音頻率
            base_freq = 55 * (2 ** (root / 12))
            
            for beat in range(int(beats_per_chord)):
                beat_time = i * beats_per_chord * 60.0 / self.tempo + beat * 60.0 / self.tempo
                
                # 貝斯音符
                note_duration = 0.3
                sample = self.instruments.bass_synth(f"C{root // 12 + 2}", note_duration)
                
                start = int(beat_time * self.sample_rate)
                end = min(start + len(sample), total_samples)
                if start < total_samples:
                    bass[start:end] += sample[:end-start]
        
        bass = bass / np.max(np.abs(bass) + 1e-8) * 0.7
        return bass
    
    def generate_chords(self):
        """生成和弦墊"""
        print("🎹 生成和弦...")
        
        total_samples = int(self.sample_rate * self.duration)
        chords = np.zeros(total_samples, dtype=np.float32)
        
        beats_per_chord = (self.tempo * self.duration / 60) / len(self.chord_prog)
        chord_duration = beats_per_chord * 60.0 / self.tempo
        
        for i, chord in enumerate(self.chord_prog):
            chord_notes = self._get_chord_notes(chord)
            chord_time = i * chord_duration
            
            # 選擇音色 - 中國風使用古箏
            if self.genre in ["chinese", "chinese_classical"]:
                play_func = self.chinese.guzheng
            elif self.genre == "ambient":
                play_func = self.instruments.pad_ambient
            else:
                play_func = self.instruments.strings
            
            # 每個和弦音
            for j, note_offset in enumerate(chord_notes):
                base_freq = 220 * (2 ** (note_offset / 12))
                note_name = f"C{note_offset // 12 + 4}"
                
                sample = play_func(note_name, chord_duration * 0.9)
                
                start = int(chord_time * self.sample_rate)
                end = min(start + len(sample), total_samples)
                if start < total_samples:
                    chords[start:end] += sample[:end-start] * 0.2
        
        chords = chords / np.max(np.abs(chords) + 1e-8) * 0.5
        return chords
    
    def generate_melody(self):
        """生成旋律"""
        print("🎵 生成旋律...")
        
        total_samples = int(self.sample_rate * self.duration)
        melody = np.zeros(total_samples, dtype=np.float32)
        
        beats_per_chord = (self.tempo * self.duration / 60) / len(self.chord_prog)
        
        # 中國風樂器選擇
        chinese_instruments = {
            "guzheng": self.chinese.guzheng,
            "dizi": self.chinese.dizi,
            "erhu": self.chinese.erhu,
            "pipa": self.chinese.pipa,
            "yangqin": self.chinese.yangqin,
        }
        
        for i, chord in enumerate(self.chord_prog):
            chord_notes = self._get_chord_notes(chord)
            note_offset = chord_notes[i % len(chord_notes)]
            
            chord_time = i * beats_per_chord * 60.0 / self.tempo
            note_name = f"C{(note_offset // 12) + 5}"
            
            # 根據曲風選擇樂器
            if self.genre in ["chinese", "chinese_classical"]:
                # 輪流使用不同中國樂器
                inst_key = list(chinese_instruments.keys())[i % len(chinese_instruments)]
                play_func = chinese_instruments[inst_key]
                sample = play_func(note_name, beats_per_chord * 60.0 / self.tempo * 0.8)
            elif self.genre == "electronic":
                sample = self.instruments.synth_lead(note_name, beats_per_chord * 60.0 / self.tempo * 0.6)
            elif self.genre == "ambient":
                sample = self.instruments.pad_ambient(note_name, beats_per_chord * 60.0 / self.tempo * 0.8)
            else:
                sample = self.instruments.piano(note_name, beats_per_chord * 60.0 / self.tempo * 0.7)
            
            start = int(chord_time * self.sample_rate)
            end = min(start + len(sample), total_samples)
            if start < total_samples:
                melody[start:end] += sample[:end-start] * 0.4
        
        melody = melody / np.max(np.abs(melody) + 1e-8) * 0.4
        return melody
    
    def mix_and_export(self, tracks, filename):
        """混音並導出"""
        print("🎛️ 混音中...")
        
        total_samples = int(self.sample_rate * self.duration)
        mixed = np.zeros(total_samples, dtype=np.float32)
        
        for track in tracks:
            if track is not None:
                if len(track) < total_samples:
                    track = np.pad(track, (0, total_samples - len(track)))
                elif len(track) > total_samples:
                    track = track[:total_samples]
                mixed += track
        
        # 標準化
        mixed = mixed / np.max(np.abs(mixed) + 1e-8) * 0.9
        
        # 轉換並導出
        mixed_int16 = (mixed * 32767).astype(np.int16)
        
        wav_path = os.path.join(self.output_dir, filename.replace(".mp3", ".wav"))
        wavfile.write(wav_path, self.sample_rate, mixed_int16)
        print(f"✅ WAV: {wav_path}")
        
        # 轉 MP3
        if ".mp3" in filename:
            mp3_path = os.path.join(self.output_dir, filename)
            ffmpeg = os.path.expanduser("~/.openclaw/ai-operator/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2")
            
            if os.path.exists(ffmpeg):
                subprocess.run([
                    ffmpeg, "-i", wav_path,
                    "-acodec", "libmp3lame", "-q:a", "2",
                    "-y", mp3_path
                ], capture_output=True)
                os.remove(wav_path)
                print(f"✅ MP3: {mp3_path}")
                return mp3_path
        
        return wav_path
    
    def generate(self):
        """生成完整 BGM"""
        print(f"\n{'='*50}")
        print(f"🎵 BGM 生成器 v1.0")
        print(f"{'='*50}")
        print(f"曲風: {self.genre}")
        print(f"BPM: {self.tempo}")
        print(f"時長: {self.duration}秒")
        print(f"{'='*50}\n")
        
        # 生成各音軌
        tracks = [
            self.generate_drums(),
            self.generate_bass(),
            self.generate_chords(),
            self.generate_melody(),
        ]
        
        # 混音導出
        filename = f"bgm_{self.genre}_{self.tempo}bpm_{self.duration}s.mp3"
        result = self.mix_and_export(tracks, filename)
        
        print(f"\n{'='*50}")
        print(f"✅ 完成: {result}")
        print(f"{'='*50}\n")
        
        return result


def main():
    parser = argparse.ArgumentParser(description="專業 BGM 生成器")
    parser.add_argument("--genre", "-g", default="electronic",
                       choices=["pop", "rock", "electronic", "ambient", "jazz", "funk", "ballad", "chinese", "chinese_classical"])
    parser.add_argument("--mood", "-m", default="energetic")
    parser.add_argument("--tempo", "-t", type=int, default=120)
    parser.add_argument("--duration", "-d", type=int, default=30)
    parser.add_argument("--key", "-k", default="C")
    parser.add_argument("--output", "-o", default="./output")
    
    args = parser.parse_args()
    
    gen = BGMGenerator(
        genre=args.genre,
        mood=args.mood,
        tempo=args.tempo,
        duration=args.duration,
        key=args.key,
        output_dir=args.output
    )
    
    result = gen.generate()
    print(f"\n📁 輸出: {result}")


if __name__ == "__main__":
    main()
