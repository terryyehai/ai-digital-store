#!/usr/bin/env python3
"""
病毒式 Shorts 影片完整生成器
Viral Shorts Video Generator - Full Version
"""

import os
import sys
import json
import random
from pathlib import Path

# MoviePy
from moviepy.editor import *
from moviepy.video.fx.all import resize, fadein, fadeout
from PIL import Image, ImageDraw, ImageFont

# 路徑
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "videos")
IMAGE_DIR = os.path.join(SCRIPT_DIR, "images")
BGM_DIR = os.path.expanduser("~/ai-products/bgm_generator/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

# 字體路徑
FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]


def find_font():
    """找到可用的字體"""
    for fp in FONT_PATHS:
        if os.path.exists(fp):
            return fp
    return None


def create_text_image(text, size=(1080, 1920), fontsize=80, color="white", stroke="black", stroke_width=3):
    """建立文字圖片"""
    img = Image.new("RGB", size, "black")
    draw = ImageDraw.Draw(img)
    
    font = find_font()
    if font:
        try:
            font = ImageFont.truetype(font, fontsize)
        except:
            font = ImageFont.load_default()
    else:
        font = ImageFont.load_default()
    
    # 計算文字位置（置中）
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # 畫文字（描邊 + 填充）
    draw.text((x, y), text, font=font, fill=color, stroke_width=stroke_width, stroke_fill=stroke)
    
    return img


def create_text_clip(text, duration, fontsize=80, color=(255, 255, 255), position=("center", "center")):
    """建立文字 Clip"""
    # 建立臨時圖片
    temp_file = f"/tmp/text_{random.randint(1000,9999)}.png"
    img = create_text_image(text, fontsize=fontsize, color=color)
    img.save(temp_file)
    
    clip = ImageClip(temp_file).set_duration(duration)
    return clip.set_position(position)


def get_images_for_category(category):
    """獲取分類的圖片"""
    cat_dir = os.path.join(IMAGE_DIR, category)
    if not os.path.exists(cat_dir):
        return []
    
    images = [os.path.join(cat_dir, f) for f in os.listdir(cat_dir) if f.endswith((".jpg", ".png", ".jpeg"))]
    return images


def get_bgm_files():
    """獲取 BGM 檔案"""
    if not os.path.exists(BGM_DIR):
        return []
    
    bgms = [os.path.join(BGM_DIR, f) for f in os.listdir(BGM_DIR) if f.endswith(".mp3")]
    return bgms


