#!/usr/bin/env python3
"""
PPT 風格 Shorts 影片生成器
Slide-based Shorts Video Generator
"""

import os
import sys
import random
from moviepy.editor import *
from moviepy.video.fx.all import resize, fadein, fadeout
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# 路徑
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "videos")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 免費圖片 API
UNSPLASH_URL = "https://source.unsplash.com/featured/1080x1920/?{}"


def find_font():
    """找到可用的字體"""
    fonts = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for fp in fonts:
        if os.path.exists(fp):
            return fp
    return None


def download_image(query, timeout=10):
    """下載相關圖片"""
    try:
        # 使用 Picsum 隨機圖片
        url = f"https://picsum.photos/1080/1920?random={random.randint(1,1000)}"
        resp = requests.get(url, timeout=timeout)
        if resp.status_code == 200:
            img = Image.open(BytesIO(resp.content))
            # 轉 RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')
            return img
    except Exception as e:
        print(f"下載失敗: {e}")
    return None


def create_slide_image(text, subtext="", bg_image=None, theme="dark"):
    """建立幻燈片圖片"""
    width, height = 1080, 1920
    
    if bg_image:
        img = bg_image.copy()
        # 暗化背景
        overlay = Image.new('RGB', (width, height), (0, 0, 0))
        img = Image.blend(img, overlay, 0.5)
    else:
        # 漸變背景
        img = Image.new('RGB', (width, height), (20, 20, 40))
    
    draw = ImageDraw.Draw(img)
    font_path = find_font()
    
    # 選擇字體大小
    if font_path:
        title_font = ImageFont.truetype(font_path, 100)
        sub_font = ImageFont.truetype(font_path, 60)
    else:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
    
    # 標題文字 - 置中
    bbox = draw.textbbox((0, 0), text, font=title_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2
    y = height // 2 - 100
    
    # 畫標題 (黃色字 + 黑色描邊)
    for offset in [(3,3), (3,-3), (-3,3), (-3,-3)]:
        draw.text((x+offset[0], y+offset[1]), text, font=title_font, fill=(0,0,0))
    draw.text((x, y), text, font=title_font, fill=(255, 215, 0))  # 金黃色
    
    # 副標題
    if subtext:
        bbox2 = draw.textbbox((0, 0), subtext, font=sub_font)
        text_w2 = bbox2[2] - bbox2[0]
        x2 = (width - text_w2) // 2
        y2 = y + text_h + 50
        draw.text((x2, y2), subtext, font=sub_font, fill=(255, 255, 255))
    
    # 添加裝飾線
    line_y = height // 2 + 50
    draw.line([(200, line_y), (880, line_y)], fill=(255, 215, 0), width=5)
    
    return img


class PPTSlider:
    """PPT 幻燈片生成器"""
    
    # PPT 腳本模板
    SCRIPTS = {
        "ai_writing": {
            "title": "AI 部落格寫作神器",
            "slides": [
                {
                    "type": "title",
                    "text": "還在為了寫文章\n熬夜到凌晨？",
                    "subtext": "",
                    "effect": "zoom"
                },
                {
                    "type": "content",
                    "text": "這 3 個 AI Prompt\n讓我 10 分鐘完成一篇",
                    "subtext": "",
                    "effect": "slide_left"
                },
                {
                    "type": "step",
                    "text": "第一步",
                    "subtext": "設定角色和目標受眾",
                    "effect": "fade"
                },
                {
                    "type": "step", 
                    "text": "第二步",
                    "subtext": "輸入詳細大綱 Prompt",
                    "effect": "fade"
                },
                {
                    "type": "step",
                    "text": "第三步",
                    "subtext": "AI 自動生成內容",
                    "effect": "fade"
                },
                {
                    "type": "payoff",
                    "text": "就是這麼簡單！\n趕快去試試！",
                    "subtext": "",
                    "effect": "bounce"
                },
                {
                    "type": "cta",
                    "text": "按讚 + 訂閱\n支持創作",
                    "subtext": "",
                    "effect": "pulse"
                },
            ]
        },
        "productivity": {
            "title": "效率提升 10 倍",
            "slides": [
                {
                    "type": "title",
                    "text": "你還在浪費時間\n做重複工作？",
                    "subtext": "",
                    "effect": "zoom"
                },
                {
                    "type": "content",
                    "text": "這 3 個工具\n讓我效率提升 10 倍！",
                    "subtext": "",
                    "effect": "slide_left"
                },
                {
                    "type": "step",
                    "text": "第一個",
                    "subtext": "自動化腳本",
                    "effect": "fade"
                },
                {
                    "type": "step",
                    "text": "第二個", 
                    "subtext": "AI 助手",
                    "effect": "fade"
                },
                {
                    "type": "step",
                    "text": "第三個",
                    "subtext": "模板系統",
                    "effect": "fade"
                },
                {
                    "type": "payoff",
                    "text": "趕快去試試！\n記得按讚！",
                    "subtext": "",
                    "effect": "bounce"
                },
            ]
        },
        "chinese": {
            "title": "兵馬俑的故事",
            "slides": [
                {
                    "type": "title",
                    "text": "秦始皇的\n地下軍團",
                    "subtext": "",
                    "effect": "zoom"
                },
                {
                    "type": "fact",
                    "text": "1974年被發現\n8000士兵待命",
                    "subtext": "",
                    "effect": "slide_left"
                },
                {
                    "type": "fact",
                    "text": "每個陶俑\n表情都不相同",
                    "subtext": "",
                    "effect": "fade"
                },
                {
                    "type": "fact",
                    "text": "歷時38年\n完成建造",
                    "subtext": "",
                    "effect": "fade"
                },
                {
                    "type": "cta",
                    "text": "點擊看更多\n歷史故事",
                    "subtext": "",
                    "effect": "pulse"
                },
            ]
        },
    }
    
    def __init__(self, script_key="ai_writing"):
        self.script_key = script_key
        self.script = self.SCRIPTS.get(script_key, self.SCRIPTS["ai_writing"])
        
        # 下載背景圖片
        self.bg_images = self._download_backgrounds()
    
    def _download_backgrounds(self):
        """下載多張背景圖"""
        themes = {
            "ai_writing": "technology,laptop,office",
            "productivity": "workspace,business,coffee",
            "chinese": "china,ancient,statue",
        }
        
        query = themes.get(self.script_key, "nature")
        images = []
        
        print(f"📥 下載背景圖片...")
        for i in range(5):
            img = download_image(query)
            if img:
                # 調整大小
                img = img.resize((1080, 1920))
                images.append(img)
                print(f"   ✅ 圖片 {i+1}")
        
        # 如果下載失敗，使用顏色背景
        while len(images) < len(self.script["slides"]):
            img = Image.new('RGB', (1080, 1920), (30 + len(images)*10, 40, 60))
            images.append(img)
        
        return images
    
    def generate(self, output_name=None):
        """生成 PPT 影片"""
        print(f"\n{'='*50}")
        print(f"📊 PPT 幻燈片 Shorts 生成器")
        print(f"{'='*50}")
        print(f"腳本: {self.script['title']}")
        print(f"幻燈片數: {len(self.script['slides'])}")
        
        clips = []
        
        for i, slide in enumerate(self.script["slides"]):
            text = slide["text"]
            subtext = slide.get("subtext", "")
            slide_type = slide["type"]
            effect = slide.get("effect", "fade")
            duration = 3.5 if slide_type == "title" else 4
            
            print(f"\n📼 幻燈片 {i+1}: {slide_type}")
            print(f"   文字: {text.replace(chr(10), ' | ')}")
            print(f"   效果: {effect}")
            
            # 選擇背景圖
            bg_idx = i % len(self.bg_images) if self.bg_images else 0
            bg = self.bg_images[bg_idx] if self.bg_images else None
            
            # 建立幻燈片圖片
            slide_img = create_slide_image(text, subtext, bg)
            
            # 儲存臨時檔
            temp_file = f"/tmp/slide_{i}_{random.randint(1000,9999)}.png"
            slide_img.save(temp_file)
            
            # 建立 Clip
            clip = ImageClip(temp_file).set_duration(duration)
            
            # 應用效果
            if effect == "zoom":
                clip = clip.resize(1.0)  # 可以添加 zoom 效果
            elif effect == "fade":
                clip = clip.fadein(0.5).fadeout(0.5)
            
            clips.append(clip)
        
        # 合併
        final_clip = concatenate_videoclips(clips, method="compose")
        
        # 添加 BGM
        bgm_path = os.path.expanduser("~/ai-products/bgm_generator/output/bgm_pop_lead_140bpm.mp3")
        if os.path.exists(bgm_path):
            print(f"\n🎵 添加 BGM")
            bgm = AudioFileClip(bgm_path).subclip(0, final_clip.duration)
            final_clip = final_clip.set_audio(bgm)
        
        # 輸出
        output_name = output_name or f"ppt_{self.script_key}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_name)
        
        print(f"\n💾 輸出: {output_path}")
        
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


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="PPT 風格 Shorts 生成器")
    parser.add_argument("--script", "-s", default="ai_writing",
                       choices=["ai_writing", "productivity", "chinese"])
    parser.add_argument("--output", "-o", default=None)
    
    args = parser.parse_args()
    
    generator = PPTSlider(script_key=args.script)
    result = generator.generate(args.output)
    
    print(f"\n📁 影片位置: {result}")


if __name__ == "__main__":
    main()
