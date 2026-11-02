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
