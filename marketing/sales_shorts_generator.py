#!/usr/bin/env python3
"""
真正能賣的行銷 Shorts - 產品導向
High-Converting Sales Shorts Generator
"""

import os
import sys
import random
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# 路徑
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "videos")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 產品腳本 - 真正能轉換的公式
PRODUCT_SCRIPTS = {
    "ai_prompts": {
        "product_name": "AI Prompt 模板套裝",
        "price": "$9.99",
        "problem": "每次要花 1 小時寫提示詞？",
        "solution": "這套 AI Prompt 模板",
        "benefit": "10 分鐘完成一篇專業文章",
        "slides": [
            {
                "type": "hook",
                "text": "還在為了寫提示詞\n浪費 1 小時？",
                "subtext": "",
                "duration": 3
            },
            {
                "type": "agitate",
                "text": "我以前也是...\n每天對著空白畫面發呆",
                "subtext": "浪費時間、沒靈感、產量低",
                "duration": 4
            },
            {
                "type": "solution",
                "text": "直到我發現了\n這套 AI Prompt 模板",
                "subtext": "",
                "duration": 3
            },
            {
                "type": "proof",
                "text": "現在 10 分鐘\n就能寫完一篇專業文章",
                "subtext": "部落格、社群、郵件都能用",
                "duration": 4
            },
            {
                "type": "offer",
                "text": "原价 $19.99\n限時特價 $9.99",
                "subtext": "終身使用權 + 免費更新",
                "duration": 4
            },
            {
                "type": "cta",
                "text": "點擊下方連結\n馬上獲取",
                "subtext": "數量有限，售完為止",
                "duration": 3
            }
        ]
    },
    "bgm_generator": {
        "product_name": "AI BGM 音樂生成器",
        "price": "$14.99",
        "problem": "找不到適合的背景音樂？",
        "solution": "AI 音樂生成器",
        "benefit": "輸入關鍵詞，自動生成版權音樂",
        "slides": [
            {
                "type": "hook",
                "text": "你的影片\n還在用免費音樂？",
                "subtext": "",
                "duration": 3
            },
            {
                "type": "agitate",
                "text": "版權問題好麻煩\n又被 YouTube 警告",
                "subtext": "影片被移除、收益被沒收",
                "duration": 4
            },
            {
                "type": "solution",
                "text": "我用 AI 自動生成\n自己的背景音樂",
                "subtext": "原創、獨特、永遠不侵權",
                "duration": 4
            },
            {
                "type": "proof",
                "text": "任何風格都能生成\n流行、古典、抖音熱門",
                "subtext": "",
                "duration": 4
            },
            {
                "type": "offer",
                "text": "終身免費升級\n僅需 $14.99",
                "subtext": "",
                "duration": 3
            },
            {
                "type": "cta",
                "text": "連結在評論區\n趕快去搶！",
                "subtext": "",
                "duration": 3
            }
        ]
    },
    "youtube_automation": {
        "product_name": "YouTube 自動化系統",
        "price": "$29.99",
        "problem": "想做 YouTube 但沒時間剪片？",
        "solution": "全自動 YouTube 系統",
        "benefit": "AI 幫你寫腳本、生成影片、上傳",
        "slides": [
            {
                "type": "hook",
                "text": "想做 YouTube\n但不會剪片？",
                "subtext": "",
                "duration": 3
            },
            {
                "type": "agitate",
                "text": "剪一支片要 5 小時\n根本沒時間經營",
                "subtext": "內容做不起來、好累",
                "duration": 4
            },
            {
                "type": "solution",
                "text": "這套系統\nAI 幫你全部搞定",
                "subtext": "腳本、剪輯、上傳一鍵完成",
                "duration": 4
            },
            {
                "type": "proof",
                "text": "每天自動產出\n3-5 支 Shorts",
                "subtext": "",
                "duration": 4
            },
            {
                "type": "offer",
                "text": "原價 $49.99\n特價 $29.99",
                "subtext": "包含完整教學 + 售後服務",
                "duration": 4
            },
            {
                "type": "cta",
                "text": "名額有限\n馬上點擊！",
                "subtext": "",
                "duration": 3
            }
        ]
    }
}


def find_font():
    """找到可用的字體"""
    fonts = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",
        "/usr/share/fonts/truetype/arphic/ukai.ttc",
        "/usr/share/fonts/truetype/arphic/uming.ttc",
    ]
    for fp in fonts:
        if os.path.exists(fp):
            return fp
    return None


def download_bg(query="technology"):
    """下載背景圖"""
    try:
        url = f"https://picsum.photos/1080/1920?random={random.randint(1,1000)}"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            img = Image.open(BytesIO(resp.content))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            return img.resize((1080, 1920))
    except:
        pass
    return None


