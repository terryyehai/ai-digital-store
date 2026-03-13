# 🎹 音色合成引擎
# Sound Synthesis Engine

import numpy as np
from scipy.io import wavfile
import os

class Synthesizer:
    """音色合成器"""
    
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.pi = np.pi
    
    def sine_wave(self, frequency, duration, amplitude=0.5):
        """正弦波"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        return amplitude * np.sin(2 * self.pi * frequency * t)
    
    def square_wave(self, frequency, duration, amplitude=0.3):
        """方波"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        return amplitude * np.sign(np.sin(2 * self.pi * frequency * t))
    
    def sawtooth_wave(self, frequency, duration, amplitude=0.3):
        """鋸齒波"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        return amplitude * (2 * (t * frequency - np.floor(0.5 + t * frequency)) - 0.5)
    
    def triangle_wave(self, frequency, duration, amplitude=0.4):
        """三角波"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        return amplitude * (2 * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5))) - 1)
    
    def noise(self, duration, amplitude=0.1):
        """白噪音"""
        samples = int(self.sample_rate * duration)
        return amplitude * np.random.randn(samples)
    
    def envelope(self, signal, attack=0.01, decay=0.1, sustain=0.7, release=0.2):
        """ADSR 包絡"""
        length = len(signal)
        attack_samples = int(attack * self.sample_rate)
        decay_samples = int(decay * self.sample_rate)
        release_samples = int(release * self.sample_rate)
        sustain_samples = length - attack_samples - decay_samples - release_samples
        
        if sustain_samples < 0:
            attack_samples = int(length * 0.2)
            decay_samples = int(length * 0.2)
            release_samples = int(length * 0.2)
            sustain_samples = length - attack_samples - decay_samples - release_samples
        
        envelope = np.concatenate([
            np.linspace(0, 1, attack_samples),
            np.linspace(1, sustain, decay_samples) if decay_samples > 0 else np.array([]),
            np.full(max(0, sustain_samples), sustain),
            np.linspace(sustain, 0, release_samples) if release_samples > 0 else np.array([])
        ])
        
        # 確保長度匹配
        if len(envelope) < length:
            envelope = np.pad(envelope, (0, length - len(envelope)))
        elif len(envelope) > length:
            envelope = envelope[:length]
        
        return signal * envelope
    
    def add_reverb(self, signal, room_size=0.5, damping=0.5):
        """簡單混響效果"""
        # 延遲線模擬
        delays = [0.03, 0.05, 0.08, 0.12, 0.17]
        output = signal.copy()
        
        for delay in delays:
            delay_samples = int(delay * self.sample_rate)
            delayed = np.pad(signal, (delay_samples, 0), mode='constant')[:len(signal)]
            output += delayed * room_size * (1 - damping)
        
        return output / (1 + len(delays) * room_size)
    
    def low_pass_filter(self, signal, cutoff=2000):
        """低通濾波器"""
        from scipy.signal import butter, lfilter
        
        nyquist = self.sample_rate / 2
        normalized_cutoff = cutoff / nyquist
        b, a = butter(4, normalized_cutoff, btype='low')
        
        return lfilter(b, a, signal)


# ==================== 樂器音色 ====================

