# M3 — Logging

> `print()` 是寫給你看的，`logging` 是寫給「未來的你」看的

## 為什麼要用 logging 而不是 print？

| `print()` | `logging` |
|:----------|:----------|
| 只能印到 console | 可以同時印到 console + 寫檔 |
| 沒有時間戳 | 自動加時間戳 |
| 沒有嚴重度分級 | DEBUG / INFO / WARNING / ERROR / CRITICAL |
| 關不掉 | 一個開關切 level |
| 正式上線要全部刪 | 正式上線把 level 調成 WARNING 即可 |

## 你會學到

- 五個 log level 的使用時機
- `logging.basicConfig()` 快速設定
- 用 `Logger` + `Handler` + `Formatter` 做精細控制
- **檔案輪替**（`RotatingFileHandler`） — 不讓 log 檔長到爆硬碟
- `logging.conf` — 用設定檔管理 logger，程式不用改

## 課程檔案

- **`S3_logging.ipynb`** — 基礎：level、basicConfig、格式化
- **`S3b_logger_advanced.ipynb`** — 進階：Handler、Formatter、檔案輪替
- **`logging.conf`** — 設定檔範例（用於進階章節）

## 實務建議

```python
# ❌ 不要這樣
print(f"開始處理 {filename}")

# ✅ 請這樣
import logging
logger = logging.getLogger(__name__)
logger.info("開始處理 %s", filename)
```

**為什麼？**
- `%s` 延遲格式化，level 被關掉時完全不消耗 CPU
- `logger.info` 可以被 root logger 的設定集中管理
- 測試時可以 mock logger 驗證「某個錯誤有沒有被記下來」

## 常踩的坑

1. **重複呼叫 `basicConfig`** → 只有第一次有效，之後被忽略
2. **沒設 handler** → log 訊息被吃掉
3. **level 設錯** → `logger.debug()` 預設看不到（WARNING 以上才印）
