#!/usr/bin/env python3
"""
AI Digital Store - Order Processing System
自動化訂單處理與產品交付系統
"""

import json
import os
from datetime import datetime
from pathlib import Path

# 產品資料庫
PRODUCTS_DB = {
    "blog-post-prompt": {
        "name": "Blog Post Prompt Pack",
        "price": 9.99,
        "file": "prompts/blog-post-prompt.md",
        "description": "SEO優化文章生成Prompt"
    },
    "youtube-script": {
        "name": "YouTube Script Pro",
        "price": 7.99,
        "file": "prompts/youtube-script-prompt.md",
        "description": "YouTube影片腳本生成器"
    },
    "notion-workflow": {
        "name": "Notion AI Workflow",
        "price": 14.99,
        "file": "templates/notion-workflow-template.md",
        "description": "Notion工作流模板"
    },
    "business-email": {
        "name": "Business Email Pack",
        "price": 12.99,
        "file": "prompts/business-email-prompt.md",
        "description": "商業郵件模板合集"
    },
    "social-calendar": {
        "name": "Social Media Calendar",
        "price": 14.99,
        "file": "templates/social-media-calendar.md",
        "description": "社群內容日曆模板"
    },
    "python-automation": {
        "name": "Python Automation",
        "price": 19.99,
        "file": "scripts/python-automation-scripts.md",
        "description": "自動化腳本合集"
    },
    "chatgpt-cheatsheet": {
        "name": "ChatGPT Cheat Sheet",
        "price": 9.99,
        "file": "prompts/chatgpt-cheat-sheet.md",
        "description": "提示詞技巧手冊"
    },
    "ai-image-guide": {
        "name": "AI Image Generation Guide",
        "price": 14.99,
        "file": "prompts/ai-image-generation-guide.md",
        "description": "AI繪圖生成指南"
    },
    "notion-ai-setup": {
        "name": "Notion AI Setup Guide",
        "price": 11.99,
        "file": "templates/notion-ai-setup-guide.md",
        "description": "Notion AI自動化指南"
    },
    "midjourney-master": {
        "name": "Midjourney Master",
        "price": 9.99,
        "file": "prompts/midjourney-master.md",
        "description": "Midjourney提示詞"
    }
}

STORE_DIR = "/home/terry/ai-products"

class OrderProcessor:
    def __init__(self, store_dir: str = STORE_DIR):
        self.store_dir = store_dir
        self.orders_file = os.path.join(store_dir, "orders.json")
        self.orders = self.load_orders()
    
    def load_orders(self):
        """載入訂單"""
        if os.path.exists(self.orders_file):
            with open(self.orders_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def save_orders(self):
        """保存訂單"""
        with open(self.orders_file, 'w', encoding='utf-8') as f:
            json.dump(self.orders, f, indent=2, ensure_ascii=False)
    
    def get_product(self, product_id: str) -> dict:
        """獲取產品資訊"""
        return PRODUCTS_DB.get(product_id)
    
    def list_products(self) -> list:
        """列出所有產品"""
        return [
            {
                "id": pid,
                "name": p["name"],
                "price": p["price"],
                "description": p["description"]
            }
            for pid, p in PRODUCTS_DB.items()
        ]
    
    def create_order(self, customer_info: dict, product_ids: list) -> dict:
        """創建訂單"""
        order = {
            "id": f"ORD-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "timestamp": datetime.now().isoformat(),
            "customer": customer_info,
            "items": [],
            "total": 0,
            "status": "pending",
            "payment_method": None,
            "payment_confirmed": False
        }
        
        for pid in product_ids:
            product = self.get_product(pid)
            if product:
                order["items"].append(product)
                order["total"] += product["price"]
        
        self.orders.append(order)
        self.save_orders()
        
        return order
    
    def confirm_payment(self, order_id: str, payment_method: str) -> dict:
        """確認付款"""
        for order in self.orders:
            if order["id"] == order_id:
                order["status"] = "paid"
                order["payment_method"] = payment_method
                order["payment_confirmed"] = True
                order["paid_at"] = datetime.now().isoformat()
                self.save_orders()
                return order
        return None
    
    def deliver_product(self, order_id: str) -> dict:
        """交付產品"""
        for order in self.orders:
            if order["id"] == order_id and order["status"] == "paid":
                order["status"] = "delivered"
                order["delivered_at"] = datetime.now().isoformat()
                self.save_orders()
                
                # 返回產品文件內容
                delivered_files = []
                for item in order["items"]:
                    filepath = os.path.join(self.store_dir, item["file"])
                    if os.path.exists(filepath):
                        with open(filepath, 'r', encoding='utf-8') as f:
                            delivered_files.append({
                                "name": item["name"],
                                "content": f.read()
                            })
                
                return {
                    "order": order,
                    "files": delivered_files
                }
        return None
    
    def get_order_status(self, order_id: str) -> dict:
        """獲取訂單狀態"""
        for order in self.orders:
            if order["id"] == order_id:
                return order
        return None

# Telegram Bot 回覆模板
RESPONSE_TEMPLATES = {
    "greeting": """👋 您好！歡迎來到 AI Digital Store！

我是自動客服機器人，很高興為您服務！

我們提供以下產品：
{product_list}

請告訴我您想要的產品編號或名稱！""",
    
    "product_detail": """📦 產品資訊

名稱：{name}
價格：${price}
說明：{description}

請確認購買後，我會發送付款資訊給您。""",
    
    "payment_info": """💳 付款資訊

訂單編號：{order_id}
總金額：${total}

請選擇付款方式：
1. 加密貨幣（BTC/ETH/USDT）
2. 銀行轉帳
3. 其他方式

確認付款後，請發送付款截圖給我。""",
    
    "payment_confirmed": """✅ 付款已確認！

感謝您的購買！🎉

我現在發送產品給您...

---
{product_list}

再次感謝您的支持！""",
    
    "help": """📚 指令說明

- 產品列表：顯示所有產品
- 購買 [產品編號]：購買指定產品
- 訂單狀態 [訂單編號]：查看訂單進度
- 幫助：顯示說明

有任何問題歡迎隨時詢問！"""
}

def generate_product_list() -> str:
    """生成產品列表"""
    processor = OrderProcessor()
    products = processor.list_products()
    
    lines = []
    for i, p in enumerate(products, 1):
        lines.append(f"{i}. {p['name']} - ${p['price']}")
        lines.append(f"   {p['description']}")
        lines.append("")
    
    return "\n".join(lines)

if __name__ == "__main__":
    processor = OrderProcessor()
    
    print("=" * 50)
    print("🤖 AI Digital Store - Order System")
    print("=" * 50)
    
    # 顯示產品列表
    print("\n📦 可用產品：")
    print(generate_product_list())
    
    # 測試創建訂單
    test_order = processor.create_order(
        customer_info={"email": "test@example.com", "name": "Test User"},
        product_ids=["blog-post-prompt", "youtube-script"]
    )
    print(f"\n✅ 測試訂單創建: {test_order['id']}")
    print(f"   總金額: ${test_order['total']}")
