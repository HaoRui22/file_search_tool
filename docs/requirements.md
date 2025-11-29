# Python 学习训练项目1：文件搜索工具（核心能力：异常处理、日志、单元测试）- 需求文档

## 项目简介

开发一个命令行工具，能够：

- 在指定目录递归搜索文件
- 在每个文件中查找关键字
- 输出包含关键字的文件路径和行号
- 对异常进行捕获（例如目录不存在）
- 使用 `logging` 模块输出日志
- 提供单元测试 `test_search.py`

## 功能需求

1. 项目输入：
   - 搜索目录
   - 搜索关键字

2. 系统功能：
   - 遍历目录(`os.walk`)
   - 尝试读取文件并搜索关键字
   - 将每次搜索结果记录到 `log.txt`
   - 对以下异常进行处理：
     - 目录不存在
     - 文件读取失败（权限/编码问题）
   - 搜索过程中的每次成功或失败都写入日志

3. 输出要求：
   - 终端打印所有匹配项，格式：
     - `path/to/file:line_number:text`

## 技术要求
- 用模块化方式实现：`searcher.py`, `logger.py`, `main.py`
- 使用 `logging.basicConfig`
- 使用 `try–except` 捕获异常
- 提供最少 3 个单元测试

## 项目结构
```
file_search_tool/
│
├── docs/
│   └── requirements.md
├── main.py
├── searcher.py
├── logger_config.py
├── tests/
│   └── test_searcher.py
└── README.md
```