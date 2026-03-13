# 🤖 多 Agent 架構設計

## 架構圖

```
                    ┌─────────────────────────────────────┐
                    │         Main Controller            │
                    │        (主要協調 Agent)             │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────┬──────────────┼──────────────┬──────────┐
        │          │              │              │          │
        ▼          ▼              ▼              ▼          ▼
   ┌────────┐ ┌────────┐  ┌──────────┐ ┌────────┐ ┌────────┐
   │  BGM   │ │ Video  │  │ YouTube  │ │ Store  │ │ Content│
   │ Agent  │ │ Editor │  │ Manager  │ │ Manager│ │ Writer │
   │        │ │ Agent  │  │   Agent  │ │  Agent │ │  Agent │
   └────────┘ └────────┘  └──────────┘ └────────┘ └────────┘
```

## Agent 職責

| Agent | 功能 | 技能 |
|-------|------|------|
| **BGM Agent** | 音樂生成 | PySynth, 音樂理論 |
| **Video Editor Agent** | 影片剪輯 | MoviePy, 腳本模板 |
| **YouTube Manager Agent** | 上傳管理 | YouTube API |
| **Store Manager Agent** | 訂單處理 | Email, Ko-fi |
| **Content Writer Agent** | 腳本撰寫 | 病毒式行銷 |

## 通訊方式

```
Agent <-> Main Controller <-> User (Telegram)
         │
         └── cron jobs (定時任務)
```

## 檔案位置

```
~/.openclaw/agents/
├── main/                    # 主控 Agent
│   └── main_agent.py
├── bgm/                    # BGM 生成 Agent
│   └── bgm_agent.py
├── video/                  # 影片剪輯 Agent
│   └── video_agent.py
├── youtube/                # YouTube 管理 Agent
│   └── youtube_agent.py
├── store/                  # 商店管理 Agent
│   └── store_agent.py
└── content/                # 內容創作 Agent
    └── content_agent.py
```

## 啟動方式

```bash
# 啟動單一 Agent
openclaw agent start bgm
openclaw agent start video
openclaw agent start youtube

# 啟動全部
openclaw agent start all
```

## 訊息格式

```json
{
  "from": "bgm",
  "to": "main",
  "action": "generate",
  "payload": {
    "style": "pop",
    "duration": 30
  }
}
```

---

*2026-03-13 設計完成*
