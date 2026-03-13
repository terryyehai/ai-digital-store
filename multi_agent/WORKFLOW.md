# 🔄 Agent 工作分配流程

## 架構圖

```
         ┌─────────────────────────────────────────┐
         │           用戶 (Telegram)                │
         │         「幫我生成音樂」                  │
         └──────────────────┬──────────────────────┘
                            │
                            ▼
         ┌─────────────────────────────────────────┐
         │         🎯 指揮官 (Main Controller)       │
         │  1. 接收請求                           │
         │  2. 分析意圖 (Intent Analysis)          │
         │  3. 選擇 Agent                          │
         └──────────────────┬──────────────────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
        ┌─────────┐  ┌─────────┐  ┌─────────┐
        │  🎵阿音  │  │  🎬阿導  │  │  🏪老闆娘│
        │   BGM   │  │  Video  │  │  Store  │
        │  Agent  │  │  Agent  │  │  Agent  │
        └─────────┘  └─────────┘  └─────────┘
```

## 分配邏輯

### 1. 意圖分析 (Intent Matching)

```python
def analyze_intent(request):
    # 關鍵字匹配
    if "音樂" in request or "BGM" in request:
        return "bgm"      # → 阿音
    
    if "影片" in request or "Shorts" in request:
        return "video"    # → 阿導
    
    if "YouTube" in request or "上傳" in request:
        return "youtube"  # → 小編
    
    if "商店" in request or "產品" in request:
        return "store"     # → 老闆娘
```

### 2. 混合任務處理

```
用戶：「生成一個 AI 產品的短影片，配上背景音樂」

分析：
- 「短影片」→ video agent
- 「背景音樂」→ bgm agent

執行順序：
1. 先叫 阿導 生成影片
2. 再叫 阿音 生成配樂
3. 合併輸出
```

### 3. 優先級

| 優先 | 任務類型 | Agent |
|------|-----------|-------|
| 1 | 音樂生成 | 阿音 |
| 2 | 影片剪輯 | 阿導 |
| 3 | YouTube 上傳 | 小編 |
| 4 | 商店咨詢 | 老闆娘 |

## 工作流程範例

### 範例 1：完整行銷流程

```
用戶：「幫我做一個產品推廣影片」

Step 1: 老闆娘 (Store)
        └→ 選擇產品、獲取價格資訊

Step 2: 阿音 (BGM)  
        └→ 生成背景音樂

Step 3: 阿導 (Video)
        └→ 剪輯 Shorts 影片

Step 4: 小編 (YouTube)
        └→ 上傳到頻道

Step 5: 指揮官
        └→ 回報完成 ✅
```

### 範例 2：快速咨詢

```
用戶：「產品多少錢？」

Step 1: 指揮官 → 分析
Step 2: 老闆娘 → 列出價格
Step 3: 指揮官 → 回報 ✅
```

## 檔案位置

```
multi_agent/
├── main.py              # 指揮官 (分配邏輯)
└── agents/
    ├── bgm_agent.py      # 阿音
    ├── video_agent.py    # 阿導
    ├── youtube_agent.py  # 小編
    └── store_agent.py   # 老闆娘
```

---

*2026-03-13 建立*
