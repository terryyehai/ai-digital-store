# 🎵 專業和弦資料庫
# Professional Chord Database
# 生成日期：2026-03-13

## 和弦級數對照表

### 大調 (Major Scale)
| 級數 | 和弦 | 羅馬數字 | 功能 |
|------|------|----------|------|
| 1 | C | I | 主和弦 (Tonic) |
| 2 | Dm | ii | 下屬和弦 (Supertonic) |
| 3 | Em | iii | 中和弦 (Mediant) |
| 4 | F | IV | 下屬和弦 (Subdominant) |
| 5 | G | V | 屬和弦 (Dominant) |
| 6 | Am | vi | 下屬和弦 (Submediant) |
| 7 | Bdim | vii° | 導和弦 (Leading) |

### 小調 (Minor Scale)
| 級數 | 和弦 | 羅馬數字 | 功能 |
|------|------|----------|------|
| 1 | Am | i | 主和弦 |
| 2 | Bdim | ii° | 半減七 |
| 3 | C | III | 大三 |
| 4 | Dm | iv | 小四 |
| 5 | Em | v | 小五 |
| 6 | F | VI | 大六 |
| 7 | G | VII | 大七 |

---

## 經典和弦進行 (Chord Progressions)

### Pop / Rock 常見
```python
POP_ progressions = [
    ["I", "V", "vi", "IV"],  # 流行經典 (C-G-Am-F)
    ["I", "IV", "V", "I"],  # 基本進行
    ["I", "vi", "IV", "V"],  # Canon in D
    ["vi", "IV", "I", "V"],  # 悲傷進行
    ["I", "V", "vi", "iii", "IV", "I", "IV", "V"],  # 八和弦進行
]
```

### Jazz 常見
```python
JAZZ_progressions = [
    ["ii7", "V7", "Imaj7"],  # 基礎爵士
    ["Imaj7", "vi7", "ii7", "V7"],  # 週期進行
    ["Im7", "IVm7", "bVII7", "bIIImaj7"],  # Minor Swing
    ["I7", "IV7", "I7", "V7"],  # 12 Bar Blues
]
```

### Electronic / EDM
```python
ELECTRONIC_progressions = [
    ["I", "V", "vi", "IV"],  # 流行電子
    ["i", "VII", "VI", "v"],  # 黑暗電子
    ["I", "bVII", "IV", "I"],  # Pop Epic
]
```

### Ambient / Cinematic
```python
AMBIENT_progressions = [
    ["I", "IV", "I", "V"],  # 簡單氛圍
    ["i", "v", "i", "iv"],  # 悲傷氛圍
    ["I", "iii", "IV", "V"],  # 電影感
]
```

### Funk / Disco
```python
FUNK_progressions = [
    ["I7", "IV7", "I7", "V7"],  # Funk 基本
    ["ii7", "V7", "Imaj7", "IV7"],  # Disco
]
```

---

## 音符頻率表 (Note Frequencies)

### A4 = 440Hz 標準
| Note | Hz |
|------|-----|
| C3 | 130.81 |
| D3 | 146.83 |
| E3 | 164.81 |
| F3 | 174.61 |
| G3 | 196.00 |
| A3 | 220.00 |
| B3 | 246.94 |
| C4 | 261.63 |
| D4 | 293.66 |
| E4 | 329.63 |
| F4 | 349.23 |
| G4 | 392.00 |
| A4 | 440.00 |
| B4 | 493.88 |
| C5 | 523.25 |
| D5 | 587.33 |
| E5 | 659.25 |
| F5 | 698.46 |
| G5 | 783.99 |

---

## 和弦音符構成

### Major 和弦 (Major Triad)
- 根音 (Root)
- 大三度 (Major 3rd) = 4 semitones
- 純五度 (Perfect 5th) = 7 semitones
- Example: C = C + E + G

### Minor 和弦 (Minor Triad)
- 根音 (Root)
- 小三度 (Minor 3rd) = 3 semitones
- 純五度 (Perfect 5th) = 7 semitones
- Example: Am = A + C + E

### 7th 和弦 (Seventh Chords)
| 類型 | 構成 | Example |
|------|------|---------|
| Major 7th | 1 + 3 + 5 + 7 | Cmaj7 |
| Dominant 7th | 1 + b3 + 5 + b7 | C7 |
| Minor 7th | 1 + b3 + 5 + b7 | Cm7 |
| Half Dim 7th | 1 + b3 + b5 + b7 | Cm7b5 |

---

## BPM 建議

| 曲風 | BPM 範圍 | 建議值 |
|------|----------|--------|
| Ambient | 40-80 | 60 |
| Ballad | 60-90 | 75 |
| Pop | 90-120 | 110 |
| Funk | 100-120 | 110 |
| Electronic | 120-140 | 128 |
| Rock | 120-160 | 140 |
| Hip-hop | 70-100 | 90 |

---

## 調式建議 (Keys)

| 調性 | 情緒 | 適用曲風 |
|------|------|----------|
| C Major | 明亮、快樂 | Pop, Rock |
| G Major | 溫暖、開放 | Folk, Country |
| D Major | 明亮、力量 | Rock, Pop |
| A Minor | 悲傷、深刻 | Ballad, Cinematic |
| E Minor | 戲劇性 | Rock, Metal |
| Am (Relative to C) | 柔和、憂鬱 | Pop, Electronic |

---

*和弦資料庫建構完成*