class InstrumentSounds:
    """樂器音色庫"""
    
    def __init__(self, sample_rate=44100):
        self.synth = Synthesizer(sample_rate)
        self.sample_rate = sample_rate
    
    # 鼓組音色
    def kick(self, duration=0.2):
        """底鼓"""
        # 頻率下降的正弦波
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        freq = 150 * np.exp(-t * 20) + 40  # 頻率從 150Hz 降到 40Hz
        signal = np.sin(2 * np.pi * freq * t)
        signal = self.synth.envelope(signal, attack=0.001, decay=0.1, sustain=0, release=0.1)
        return signal
    
    def snare(self, duration=0.2):
        """小鼓"""
        # 混合噪音 + 正弦波
        tone = self.synth.sine_wave(200, duration, 0.5)
        noise = self.synth.noise(duration, 0.5)
        signal = tone + noise
        signal = self.synth.envelope(signal, attack=0.001, decay=0.15, sustain=0, release=0.05)
        return signal
    
    def hihat(self, duration=0.1):
        """高音鈸"""
        # 高頻噪音
        noise = self.synth.noise(duration, 0.4)
        # 高通濾波
        from scipy.signal import butter, lfilter
        nyquist = self.sample_rate / 2
        b, a = butter(4, 5000/nyquist, btype='high')
        signal = lfilter(b, a, noise)
        return self.synth.envelope(signal, attack=0.001, decay=0.08, sustain=0, release=0.02)
    
    def clap(self, duration=0.15):
        """拍手"""
        noise = self.synth.noise(duration, 0.6)
        return self.synth.envelope(noise, attack=0.005, decay=0.1, sustain=0, release=0.05)
    
    def tom(self, duration=0.3):
        """湯姆鼓"""
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        freq = 120 * np.exp(-t * 5) + 60
        signal = np.sin(2 * np.pi * freq * t)
        return self.synth.envelope(signal, attack=0.001, decay=0.2, sustain=0, release=0.1)
    
    # 貝斯音色
    def bass_synth(self, note, duration=0.5):
        """合成貝斯"""
        freq = self.note_to_freq(note)
        # 混合正弦波 + 鋸齒波
        sine = self.synth.sine_wave(freq, duration, 0.6)
        saw = self.synth.sawtooth_wave(freq, duration, 0.3)
        signal = sine + saw
        return self.synth.envelope(signal, attack=0.01, decay=0.1, sustain=0.6, release=0.2)
    
    def bass_electric(self, note, duration=0.5):
        """電貝斯"""
        freq = self.note_to_freq(note)
        signal = self.synth.sine_wave(freq, duration, 0.7)
        signal += self.synth.sine_wave(freq * 2, duration, 0.2)  # 倍頻
        # 低通濾波
        return self.synth.low_pass_filter(signal, 800)
    
    # 旋律音色
    def piano(self, note, duration=0.5):
        """鋼琴 - 真實鋼琴音色"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 鋼琴關鍵：多層諧波 + 鍵擊噪音
        signal = np.zeros(len(t))
        
        # 8層諧波（鋼琴特徵）
        harmonics = [1, 2, 3, 4, 5, 6, 7, 8]
        amplitudes = [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03, 0.015, 0.008]
        
        for h, amp in zip(harmonics, amplitudes):
            signal += amp * np.sin(2 * np.pi * freq * h * t)
        
        # 鍵擊噪音（攻擊時的機械噪音）
        attack_samples = int(0.008 * self.sample_rate)
        if attack_samples < len(signal):
            noise = np.random.randn(attack_samples) * 0.05
            signal[:attack_samples] += noise
        
        # 鋼琴包絡：快速起音、自然衰減
        # 改進：每層諧波獨立衰減 + 增強鍵擊噪音
        # 第一部分：諧波信號獨立衰減
        harm_signal = np.zeros(len(t))
        for h, base_amp in zip(harmonics, amplitudes):
            hf = freq * h
            hs = np.sin(2 * np.pi * hf * t)
            # 高頻諧波衰減更快
            hs *= base_amp * np.exp(-t * (2 + h * 0.3))
            harm_signal += hs
        
        # 第二部分：鍵擊噪音（增強）
        noise_signal = np.zeros(len(t))
        attack_samples = int(0.01 * self.sample_rate)  # 10ms
        if attack_samples < len(t):
            noise = np.random.randn(attack_samples) * 0.1
            # 簡單低通
            noise = np.convolve(noise, np.ones(5)/5, mode='same')
            noise_signal[:attack_samples] = noise
        
        # 合併
        signal = harm_signal + noise_signal * 0.5
        
        # 鋼琴 ADSR 包絡
        return self.synth.envelope(signal, attack=0.005, decay=0.2, sustain=0.35, release=0.6)
    
    def synth_lead(self, note, duration=0.4):
        """合成旋律"""
        freq = self.note_to_freq(note)
        signal = self.synth.sawtooth_wave(freq, duration, 0.4)
        signal += self.synth.sine_wave(freq, duration, 0.3)
        return self.synth.envelope(signal, attack=0.02, decay=0.1, sustain=0.6, release=0.2)
    
    def strings(self, note, duration=1.0):
        """弦樂"""
        freq = self.note_to_freq(note)
        signal = self.synth.sine_wave(freq, duration, 0.4)
        signal += self.synth.sine_wave(freq * 2, duration, 0.2)
        # 添加顫音
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        vibrato = 1 + 0.02 * np.sin(2 * np.pi * 5 * t)
        signal *= vibrato
        return self.synth.envelope(signal, attack=0.1, decay=0.1, sustain=0.8, release=0.3)
    
    def pad_ambient(self, note, duration=2.0):
        """氛圍墊"""
        freq = self.note_to_freq(note)
        signal = self.synth.sine_wave(freq, duration, 0.3)
        signal += self.synth.sine_wave(freq * 1.5, duration, 0.15)  # 大三度
        signal += self.synth.sine_wave(freq * 2, duration, 0.1)  # 八度
        # 添加混響
        signal = self.synth.add_reverb(signal, room_size=0.6, damping=0.3)
        return self.synth.envelope(signal, attack=0.3, decay=0.2, sustain=0.6, release=0.5)
    
    def guitar_acoustic(self, note, duration=0.6):
        """木吉他"""
        freq = self.note_to_freq(note)
        signal = self.synth.sawtooth_wave(freq, duration, 0.3)
        signal += self.synth.sawtooth_wave(freq * 2, duration, 0.15)
        # 交替弦樂效果
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        tremolo = 1 + 0.3 * np.sin(2 * np.pi * 8 * t)
        signal *= tremolo
        return self.synth.envelope(signal, attack=0.01, decay=0.2, sustain=0.5, release=0.3)
    
    # 輔助方法
    def note_to_freq(self, note):
        """音符轉頻率"""
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        if isinstance(note, str):
            if len(note) == 2:
                note_name = note[0]
                octave = int(note[1])
            elif len(note) == 3:
                note_name = note[:2]
                octave = int(note[2])
            else:
                return 440
            
            if note_name in notes:
                semitone = notes.index(note_name)
                # A4 = 440Hz
                return 440 * 2 ** ((semitone - 9 + (octave - 4) * 12) / 12)
        return note


# ==================== 測試 ====================

if __name__ == "__main__":
    inst = InstrumentSounds()
    
    # 測試底鼓
    kick = inst.kick()
    print(f"底鼓樣本: {len(kick)} samples")
    
    # 測試鋼琴
    piano = inst.piano("C4", 0.5)
    print(f"鋼琴樣本: {len(piano)} samples")
    
    print("音色庫載入成功")

# ==================== 中國傳統樂器 ====================

class ChineseInstruments:
    """中國傳統樂器音色庫"""
    
    def __init__(self, sample_rate=44100):
        self.synth = Synthesizer(sample_rate)
        self.sample_rate = sample_rate
    
    def erhu(self, note, duration=1.0):
        """二胡 - 中國傳統弦樂，音色悲涼憂鬱"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 二胡特色：滑音 + 顫音
        signal = self.synth.sine_wave(freq, duration, 0.5)
        # 添加滑音效果
        glide = np.linspace(1.0, 0.95, len(t))
        signal *= glide
        # 添加顫音
        vibrato = 1 + 0.03 * np.sin(2 * np.pi * 6 * t)
        signal *= vibrato
        # 添加泛音
        signal += self.synth.sine_wave(freq * 2, duration, 0.15)
        signal += self.synth.sine_wave(freq * 3, duration, 0.05)
        
        # 二胡包絡：慢起音、長延音
        return self.synth.envelope(signal, attack=0.1, decay=0.2, sustain=0.6, release=0.3)
    
    def guzheng(self, note, duration=0.8):
        """古箏 - 中國傳統彈撥，音色清脆如流水"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 古箏特色：彈撥感 + 共鳴
        signal = self.synth.sawtooth_wave(freq, duration, 0.3)
        signal += self.synth.sine_wave(freq, duration, 0.4)
        # 弦樂共鳴
        signal += self.synth.sine_wave(freq * 2, duration, 0.2)
        signal += self.synth.sine_wave(freq * 3, duration, 0.1)
        
        # 顫音裝飾
        vibrato = 1 + 0.02 * np.sin(2 * np.pi * 5 * t)
        signal *= vibrato
        
        # 快速起音，短延音
        return self.synth.envelope(signal, attack=0.005, decay=0.3, sustain=0.4, release=0.3)
    
    def pipa(self, note, duration=0.5):
        """琵琶 - 中國彈撥樂器，音色鏗鏘有力"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 琵琶特色：顆粒感、輪指效果
        signal = self.synth.square_wave(freq, duration, 0.3)
        signal += self.synth.sawtooth_wave(freq, duration, 0.2)
        
        # 模擬輪指（快速重複）
        tremolo = np.ones(len(t))
        for i in range(len(t)):
            tremolo[i] *= (1 + 0.3 * np.sin(2 * np.pi * 12 * t[i]))
        signal *= tremolo
        
        # 快速起音，短促
        return self.synth.envelope(signal, attack=0.001, decay=0.2, sustain=0.3, release=0.1)
    
    def dizi(self, note, duration=1.5):
        """笛子 - 中國吹奏樂器，音色悠揚空靈"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 笛子特色：純淨音色 + 氣流感
        signal = self.synth.sine_wave(freq, duration, 0.5)
        signal += self.synth.sine_wave(freq * 2, duration, 0.2)  # 高音泛音
        signal += self.synth.sine_wave(freq * 3, duration, 0.1)
        
        # 氣流感（輕微波動）
        breath = 1 + 0.05 * np.sin(2 * np.pi * 3 * t)
        signal *= breath
        
        # 悠長延音
        return self.synth.envelope(signal, attack=0.05, decay=0.1, sustain=0.8, release=0.4)
    
    def suona(self, note, duration=0.6):
        """嗩吶 - 中國吹管樂器，音色高昂熱鬧"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 嗩吶特色：明亮、帶有雜音的張力
        signal = self.synth.sawtooth_wave(freq, duration, 0.4)
        signal += self.synth.sine_wave(freq * 2, duration, 0.3)
        signal += self.synth.noise(duration, 0.1)  # 添加氣息雜音
        
        # 顫音
        vibrato = 1 + 0.04 * np.sin(2 * np.pi * 8 * t)
        signal *= vibrato
        
        # 有力的起音和衰减
        return self.synth.envelope(signal, attack=0.01, decay=0.2, sustain=0.5, release=0.2)
    
    def yangqin(self, note, duration=0.4):
        """揚琴 - 中國擊弦樂器，音色明亮顆粒"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 揚琴特色：顆粒感、金屬音色
        signal = self.synth.sine_wave(freq, duration, 0.3)
        signal += self.synth.sine_wave(freq * 2.5, duration, 0.3)  # 金屬泛音
        signal += self.synth.sine_wave(freq * 4, duration, 0.2)
        
        # 快速衰减
        return self.synth.envelope(signal, attack=0.001, decay=0.3, sustain=0.2, release=0.1)
    
    def guqin(self, note, duration=2.0):
        """古琴 - 中國最古老弦樂，音色深沉內斂"""
        freq = self.note_to_freq(note)
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        
        # 古琴特色：深沉、餘音繞梁
        signal = self.synth.sine_wave(freq, duration, 0.4)
        signal += self.synth.sine_wave(freq * 2, duration, 0.15)
        
        # 吟猱效果
        for i in range(len(t)):
            if i % 1000 == 0:
                signal[i:i+100] *= 1.1
        
        # 緩慢起音，極長延音
        return self.synth.envelope(signal, attack=0.2, decay=0.2, sustain=0.5, release=0.8)
    
    def zheng_piano(self, note, duration=0.6):
        """鋼琴（優雅版）- 真實鋼琴音色"""
        return self.piano(note, duration)  # 使用改良後的鋼琴音色
    
    # 輔助方法
    def note_to_freq(self, note):
        """音符轉頻率"""
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        if isinstance(note, str):
            note = note.strip()
            if len(note) >= 2:
                try:
                    note_name = note[:-1]
                    octave = int(note[-1])
                    if note_name in notes:
                        semitone = notes.index(note_name)
                        return 440 * 2 ** ((semitone - 9 + (octave - 4) * 12) / 12)
                except:
                    pass
        return 440


# ==================== 音色驗證系統 ====================

class SoundVerifier:
    """音色驗證器 - 確保輸出正確的樂器音色"""
    
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
    
    def analyze_frequency(self, audio):
        """分析頻譜"""
        from scipy.fft import fft, fftfreq
        
        n = len(audio)
        yf = fft(audio)
        xf = fftfreq(n, 1/self.sample_rate)[:n//2]
        power = 2.0/n * np.abs(yf[0:n//2])
        
        return xf, power
    
    def get_spectral_centroid(self, audio):
        """計算頻譜重心（音色亮度）"""
        xf, power = self.analyze_frequency(audio)
        centroid = np.sum(xf * power) / np.sum(power + 1e-10)
        return centroid
    
    def get_harmonic_ratio(self, audio):
        """計算諧波比率"""
        xf, power = self.analyze_frequency(audio)
        
        # 找基頻
        fundamental_idx = np.argmax(power[:2000])  # 低頻區找基頻
        fundamental_freq = xf[fundamental_idx]
        
        # 計算諧波能量
        harmonics = []
        for h in range(1, 6):
            harmonic_freq = fundamental_freq * h
            if harmonic_freq < xf[-1]:
                idx = int(harmonic_freq * len(xf) / (self.sample_rate/2))
                if idx < len(power):
                    harmonics.append(power[idx])
        
        return harmonics, fundamental_freq
    
    def verify_piano(self, audio):
        """驗證是否為鋼琴音色"""
        # 鋼琴特徵：
        # 1. 清晰的諧波結構
        # 2. 快速起音
        # 3. 頻譜重心在 800-2000 Hz
        
        centroid = self.get_spectral_centroid(audio)
        harmonics, freq = self.get_harmonic_ratio(audio)
        
        # 起音分析
        attack_samples = int(0.02 * self.sample_rate)
        attack_energy = np.sum(audio[:attack_samples]**2)
        total_energy = np.sum(audio**2)
        attack_ratio = attack_energy / (total_energy + 1e-10)
        
        # 驗證條件
        checks = {
            "頻譜重心": 500 < centroid < 3000,
            "諧波存在": len(harmonics) >= 3,
            "起音明顯": attack_ratio > 0.05,
            "基頻合理": 60 < freq < 2000,
        }
        
        passed = sum(checks.values())
        total = len(checks)
        
        return passed >= 3, {
            "centroid": centroid,
            "fundamental_freq": freq,
            "harmonics": harmonics,
            "attack_ratio": attack_ratio,
            "checks": checks,
            "score": f"{passed}/{total}"
        }
    
    def verify_guzheng(self, audio):
        """驗證是否為古箏音色"""
        # 古箏特徵：
        # 1. 豐富的低頻共鳴
        # 2. 顆粒感
        # 3. 較寬的頻譜
        
        centroid = self.get_spectral_centroid(audio)
        
        # 低頻能量
        xf, power = self.analyze_frequency(audio)
        low_freq_mask = xf < 500
        low_energy = np.sum(power[low_freq_mask])
        total_energy = np.sum(power)
        low_ratio = low_energy / (total_energy + 1e-10)
        
        checks = {
            "低頻共鳴": low_ratio > 0.2,
            "頻譜合理性": 200 < centroid < 2500,
        }
        
        passed = sum(checks.values())
        return passed >= 1, {"centroid": centroid, "low_ratio": low_ratio, "score": f"{passed}/2"}
    
    def verify_dizi(self, audio):
        """驗證是否為笛子音色"""
        # 笛子特徵：
        # 1. 純淨音色（諧波較少）
        # 2. 高頻較少
        # 3. 頻譜重心適中
        
        centroid = self.get_spectral_centroid(audio)
        harmonics, freq = self.get_harmonic_ratio(audio)
        
        # 諧波比（笛子諧波較少）
        if len(harmonics) > 0:
            harmonic_ratio = harmonics[0] / (sum(harmonics) + 1e-10)
        else:
            harmonic_ratio = 0
        
        checks = {
            "頻譜純淨": centroid < 2000,
            "基頻存在": freq > 200,
            "諧波比": harmonic_ratio > 0.3,
        }
        
        passed = sum(checks.values())
        return passed >= 2, {"centroid": centroid, "harmonic_ratio": harmonic_ratio, "score": f"{passed}/3"}
    
    def verify_erhu(self, audio):
        """驗證是否為二胡音色"""
        # 二胡特徵：
        # 1. 頻率波動（滑音、顫音）
        # 2. 較少的諧波
        # 3. 中頻為主
        
        centroid = self.get_spectral_centroid(audio)
        
        # 頻率波動
        instantaneous_freq = np.diff(audio)
        freq_variance = np.var(instantaneous_freq)
        
        checks = {
            "中頻為主": 200 < centroid < 1500,
            "頻率波動": freq_variance > 0.001,
        }
        
        passed = sum(checks.values())
        return passed >= 1, {"centroid": centroid, "variance": freq_variance, "score": f"{passed}/2"}
    
    def verify_instrument(self, audio, instrument_name):
        """驗證樂器音色"""
        verifiers = {
            "piano": self.verify_piano,
            "guzheng": self.verify_guzheng,
            "dizi": self.verify_dizi,
            "erhu": self.verify_erhu,
        }
        
        verifier = verifiers.get(instrument_name)
        if verifier:
            return verifier(audio)
        
        # 預設：只做基本檢查
        centroid = self.get_spectral_centroid(audio)
        return centroid > 0, {"centroid": centroid, "note": "basic check only"}


# ==================== 測試 ====================

if __name__ == "__main__":
    # 測試鋼琴驗證
    synth = Synthesizer()
    verifier = SoundVerifier()
    
    # 生成鋼琴音符
    piano_note = synth.sine_wave(261.63, 1.0, 0.5)  # C4
    piano_note += synth.sine_wave(523.25, 1.0, 0.25)  # C5
    piano_note += synth.sine_wave(784.87, 1.0, 0.125)  # G5
    piano_note = synth.envelope(piano_note, attack=0.01, decay=0.3, sustain=0.4, release=0.3)
    
    # 驗證
    is_valid, details = verifier.verify_piano(piano_note)
    print(f"鋼琴驗證: {'✅ 通過' if is_valid else '❌ 失敗'}")
    print(f"詳情: {details}")

