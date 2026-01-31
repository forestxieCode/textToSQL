# 项目结构说明 / Project Structure Documentation

本文档详细说明了重新组织后的项目结构。
This document explains the reorganized project structure.

## 📁 目录结构 / Directory Structure

```
text_to_sql/
├── src/                          # 源代码目录 / Source code directory
│   └── text_to_sql/              # 主包 / Main package
│       ├── __init__.py           # 包初始化，导出主要API / Package init, exports main API
│       ├── core/                 # 核心业务逻辑 / Core business logic
│       │   ├── __init__.py
│       │   ├── agent.py          # LangGraph工作流主逻辑 / Main workflow logic
│       │   └── sql_generator.py  # SQL生成器 / SQL generator
│       ├── database/             # 数据库操作模块 / Database operations module
│       │   ├── __init__.py
│       │   └── manager.py        # 数据库管理器 / Database manager
│       └── utils/                # 通用工具 / Utilities
│           ├── __init__.py
│           ├── config.py         # 配置管理 / Configuration
│           ├── constants.py      # 常量定义 / Constants
│           ├── exceptions.py     # 自定义异常 / Custom exceptions
│           ├── formatter.py      # 输出格式化 / Output formatter
│           └── logger.py         # 日志系统 / Logging system
├── scripts/                      # 可执行脚本 / Executable scripts
│   ├── cli.py                    # 命令行交互界面 / CLI interface
│   ├── demo.py                   # 功能演示 / Demo script
│   ├── init_database.py          # 初始化示例数据库 / Initialize sample database
│   └── visualize_workflow.py     # 可视化工作流 / Visualize workflow
├── tests/                        # 测试文件 / Test files
│   ├── __init__.py
│   └── test_database.py          # 数据库测试 / Database tests
├── cli.py                        # CLI包装器 / CLI wrapper (for convenience)
├── demo.py                       # Demo包装器 / Demo wrapper
├── init_database.py              # 初始化包装器 / Init wrapper
├── visualize_workflow.py         # 可视化包装器 / Visualize wrapper
├── setup.py                      # 包安装配置 / Package setup configuration
├── requirements.txt              # 依赖项 / Dependencies
├── README.md                     # 主要文档 / Main documentation
└── OPTIMIZATION_SUMMARY.md       # 优化总结 / Optimization summary
```

## 🎯 设计原则 / Design Principles

### 1. 模块化 / Modularity
- **清晰的职责分离**: 每个模块有明确的职责
- **Clear separation of concerns**: Each module has a specific responsibility
- **core**: 核心业务逻辑和工作流 / Core business logic and workflows
- **database**: 数据库相关操作 / Database-related operations
- **utils**: 通用工具和配置 / Common utilities and configuration

### 2. 可维护性 / Maintainability
- **易于定位**: 按功能组织文件，快速找到需要修改的代码
- **Easy to locate**: Files organized by function for quick navigation
- **独立性**: 模块之间低耦合，修改一个模块不影响其他模块
- **Independence**: Low coupling between modules

### 3. 可扩展性 / Extensibility
- **添加新功能**: 在相应模块中添加新文件或类
- **Add new features**: Add new files or classes in relevant modules
- **新的数据库支持**: 在 database 模块中添加新的管理器
- **New database support**: Add new managers in database module
- **新的格式化器**: 在 utils 模块中添加
- **New formatters**: Add in utils module

### 4. 易用性 / Usability
- **包装器脚本**: 根目录的包装器脚本方便直接运行
- **Wrapper scripts**: Root-level wrappers for easy execution
- **包导入**: 通过 `from text_to_sql import ...` 使用
- **Package imports**: Use via `from text_to_sql import ...`

## 📦 模块说明 / Module Description

### Core Module (src/text_to_sql/core/)
**核心业务逻辑 / Core Business Logic**

- **agent.py**: 
  - LangGraph 状态图定义 / LangGraph state graph definition
  - 工作流节点实现 (generate_sql, execute_sql, format_output)
  - Workflow node implementations
  - 主要入口函数 `run_query()` / Main entry function

- **sql_generator.py**:
  - LLM SQL 生成器 / LLM SQL generator
  - 提示词模板管理 / Prompt template management
  - SQL 清理和验证 / SQL cleaning and validation

### Database Module (src/text_to_sql/database/)
**数据库操作 / Database Operations**

- **manager.py**:
  - 数据库连接管理 / Database connection management
  - Schema 获取和缓存 / Schema retrieval and caching
  - SQL 执行和安全检查 / SQL execution and safety checks
  - 支持多种数据库 (SQLite, PostgreSQL, MySQL)
  - Support for multiple databases

### Utils Module (src/text_to_sql/utils/)
**通用工具 / Common Utilities**

