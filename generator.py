#!/usr/bin/env python3
"""
AI Digital Product Generator
使用 MiniMax API 自動生成數位產品
"""

import json
import os
from datetime import datetime

# 產品模板
PRODUCT_TEMPLATES = {
    "prompt_pack": {
        "name": "AI Prompt Pack - {niche}",
        "description": "精選 AI 提示詞模板，幫助你快速產出高品質內容",
        "price": 9.99,
        "category": "prompts"
    },
    "workflow": {
        "name": "Notion Workflow - {niche}",
        "description": "自動化工作流模板，提升工作效率",
        "price": 14.99,
        "category": "templates"
    },
    "guide": {
        "name": "Complete Guide - {niche}",
        "description": "深入淺出的完整教學指南",
        "price": 19.99,
        "category": "guides"
    }
}

# 熱門領域
NICHES = [
    "SaaS Marketing",
    "E-commerce",
    "Content Creator",
    "Freelancer",
    "Developer",
    "Designer",
    "Finance",
    "Health & Fitness",
    "Education",
    "Real Estate"
]

def generate_prompt_content(niche: str, template_type: str) -> str:
    """生成 Prompt 內容"""
    
    prompts = {
        "prompt_pack": f"""# 🎯 {niche} AI Prompt Pack

## 產品說明
這是一套專為 {niche} 設計的 AI 提示詞模板。

## 包含內容

### 1. 內容生成 Prompt
```
你是一位{niche}專家。你的任務是...
```

### 2. 郵件寫作 Prompt
```
撰寫一封專業的{niche}相關郵件...
```

### 3. 社群媒體 Prompt
```
為{niche}創建吸引人的社群內容...
```

### 4. 銷售文案 Prompt
```
撰寫高轉化率的{niche}銷售文案...
```

---

## 定價：$9.99
版本：1.0
更新日期：{datetime.now().strftime('%Y-%m-%d')}
""",
        "workflow": f"""# 📊 {niche} Notion Workflow Template

## 模板說明
這是一套專為 {niche} 設計的 Notion 工作流模板。

## 包含內容

### 1. 每日任務儀表板
- 任務清單
- 進度追蹤
- AI 輔助建議

### 2. 項目管理系統
- 看板視圖
- 時間線
- 自動化提醒

### 3. 知識庫
- 靈感收集
- 資料整理
- AI 摘要

---

## 定價：$14.99
版本：1.0
更新日期：{datetime.now().strftime('%Y-%m-%d')}
""",
        "guide": f"""# 📚 {niche} Complete Guide

## 指南說明
這是一本完整的 {niche} 終極指南。

## 目錄

### 第1章：基礎概念
- 什麼是 {niche}
- 為什麼重要
- 核心原則

### 第2章：實踐方法
- 步驟一：xxx
- 步驟二：xxx
- 步驟三：xxx

### 第3章：進階技巧
- 優化策略
- 常見錯誤
- 案例分析

### 第4章：工具與資源
- 推薦工具
- 學習資源
- 社群推薦

---

## 定價：$19.99
版本：1.0
更新日期：{datetime.now().strftime('%Y-%m-%d')}
"""
    }
    
    return prompts.get(template_type, "")

def create_product(niche: str, template_type: str, output_dir: str) -> str:
    """創建產品並保存"""
    
    template = PRODUCT_TEMPLATES[template_type]
    content = generate_prompt_content(niche, template_type)
    
    # 創建目錄
    category_dir = os.path.join(output_dir, template["category"])
    os.makedirs(category_dir, exist_ok=True)
    
    # 文件名
    filename = f"{niche.lower().replace(' ', '-')}-{template_type}.md"
    filepath = os.path.join(category_dir, filename)
    
    # 寫入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath

def generate_product_batch(niches: list = None, output_dir: str = None):
    """批量生成產品"""
    
    if niches is None:
        niches = NICHES
    
    if output_dir is None:
        output_dir = "/home/terry/ai-products/generated"
    
    os.makedirs(output_dir, exist_ok=True)
    
    generated = []
    for niche in niches:
        for template_type in PRODUCT_TEMPLATES.keys():
            try:
                filepath = create_product(niche, template_type, output_dir)
                generated.append({
                    "niche": niche,
                    "type": template_type,
                    "file": filepath,
                    "status": "success"
                })
                print(f"✅ Generated: {filepath}")
            except Exception as e:
                generated.append({
                    "niche": niche,
                    "type": template_type,
                    "error": str(e),
                    "status": "failed"
                })
                print(f"❌ Failed: {niche} - {template_type}: {e}")
    
    # 保存生成記錄
    log_file = os.path.join(output_dir, "generation_log.json")
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "generated": generated
        }, f, indent=2, ensure_ascii=False)
    
    return generated

if __name__ == "__main__":
    print("🚀 AI Product Generator")
    print("=" * 50)
    
    # 生成一批產品
    results = generate_product_batch(
        niches=["SaaS Marketing", "E-commerce", "Content Creator"],
        output_dir="/home/terry/ai-products/generated"
    )
    
    print("\n" + "=" * 50)
    print(f"📊 Total: {len(results)} products")
    print(f"✅ Success: {len([r for r in results if r['status'] == 'success'])}")
    print(f"❌ Failed: {len([r for r in results if r['status'] == 'failed'])}")
