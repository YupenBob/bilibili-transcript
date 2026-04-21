# 📥 Bilibili Video Download + Transcript

> 基于 GitHub Actions 的 B站视频下载 + Whisper 转写工具
> 下载在 GitHub Actions 服务器跑，不受本地网络限制

[![GitHub stars](https://img.shields.io/github/stars/YupenBob/bilibili-transcript?logo=github&style=flat-square)](https://github.com/YupenBob/bilibili-transcript)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Actions](https://github.com/YupenBob/bilibili-transcript/workflows/Deploy/badge.svg)](https://github.com/YupenBob/bilibili-transcript/actions)

[🐛 Issues](https://github.com/YupenBob/bilibili-transcript/issues) · [⭐ GitHub](https://github.com/YupenBob/bilibili-transcript)

---

## ✨ 特性

- 📥 **视频下载** — 输入 B站 视频 URL，自动下载高清视频
- ✍️ **Whisper 转写** — 自动将视频内容转写为文字字幕
- ☁️ **GitHub Actions 驱动** — 服务器端运行，不受本地网络限制
- 🔑 **大会员支持** — 可配置 Cookies 下载会员专属内容
- 🆓 **完全免费** — 使用公开的 GitHub Actions 算力

## 🚀 快速开始

1. **Fork 或直接使用本仓库**
2. **前往 Actions → Bilibili Video Download + Transcript → Run workflow**
3. **填入 B站 视频 URL**，选择 Whisper 模型，点击 Run

## 🔧 配置说明

### B站 Cookies（可选）

部分视频需要登录后才能下载（如大会员内容）。

1. 浏览器登录 B站
2. 打开开发者工具 → Application → Cookies → bilibili.com
3. 复制所有 cookie 的 `name=value`，粘贴到文本文件
4. Base64 编码：

```bash
base64 -w0 cookies.txt   # Linux/Mac
certutil -encodestring cookies.txt > cookies_b64.txt  # Windows
```

5. 在 GitHub Secrets 中添加 `BILIBILI_COOKIES` 环境变量

### Whisper 模型选择

| 模型 | 大小 | 速度 | 适用场景 |
|------|------|------|---------|
| tiny | ~39 MB | 最快 | 快速预览 |
| base | ~74 MB | 快 | 日常使用 |
| small | ~244 MB | 中 | 精度优先 |
| medium | ~769 MB | 慢 | 高精度需求 |

## 📜 License

MIT © 2024-2026 [YupenBob](https://github.com/YupenBob)