- **config.py**: 配置管理，从环境变量加载 / Configuration management
- **constants.py**: 常量定义（提示词、消息模板等）/ Constants definition
- **exceptions.py**: 自定义异常类 / Custom exception classes
- **formatter.py**: 输出格式化工具 / Output formatting utilities
- **logger.py**: 统一日志系统 / Unified logging system

### Scripts (scripts/)
**可执行脚本 / Executable Scripts**

- **cli.py**: 交互式命令行界面 / Interactive CLI
- **demo.py**: 演示完整工作流程 / Demonstrate complete workflow
- **init_database.py**: 创建示例数据库 / Create sample database
- **visualize_workflow.py**: 可视化 LangGraph 工作流 / Visualize workflow

### Tests (tests/)
**测试 / Tests**

- **test_database.py**: 数据库功能测试 / Database functionality tests
- 未来可添加更多测试 / More tests can be added

## 🚀 使用方式 / Usage

### 方式 1: 直接运行脚本 / Method 1: Run scripts directly
```bash
# 从项目根目录 / From project root
python cli.py
python demo.py
python init_database.py
python visualize_workflow.py
python tests/test_database.py
```

### 方式 2: 作为 Python 包使用 / Method 2: Use as Python package
```python
# 导入主要功能 / Import main functions
from text_to_sql import run_query, db_manager, config

# 运行查询 / Run query
result = run_query("显示所有用户")

# 访问数据库 / Access database
schema = db_manager.get_schema()

# 访问配置 / Access config
db_url = config.database.url
```

### 方式 3: 安装为包 / Method 3: Install as package
```bash
# 在项目根目录 / In project root
pip install -e .

# 然后可以在任何地方使用 / Then use anywhere
python -c "from text_to_sql import run_query; print(run_query('显示所有用户'))"
```

## 🔄 迁移指南 / Migration Guide

### 旧导入 → 新导入 / Old Imports → New Imports

```python
# 旧方式 / Old way
from text_to_sql_agent import run_query
from database import db_manager
from config import config
from logger import logger
from formatter import OutputFormatter

# 新方式 / New way
from text_to_sql import run_query
from text_to_sql.database import db_manager
from text_to_sql.utils import config, logger
from text_to_sql.utils.formatter import OutputFormatter
```

### 脚本执行 / Script Execution

```bash
# 旧方式（所有脚本在根目录）/ Old way (all scripts in root)
python cli.py
python demo.py

# 新方式（仍然可以这样用！）/ New way (still works!)
python cli.py
python demo.py

# 或者 / Or
python scripts/cli.py
python scripts/demo.py
```

## ✅ 优势 / Advantages

1. **更清晰的代码组织** / Clearer code organization
   - 一目了然的模块结构 / Intuitive module structure
   - 易于理解项目架构 / Easy to understand project architecture

2. **更好的可维护性** / Better maintainability
   - 相关代码集中在一起 / Related code grouped together
   - 修改影响范围小 / Small change impact radius

3. **更容易扩展** / Easier to extend
   - 添加新功能时知道放在哪里 / Know where to add new features
   - 模块间低耦合 / Low coupling between modules

4. **更专业的项目结构** / More professional structure
   - 符合 Python 包开发最佳实践 / Follows Python packaging best practices
   - 易于分发和安装 / Easy to distribute and install

5. **向后兼容** / Backward compatible
   - 根目录的包装器脚本保持原有使用方式 / Root wrappers maintain original usage
   - 平滑迁移，无破坏性变更 / Smooth migration, no breaking changes

## 📝 最佳实践 / Best Practices

1. **添加新功能时** / When adding new features:
   - 确定功能属于哪个模块 / Determine which module it belongs to
   - 在对应模块添加新文件或扩展现有文件 / Add new file or extend existing one
   - 更新模块的 `__init__.py` 导出新功能 / Update module's `__init__.py`

2. **修改现有代码时** / When modifying existing code:
   - 保持模块间的清晰边界 / Maintain clear module boundaries
   - 避免跨模块的紧密耦合 / Avoid tight coupling across modules
   - 更新相关文档和测试 / Update related docs and tests

3. **编写测试时** / When writing tests:
   - 测试文件放在 tests/ 目录 / Place test files in tests/
   - 测试文件名以 test_ 开头 / Test file names start with test_
   - 每个模块有对应的测试文件 / Each module has corresponding test file

## 🎓 学习路径 / Learning Path

对于新开发者，建议按以下顺序阅读代码：
For new developers, suggested reading order:

1. `README.md` - 了解项目概述 / Understand project overview
2. `src/text_to_sql/__init__.py` - 查看主要 API / See main API
3. `src/text_to_sql/utils/` - 理解基础工具 / Understand utilities
4. `src/text_to_sql/database/` - 学习数据库操作 / Learn database ops
5. `src/text_to_sql/core/` - 深入核心逻辑 / Dive into core logic
6. `scripts/` - 查看实际使用示例 / See usage examples
