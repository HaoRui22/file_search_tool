# 文件搜索工具

## 项目描述
这是学习Python过程中用于练习的小项目，内容是使用Python实现命令行文件搜索工具。

包含两种模式：
- 文件文本内容搜索：根据关键字匹配文件文本内容
- 文件名搜索：根据关键字匹配文件名

可以指定特定目录。

实现了命令行的彩色文本输出，结果超过20行时会自动分页。

使用模块：
- `os`
- `logging`
- `unittest`
- `colorama`
- `argparse`

## 用法

运行`mian.py`并键入参数：
- `-m`：选择模式
  - `content`：文本内容搜索
  - `name`：文件名搜索
- `-d`：输入搜索路径
- `-k`：输入搜索关键字

示例：
```shell
python main.py -m content -d . -k kw
# 模式：文本内容搜索
# 路径：当前路径
# 搜索关键字：kw
```

------

# File Search Tool

## Project Description

This is a small practice project for learning Python. The project involves building a command-line file search tool using Python.

Two modes:
- File Content Search: Matches files based on keywords in their content.
- Filename Search: Matches files based on keywords in their filenames.

You can specify a particular directory to search within.

Used mods:
- `os`
- `logging`
- `unittest`
- `colorama`
- `argparse`

## Usage

Run `main.py` and enter the parameters:
- `-m`: Select mode
  - `content`: Search by text content
  - `name`: Search by filename
- `-d`: Enter the search path
- `-k`: Enter the search keyword

```shell
python main.py -m content -d . -k kw  
# Mode: Search by text content  
# Path: Current directory  
# Search keyword: kw  
```