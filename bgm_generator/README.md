# 🎵 AI BGM 生成器

專業級背景音樂生成工具，無需外部 API，純 Python 實現。

## 功能特點

| 功能 | 說明 |
|------|------|
| 🎸 多曲風 | Pop, Rock, Electronic, Ambient, Jazz, Funk, Ballad |
| 🥁 鼓組引擎 | 8 種鼓組模板（基本、搖滾、電子、嘻哈、雷鬼、放克、氛圍、抒情） |
| 🎹 和弦進行 | 經典和弦進行庫 |
| 🎵 音色合成 | 專業樂器音色（鼓、貝斯、鋼琴、弦樂、合成器） |
| 🎛️ 混音輸出 | WAV + MP3 輸出 |

## 安裝

```bash
cd /home/terry/ai-products/bgm_generator
pip install numpy scipy
```

## 使用方法

### 命令行

```bash
# 電子風格 128 BPM 30秒
python bgm_generator.py --genre electronic --tempo 128 --duration 30

# 流行風格 110 BPM 60秒
python bgm_generator.py --genre pop --tempo 110 --duration 60

# 氛圍音樂 60 BPM
python bgm_generator.py --genre ambient --tempo 60 --duration 45
```

### 參數說明

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `--genre`, `-g` | 曲風 | electronic |
| `--tempo`, `-t` | BPM (60-180) | 120 |
| `--duration`, `-d` | 時長（秒） | 30 |
| `--mood`, `-m` | 情緒 | energetic |
| `--key`, `-k` | 調性 | C |
| `--output`, `-o` | 輸出目錄 | ./output |

### 可用曲風

- `pop` - 流行
- `rock` - 搖滾
- `electronic` - 電子
- `ambient` - 氛圍
- `jazz` - 爵士
- `funk` - 放克
- `ballad` - 抒情

## 曲風與 BPM 建議

| 曲風 | BPM 範圍 | 建議 BPM |
|------|----------|----------|
| Ambient | 40-80 | 60 |
| Ballad | 60-90 | 75 |
| Pop | 90-120 | 110 |
| Funk | 100-120 | 110 |
| Electronic | 120-140 | 128 |
| Rock | 120-160 | 140 |

## 架構

```
bgm_generator/
├── chords/          # 和弦資料庫
│   └── chord_database.py
├── rhythm/          # 節奏模板
│   └── rhythm_patterns.py
├── synths/          # 音色合成
│   └── sound_synthesizer.py
├── output/          # 輸出目錄
└── bgm_generator.py # 主程式
```

## 生成流程

```
1. 鼓組生成 → 根據曲風選擇節奏模板
2. 貝斯生成 → 根據和弦進行生成低音線
3. 和弦生成 → 根據和弦進行生成和弦墊
4. 旋律生成 → 根據和弦生成簡單旋律
5. 混音輸出 → 合併所有音軌並導出
```

## 示例輸出

```bash
$ python bgm_generator.py --genre electronic --tempo 128 --duration 30

==================================================
🎵 BGM 生成器 v1.0
==================================================
曲風: electronic
BPM: 128
時長: 30秒
==================================================

🥁 生成鼓組...
🎸 生成貝斯...
🎹 生成和弦...
🎵 生成旋律...
🎛️ 混音中...
✅ MP3: ./output/bgm_electronic_128bpm_30s.mp3

==================================================
✅ 完成: ./output/bgm_electronic_128bpm_30s.mp3
==================================================
```

## 下一步優化

- [ ] 添加更多和弦進行
- [ ] 加入 MIDI 輸出支持
- [ ] 添加更多樂器音色
- [ ] 實現專業效果器（混響、延遲、壓縮）
- [ ] 添加 AI 旋律生成（接入 Magenta）

---

*生成器版本：1.0.0*
*最後更新：2026-03-13*