class ShortsGenerator:
    """Shorts 影片生成器"""
    
    # 病毒式腳本模板
    SCRIPTS = {
        "ai_writing": {
            "title": "AI部落格寫作神器",
            "duration": 30,
            "segments": [
                {"text": "還在為了寫文章熬夜到凌晨？", "duration": 3, "type": "hook"},
                {"text": "這3個AI Prompt\n讓我10分鐘完成一篇部落格", "duration": 5, "type": "content"},
                {"text": "第一步：設定角色和目標", "duration": 4, "type": "step"},
                {"text": "第二步：輸入詳細大綱", "duration": 4, "type": "step"},
                {"text": "第三步：AI自動生成內容", "duration": 4, "type": "step"},
                {"text": "就是這麼簡單！\n趕快去試試！", "duration": 5, "type": "payoff"},
                {"text": "按讚 + 訂閱", "duration": 5, "type": "cta"},
            ],
        },
        "productivity": {
            "title": "效率提升10倍",
            "duration": 28,
            "segments": [
                {"text": "你還在浪費時間\n做重複工作？", "duration": 3, "type": "hook"},
                {"text": "這3個工具\n讓我效率提升10倍！", "duration": 5, "type": "content"},
                {"text": "第一個：自動化腳本", "duration": 4, "type": "step"},
                {"text": "第二個：AI助手", "duration": 4, "type": "step"},
                {"text": "第三個：模板系統", "duration": 4, "type": "step"},
                {"text": "趕快去試試！\n記得按讚！", "duration": 5, "type": "payoff"},
            ],
        },
        "chinese": {
            "title": "中國傳統文化",
            "duration": 30,
            "segments": [
                {"text": "你只知道兵馬俑？", "duration": 3, "type": "hook"},
                {"text": "秦始皇的地下軍團\n震驚世界", "duration": 5, "type": "content"},
                {"text": "1974年被發現\n8000士兵待命", "duration": 5, "type": "fact"},
                {"text": "每個陶俑\n表情都不相同", "duration": 5, "type": "fact"},
                {"text": "點擊看更多\n歷史故事", "duration": 5, "type": "cta"},
            ],
        },
    }
    
    def __init__(self, script_key="ai_writing", category="ai_writing"):
        self.script_key = script_key
        self.script = self.SCRIPTS.get(script_key, self.SCRIPTS["ai_writing"])
        self.category = category
        
        # 獲取素材
        self.images = get_images_for_category(category)
        self.bgms = get_bgm_files()
        
        # 如果沒有圖片，使用顏色背景
        if not self.images:
            self.images = [None] * len(self.script["segments"])
    
    def generate(self, output_name=None):
        """生成影片"""
        print(f"\n{'='*50}")
        print(f"🎬 Shorts 影片生成器")
        print(f"{'='*50}")
        print(f"腳本: {self.script['title']}")
        print(f"分類: {self.category}")
        
        clips = []
        current_time = 0
        
        # 處理每個段落
        for i, segment in enumerate(self.script["segments"]):
            duration = segment["duration"]
            text = segment["text"]
            seg_type = segment["type"]
            
            print(f"\n📝 段落 {i+1}: {seg_type}")
            print(f"   文字: {text.replace(chr(10), ' | ')}")
            print(f"   時長: {duration}秒")
            
            # 選擇背景
            if i < len(self.images) and self.images[i]:
                img_path = self.images[i]
                try:
                    # 載入圖片
                    img_clip = ImageClip(img_path).set_duration(duration)
                    
                    # 調整大小為 9:16
                    img_clip = img_clip.resize(height=1920)
                    
                    # 裁剪為 9:16
                    img_clip = vfx.crop(img_clip, width=1080, height=1920, x_center="center", y_center="center")
                    
                    # 添加暗化效果（讓文字更清楚）
                    img_clip = img_clip.image_transform(lambda im: ImageEnhance.Brightness(im).enhance(0.5))
                    
                    clips.append(img_clip)
                except Exception as e:
                    print(f"   ⚠️ 圖片載入失敗: {e}")
                    clips.append(self._create_color_clip(duration, seg_type))
            else:
                clips.append(self._create_color_clip(duration, seg_type))
            
            # 添加文字
            fontsize = 70 if seg_type == "hook" else 60
            text_clip = create_text_clip(text, duration, fontsize=fontsize)
            clips.append(text_clip.set_start(current_time))
            
            current_time += duration
        
        # 合併所有 clips
        if clips:
            final_clip = CompositeVideoClip(clips)
        else:
            # 如果沒有內容，建立黑色影片
            final_clip = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=self.script["duration"])
        
        # 添加 BGM
        if self.bgms:
            bgm_path = random.choice(self.bgms)
            print(f"\n🎵 BGM: {os.path.basename(bgm_path)}")
            try:
                bgm = AudioFileClip(bgm_path)
                # 循環或截斷 BGM 以匹配影片長度
                if bgm.duration < self.script["duration"]:
                    # 循環
                    loops = int(self.script["duration"] / bgm.duration) + 1
                    bgm = afx.audio_loop(bgm, nloops=loops).subclip(0, self.script["duration"])
                else:
                    bgm = bgm.subclip(0, self.script["duration"])
                final_clip = final_clip.set_audio(bgm)
            except Exception as e:
                print(f"   ⚠️ BGM 載入失敗: {e}")
        
        # 輸出
        output_name = output_name or f"shorts_{self.script_key}_{int(random.randint(1000,9999))}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_name)
        
        print(f"\n💾 輸出: {output_path}")
        
        # 導出
        final_clip.write_videofile(
            output_path,
            fps=30,
            codec="libx264",
            audio_codec="aac",
            preset="ultrafast",
            verbose=False,
            logger=None
        )
        
        print(f"✅ 完成!")
        
        return output_path
    
    def _create_color_clip(self, duration, seg_type):
        """建立顏色背景 Clip"""
        colors = {
            "hook": (255, 60, 60),      # 紅色
            "content": (60, 60, 255),   # 藍色
            "step": (60, 180, 60),      # 綠色
            "fact": (180, 60, 180),     # 紫色
            "payoff": (255, 180, 60),   # 橙色
            "cta": (60, 60, 60),        # 灰色
        }
        color = colors.get(seg_type, (30, 30, 30))
        
        clip = ColorClip(size=(1080, 1920), color=color, duration=duration)
        
        # 添加漸入效果
        clip = clip.fadein(0.5)
        
        return clip


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Shorts 影片生成器")
    parser.add_argument("--script", "-s", default="ai_writing",
                       choices=["ai_writing", "productivity", "chinese"])
    parser.add_argument("--category", "-c", default="ai_writing",
                       help="圖片分類目錄")
    parser.add_argument("--output", "-o", default=None, help="輸出檔名")
    
    args = parser.parse_args()
    
    generator = ShortsGenerator(script_key=args.script, category=args.category)
    result = generator.generate(args.output)
    
    print(f"\n📁 影片位置: {result}")


if __name__ == "__main__":
    main()
