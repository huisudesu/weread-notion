# 微信读书笔记 Notion 转换器

修改说明
- 适配微信读书 iOS 最新导出格式。
- Readwise 分支：导出到能够导入 Readwise 的 csv。


---

这是一个由椒盐豆豉开发的简单微信读书笔记转换为 Notion table 的小工具。
因为最近开始做[读书笔记剪报 channel](https://t.me/mtfront)，因此需要一些排序、过滤功能，以前偷懒直接纯文本粘贴的微信读书笔记就不好使了。索性写了个 script.

*** ***本 script 仅在 MacOS 上测试过，Windows 不知道有没有问题，就算有我猜轻微改一下能用，如果有试了的朋友欢迎告诉我。*** ***

## Notion 最终效果：
| Name | Highlight | Note | No. |
| --- | --- | --- | --- |
|章节名|你的高亮/划线|你的笔记/想法|用来排序的序号|

变成在 notion 的表格之后后续可以导出、自己加新 field 排序、filter 等，配合其他工具使用参见之前这篇中的效果：[读书笔记 workflow。](https://blog.douchi.space/?p=1134#reading)

## 如何使用
0. 用 git clone 下载基本代码到你的 Mac 上
1. 进入微信读书->笔记，点击“导出”
2. 点击底部的“复制到剪切板”
3. 把剪贴板内容粘贴进一个 txt 文件
4. 在 Mac terminal 里 `python3 weread.py [txt 文件地址]`来运行本工具，生成一个 csv 文件
5. 在 Notion 里创建一个数据库
6. 点击数据库右上角的'...'，选择'Merge with CSV'
7. 等待导入结束并刷新 Notion 页面
8. 再次点击'...' -> 'Sort', 对'No.' field 添加一个 Ascending sort
9. 如果笔记很少的话 Notion 可能会把你的笔记变成单选类型。点击数据库表头的'Note'部分将 property type 改成'Text'即可
10. 去掉无用的 Notion 默认生成的列，如 'Tags'


# weread-notion
This is a simple script created by Mt Front that converts Weread notes export to a csv, so it can be import to Notion into a table.
Made for [my reading notes channel](https://t.me/mtfront) because filtering and sorting is just much more easier this way.

*** ***Warning: This script has only been tested on MacOS. If you're using Windows please let me know if it works.*** ***

## Output table format in Notion:

| Name | Highlight | Note | No. |
| --- | --- | --- | --- |
|Chapter|Underlined highlights|Notes/thoughts|Index used to sort|


## How to use:
0. run git clone of this reopo on your Mac
1. In Weread, go into your notes, click "export"
2. Click "Copy to clipboard” on the bottom
3. Paste the copied notes into a txt file.
4. Run this script by typing 'python3 weread.py [txt file path]' in termincal, the script will create a csv file
5. In Notion, create a table (can be either inline or entire page)
6. Click the '...' on right top cornor of your table, chose "Merge with CSV"
7. Wait for import to complete and refresh the notion page
8. Click the '...'->sort, add an ascending sort on 'No.' (why does stupid notion import in random order?)
9. Notion may convert your 'Note' column to 'Type'. Simply click on the header and change property type to 'Text'
10. Remove default unsed fields like "tags"
