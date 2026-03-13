#!/usr/bin/env python3
"""
圖片素材下載工具 - 從 Pexels 免費下載
"""
import os
import requests
import json

# Pexels API (免費 API)
PEXELS_API_KEY = "REPLACE_WITH_YOUR_PEXELS_KEY"  # 可選

# 常用搜尋關鍵詞
IMAGE_QUERIES = {
    "ai_writing": ["artificial intelligence", "laptop", "computer", "keyboard", "writing", "blog"],
    "productivity": ["office", "workspace", "coffee", "clock", "productivity", "business"],
    "tools": ["robot", "technology", "gears", "computer", "digital", "code"],
    "chinese": ["chinese traditional", "lantern", "temple", "china", "asian"],
    "nature": ["nature", "landscape", "mountain", "water"],
}

def download_from_pexels(query, count=5, output_dir="."):
    """從 Pexels 下載圖片"""
    headers = {"Authorization": PEXELS_API_KEY} if PEXELS_API_KEY != "REPLACE_WITH_YOUR_PEXELS_KEY" else {}
    
    url = f"https://api.pexels.com/v1/search?query={query}&per_page={count}"
    
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            photos = data.get("photos", [])
            
            for i, photo in enumerate(photos):
                src = photo["src"]["large"]
                filename = f"{query}_{i+1}.jpg"
                
                # 下載
                img_resp = requests.get(src)
                if img_resp.status_code == 200:
                    path = os.path.join(output_dir, filename)
                    with open(path, "wb") as f:
                        f.write(img_resp.content)
                    print(f"✅ {filename}")
            return len(photos)
    except Exception as e:
        print(f"❌ Error: {e}")
    return 0


def create_sample_images(output_dir):
    """建立範例圖片目錄結構"""
    
    print("\n📁 建立素材目錄...")
    
    categories = {
        "ai_writing": "AI寫作相關",
        "productivity": "效率提升相關",
        "tools": "工具相關",
        "chinese": "中國風",
        "nature": "自然風景",
    }
    
    for cat, desc in categories.items():
        path = os.path.join(output_dir, cat)
        os.makedirs(path, exist_ok=True)
        print(f"  📂 {cat}/ - {desc}")
    
    return True


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="圖片素材工具")
    parser.add_argument("--setup", "-s", action="store_true", help="建立目錄結構")
    parser.add_argument("--query", "-q", default="technology", help="搜尋關鍵詞")
    parser.add_argument("--count", "-c", type=int, default=5, help="下載數量")
    parser.add_argument("--output", "-o", default="/home/terry/ai-products/marketing/images", help="輸出目錄")
    
    args = parser.parse_args()
    
    if args.setup:
        create_sample_images(args.output)
    else:
        download_from_pexels(args.query, args.count, args.output)