def create_sales_slide(text, subtext="", bg_image=None, slide_type="normal"):
    """建立銷售導向幻燈片"""
    width, height = 1080, 1920
    
    # 背景
    if bg_image:
        img = bg_image.copy()
        overlay = Image.new('RGB', (width, height), (0, 0, 0))
        img = Image.blend(img, overlay, 0.6)
    else:
        # 根據類型選擇顏色
        colors = {
            "hook": (200, 50, 50),      # 紅色 - 引起注意
            "agitate": (80, 80, 120),   # 藍灰色 - 陳述問題
            "solution": (50, 150, 80),  # 綠色 - 解決方案
            "proof": (100, 80, 150),    # 紫色 - 證明
            "offer": (255, 180, 0),    # 金色 - 優惠
            "cta": (255, 80, 80),       # 紅色 - 行動
            "normal": (30, 30, 50),     # 深色
        }
        color = colors.get(slide_type, (30, 30, 50))
        img = Image.new('RGB', (width, height), color)
    
    draw = ImageDraw.Draw(img)
    font_path = find_font()
    
    if font_path:
        title_size = 90 if slide_type == "hook" else 70
        sub_size = 45
        title_font = ImageFont.truetype(font_path, title_size)
        sub_font = ImageFont.truetype(font_path, sub_size)
    else:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()
    
    # 標題 - 置中
    lines = text.split('\n')
    y = height // 2 - 100
    
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        text_w = bbox[2] - bbox[0]
        x = (width - text_w) // 2
        
        # 黃色字 + 黑邊
        for ox, oy in [(3,3), (3,-3), (-3,3), (-3,-3)]:
            draw.text((x+ox, y+oy), line, font=title_font, fill=(0,0,0))
        draw.text((x, y), line, font=title_font, fill=(255, 220, 0))
        y += title_size + 10
    
    # 副標題
    if subtext:
        y += 20
        bbox2 = draw.textbbox((0, 0), subtext, font=sub_font)
        text_w2 = bbox2[2] - bbox2[0]
        x2 = (width - text_w2) // 2
        draw.text((x2, y), subtext, font=sub_font, fill=(255, 255, 255))
    
    # 裝飾線
    line_y = height // 2 - 130
    draw.line([(150, line_y), (930, line_y)], fill=(255, 220, 0), width=4)
    
    return img


class SalesShortsGenerator:
    """銷售導向 Shorts 生成器"""
    
    def __init__(self, product_key="ai_prompts"):
        self.product_key = product_key
        self.product = PRODUCT_SCRIPTS.get(product_key, PRODUCT_SCRIPTS["ai_prompts"])
        
        # 下載背景
        self.bg_images = []
        print("📥 下載背景圖...")
        for i in range(6):
            bg = download_bg()
            if bg:
                self.bg_images.append(bg)
        
        while len(self.bg_images) < len(self.product["slides"]):
            self.bg_images.append(None)
    
    def generate(self, output_name=None):
        """生成影片"""
        print(f"\n{'='*50}")
        print(f"💰 銷售 Shorts 生成器")
        print(f"{'='*50}")
        print(f"產品: {self.product['product_name']}")
        print(f"價格: {self.product['price']}")
        
        clips = []
        
        for i, slide in enumerate(self.product["slides"]):
            slide_type = slide["type"]
            text = slide["text"]
            subtext = slide.get("subtext", "")
            duration = slide["duration"]
            
            print(f"\n📼 幻燈片 {i+1}: {slide_type}")
            
            # 選擇背景
            bg = self.bg_images[i] if i < len(self.bg_images) else None
            
            # 建立圖片
            slide_img = create_sales_slide(text, subtext, bg, slide_type)
            
            # 儲存
            temp_file = f"/tmp/sales_slide_{i}_{random.randint(1000,9999)}.png"
            slide_img.save(temp_file)
            
            # 建立 Clip
            clip = ImageClip(temp_file).set_duration(duration)
            clip = clip.fadein(0.3).fadeout(0.3)
            
            clips.append(clip)
        
        # 合併
        final_clip = concatenate_videoclips(clips, method="compose")
        
        # 添加 BGM - 節奏感強的
        bgm_path = os.path.expanduser("~/ai-products/bgm_generator/output/bgm_pop_lead_140bpm.mp3")
        if os.path.exists(bgm_path):
            print(f"\n🎵 添加 BGM")
            bgm = AudioFileClip(bgm_path).subclip(0, final_clip.duration)
            final_clip = final_clip.set_audio(bgm)
        
        # 輸出
        output_name = output_name or f"sales_{self.product_key}.mp4"
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
    
    parser = argparse.ArgumentParser(description="銷售 Shorts 生成器")
    parser.add_argument("--product", "-p", default="ai_prompts",
                       choices=["ai_prompts", "bgm_generator", "youtube_automation"])
    parser.add_argument("--output", "-o", default=None)
    
    args = parser.parse_args()
    
    generator = SalesShortsGenerator(product_key=args.product)
    result = generator.generate(args.output)
    
    print(f"\n📁 影片位置: {result}")


if __name__ == "__main__":
    main()
