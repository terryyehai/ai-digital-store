# 🥁 節奏模板系統
# Rhythm Template System

import numpy as np

class RhythmPattern:
    """節奏模板類"""
    
    def __init__(self, name, bpm, time_signature=(4, 4)):
        self.name = name
        self.bpm = bpm
        self.time_signature = time_signature
        self.beats_per_measure = time_signature[0]
        self.seconds_per_beat = 60.0 / bpm
        self.seconds_per_measure = self.seconds_per_beat * self.beats_per_measure
    
    def get_beat_times(self, measures=1):
        """獲取每拍的時間點"""
        total_beats = self.beats_per_measure * measures
        return [i * self.seconds_per_beat for i in range(total_beats)]


# ==================== 鼓組模板 ====================

class DrumPatterns:
    """鼓組節奏模板庫"""
    
    @staticmethod
    def basic_4_4():
        """基本 4/4 拍"""
        return {
            "kick":  [1, 0, 0, 0,  2, 0, 0, 0,  3, 0, 0, 0,  4, 0, 0, 0],  # 每拍一個
            "snare": [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],  # 2, 4 拍
            "hihat": [1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1],  # 8 分音符
        }
    
    @staticmethod
    def rock():
        """搖滾鼓組"""
        return {
            "kick":   [1, 0, 0, 0,  0, 0, 1, 0,  0, 0, 0, 0,  1, 0, 1, 0],
            "snare":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],
            "hihat":  [1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1,  1, 1, 1, 1],
            "tom":    [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 1],
        }
    
    @staticmethod
    def electronic():
        """電子舞曲鼓組"""
        return {
            "kick":   [1, 0, 0, 0,  1, 0, 0, 0,  1, 0, 0, 0,  1, 0, 0, 0],
            "snare":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],
            "hihat":  [1, 0, 1, 0,  1, 0, 1, 0,  1, 0, 1, 0,  1, 0, 1, 0],  # 16 分音符
            "clap":   [0, 0, 0, 1,  0, 0, 0, 1,  0, 0, 0, 1,  0, 0, 0, 1],
        }
    
    @staticmethod
    def hiphop():
        """嘻哈鼓組"""
        return {
            "kick":   [1, 0, 0, 1,  0, 0, 1, 0,  0, 1, 0, 0,  0, 0, 1, 0],
            "snare":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],
            "hihat":  [1, 0, 1, 0,  0, 0, 1, 0,  1, 0, 1, 0,  0, 0, 1, 0],
            "snare2": [0, 0, 0, 1,  0, 0, 0, 1,  0, 0, 0, 1,  0, 0, 0, 1],
        }
    
    @staticmethod
    def reggae():
        """雷鬼節奏"""
        return {
            "kick":   [1, 0, 0, 0,  0, 0, 1, 0,  0, 0, 0, 0,  0, 0, 1, 0],
            "snare":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],
            "hihat":  [1, 0, 1, 0,  1, 0, 1, 0,  1, 0, 1, 0,  1, 0, 1, 0],
            "skank":  [0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0],  # Guitar skank
        }
    
    @staticmethod
    def funk():
        """放克節奏"""
        return {
            "kick":   [1, 0, 0, 1,  0, 0, 1, 0,  0, 0, 1, 0,  0, 1, 0, 0],
            "snare":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],
            "hihat":  [1, 1, 0, 1,  1, 1, 0, 1,  1, 1, 0, 1,  1, 1, 0, 1],
            "cowbell":[0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0],
        }
    
    @staticmethod
    def ambient():
        """氛圍節奏（輕柔）"""
        return {
            "kick":   [1, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0],  # 每小節一次
            "hihat":  [0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0,  0, 0, 1, 0],  # 稀疏
            "pad":    [1, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0],  # 持續音
        }
    
    @staticmethod
    def ballad():
        """抒情節奏"""
        return {
            "kick":   [1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0],
            "snare":  [0, 0, 0, 0,  1, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 0],
            "hihat":  [1, 0, 1, 0,  1, 0, 1, 0,  1, 0, 1, 0,  1, 0, 1, 0],
            "toms":   [0, 0, 0, 0,  0, 0, 0, 0,  0, 0, 0, 0,  1, 0, 0, 1],
        }


# ==================== 節奏工廠 ====================

class RhythmFactory:
    """節奏工廠"""
    
    PRESETS = {
        "basic_4_4": DrumPatterns.basic_4_4,
        "rock": DrumPatterns.rock,
        "electronic": DrumPatterns.electronic,
        "hiphop": DrumPatterns.hiphop,
        "reggae": DrumPatterns.reggae,
        "funk": DrumPatterns.funk,
        "ambient": DrumPatterns.ambient,
        "ballad": DrumPatterns.ballad,
    }
    
    @classmethod
    def get_pattern(cls, genre):
        """根據曲風獲取節奏模板"""
        return cls.PRESETS.get(genre, DrumPatterns.basic_4_4)
    
    @classmethod
    def get_bpm_range(cls, genre):
        """根據曲風獲取建議 BPM"""
        ranges = {
            "basic_4_4": (90, 120),
            "rock": (100, 160),
            "electronic": (120, 140),
            "hiphop": (70, 100),
            "reggae": (60, 90),
            "funk": (100, 120),
            "ambient": (40, 80),
            "ballad": (60, 90),
        }
        return ranges.get(genre, (90, 120))


# ==================== 節奏生成器 ====================

class RhythmGenerator:
    """節奏生成器"""
    
    def __init__(self, genre="electronic", bpm=120, duration=30):
        self.genre = genre
        self.bpm = bpm
        self.duration = duration
        self.pattern = RhythmFactory.get_pattern(genre)
        self.seconds_per_beat = 60.0 / bpm
    
    def generate_drum_track(self):
        """生成鼓組音軌"""
        total_beats = int(self.bpm * self.duration / 60)
        
        # 擴展模板到完整時長
        drum_track = {}
        for instrument, pattern in self.pattern.items():
            expanded = []
            repeat = (total_beats // len(pattern)) + 1
            expanded = (pattern * repeat)[:total_beats]
            drum_track[instrument] = expanded
        
        return drum_track
    
    def get_beat_times(self):
        """獲取每拍的時間"""
        total_beats = int(self.bpm * self.duration / 60)
        return [i * self.seconds_per_beat for i in range(total_beats)]


if __name__ == "__main__":
    # 測試
    gen = RhythmGenerator(genre="electronic", bpm=128, duration=30)
    drums = gen.generate_drum_track()
    print(f"鼓組生成完成: {len(drums['kick'])} beats")
    print(f"Genre: {gen.genre}, BPM: {gen.bpm}")
