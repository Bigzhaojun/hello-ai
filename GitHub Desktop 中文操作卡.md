# GitHub Desktop 中文操作卡

> 这份文件是给你自己看的。忘了怎么操作就打开它。

## 界面上的字都什么意思

| 英文 | 中文 | 要不要管 |
|---|---|---|
| Current repository | 当前仓库 | 看，知道自己在哪个项目 |
| Current branch | 当前分支（主线 main） | 不用管 |
| Fetching origin | 正在检查云端有没有更新 | 不用管 |
| **Changes** | **改动（我改了什么）** | **要看** |
| History | 历史（以前存过什么） | 想看时点 |
| Filter | 筛选 | 不用管 |
| No local changes | 本地没有改动（正常状态） | 不是错误 |
| **Summary (required)** | **摘要，必填，一句话说明改了什么** | **要填** |
| Description | 详细描述 | 可以不填 |
| **Commit to main** | **提交到主线 ← 这是「存档」按钮** | **要按** |
| **Push origin** | **上传到云端 ← 存档之后才出现** | **要按** |
| Show in Explorer | 在文件夹里打开 | 偶尔用 |
| View on GitHub | 在浏览器里查看 | 偶尔用 |

## 以后只需要记住四个动作

1. **改文件** —— 自己改，或者让 AI 改
2. **打开 GitHub Desktop** —— 看左侧 Changes 里出现了哪些文件
3. **填 Summary，点 Commit to main** —— 左下角蓝色大按钮，等于「存档」
4. **点 Push origin** —— 顶部出现的按钮，等于「上传到云端」

存档和上传是两个动作，可以分开做。只存档不上传，东西就只留在自己电脑上。

## 三种「卡住」的真相

| 现象 | 真相 |
|---|---|
| Fetching origin 一直转 | 在等 GitHub 回应，网络慢而已。菜单 Repository → Fetch origin 可重试 |
| No local changes | 不是错误，是「确实没东西可存」 |
| 蓝按钮点不动 | Summary 没填，或者真的没有改动 |

## 这个仓库是干什么的

练习场。用来看清「本地改 → 存档 → 上传」这条链路长什么样。

真正的项目以后放在 `D:\code` 下各自独立的文件夹里，一个项目一个仓库。

---

## 实战记录：第 1 次完整走通（2026-11-02）

这是你自己亲手做完的第一轮，留个证据。

| 环节 | 结果 |
|---|---|
| 提交编号 | `111f9c1` |
| 提交说明 | Create GitHub Desktop 中文操作卡.md |
| 存档到本地 | ✅ 成功 |
| 上传到云端 | ✅ 成功 |
| 云端文件数 | 3 个（README.md、hello.py、本文件） |
| 本地与云端对比 | 完全一致，没有落后的、也没有多出来的 |

### 当时界面长什么样

左上角 `hello-ai`、中间 `main`、右上按钮写着 `Fetch origin`、中间大字 `No local changes`。

**记住这个画面就是「全部干净」的样子。** 以后每次 Push 完，界面都会回到这个状态——这是好事，不是卡住了。

### 下次自己做的顺序（30 秒版）

1. 改文件 → 保存
2. 打开 GitHub Desktop，左上看清楚是 `hello-ai`
3. 左侧出现改动清单 → 左下 Summary 写一句话 → 点蓝色 `Commit to main`
4. 顶部按钮变成 `Push origin ↑1` → 点它
5. 等按钮变回 `Fetch origin` → 完事

### 常见误会

- 「按钮点不动」→ 先看 Summary 是不是空的，再看有没有改动
- 「右上一直转圈」→ 只是网络慢，`Repository → Fetch origin` 重试
- 「是不是没存上」→ 点右上 `View on GitHub`，浏览器看到文件就是存上了
