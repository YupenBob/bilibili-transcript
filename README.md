# 📥 Bilibili Video Download + Transcript

基于 GitHub Actions 的 B站视频下载 + Whisper 转写工具。下载在 GitHub Actions 服务器跑，不受本地网络限制。

## 🚀 快速开始

1. **Fork 或直接使用本仓库**
2. **前往 Actions → Bilibili Video Download + Transcript → Run workflow**
3. **填入 B站视频 URL**，选择 Whisper 模型，点击 Run

## 🔧 配置说明

### B站 Cookies（可选）

部分视频需要登录后才能下载（如大会员内容）。

1. 浏览器登录 B站
2. 打开开发者工具 → Application → Cookies → bilibili.com
3. 复制所有 cookie 的 name=value，粘贴到文本文件
4. Base64 编码：
   ```bash
   base64 -w0 cookies.txt   # Linux/Mac
   certutil -encode cookies.txt cookies_b64.txt   # Windows
   ```
5. 在 workflow 的 `cookies_b64` 输入框填入编码结果

### Whisper 模型选择

| 模型 | 大小 | 速度 | 精度 |
|------|------|------|------|
| tiny | ~75MB | 最快 | 较低 |
| base | ~140MB | 快 | 中等 |
| small | ~450MB | 中等 | 较高 |
| medium | ~1.5GB | 慢 | 高 |
| large | ~2.9GB | 最慢 | 最高 |

默认 `base`，中文推荐 `small`。

## 📁 输出文件

workflow 运行完成后可在 Artifacts 下载：

- `transcript_full.txt` — 完整转写文本
- `transcript_segmented.txt` — 带时间戳的分段文本
- `transcript.json` — JSON 格式（包含每段置信度）
- `audio.wav` — 16kHz 单声道音频
- `summary.md` — 运行摘要

## ❓ 常见问题

**Q: 下载失败？**
A: 试试填入 B站 cookies，公开视频一般不需要。

**Q: 转写慢？**
A: `tiny` 最快，`large` 最慢但最准。长视频建议选 `small`。

**Q: 能否批量下载？**
A: 可以用 workflow_dispatch 多次触发，或修改为 `repository_dispatch` 事件配合脚本。

## 📜 License

MIT
