# NewsFeed — 个人 AI RSS

个人 AI 推送源，目前包含：

- 每日新闻：国内 / 国外重要新闻
- 每周 Great Books：深度书评、思想随笔与导读

## 在 NetNewsWire 中订阅

```text
https://raw.githubusercontent.com/haloworld-C/NewFeed/main/feed.xml
```

## 标签约定

RSS 使用标准 `<category>` 字段，一个条目可以有多个标签。

- 栏目：`新闻`、`Great Books`
- 领域：`国内`、`国外`、`哲学`、`文学`、`文明史`、`政治思想`、`社会观察`、`科技与人性`、`中国经典`
- 主题：按内容补充，例如 `但丁`、`现代性`、`宗教`、`权威`、`语言`、`开放社会`、`俄乌`、`地缘政治`

Great Books 完整文章归档于 `great-books/`，RSS 中保留标题、摘要、链接和标签。

每日新闻约上午 09:36（Asia/Shanghai）更新；Great Books 每周日 09:00（Asia/Shanghai）生成。
