# UAV-Knowledge-Base

> 基于LLM辅助构建的CAAC无人机法规结构化知识库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green)](https://zhouloukai.github.io/UAV-Knowledge-Base/)

---

## 项目简介

本项目是一个系统化的中国民航局（CAAC）无人机法规知识库，旨在通过**LLM辅助+人工审核**的方式，将分散的无人机法规条文转化为结构化、可检索的知识点。项目面向无人机从业者、培训机构、航空爱好者，提供准确、及时的法规参考。

**核心价值**：
- 将复杂的法规体系拆解为200+结构化知识点
- 覆盖CAAC无人机管理5大核心分类
- 识别并记录15+类LLM在处理法规时的典型错误模式
- 所有知识点均经过持照机长的专业审核

---

## 核心成果

| 指标 | 数据 |
|------|------|
| 结构化知识点 | 200+ 条 |
| 知识分类 | 5 大分类 |
| LLM错误模式分析 | 15+ 类 |
| 法规覆盖范围 | CAAC无人机管理全体系 |

### 知识库5大分类

| 分类 | 说明 | 文件 |
|------|------|------|
| 法规概述 | 中国无人机管理法规体系架构、法律层级、关键概念 | [docs/法规概述.md](docs/法规概述.md) |
| 飞行分类 | VLOS/BVLOS定义、执照要求、高度限制、禁飞区 | [docs/飞行分类.md](docs/飞行分类.md) |
| 执照体系 | CAAC执照等级、申请条件、考试内容、有效期 | [docs/执照体系.md](docs/执照体系.md) |
| 空域管理 | 空域分类、UOM平台、飞行计划申报流程 | [docs/空域管理.md](docs/空域管理.md) |
| 安全规范 | 飞行前检查、气象要求、应急处置 | [docs/安全规范.md](docs/安全规范.md) |

---

## 技术方法：四步构建法

本项目采用**人机协同**的方式构建知识库，具体流程如下：

```
Step 1: DeepSeek初步拆解
    ↓ 将法规条文输入LLM，进行初步的结构化拆解
Step 2: 人工审核
    ↓ 由CAAC持照机长对每个知识点进行准确性核验
Step 3: 迭代优化Prompt
    ↓ 根据LLM错误模式，持续优化提示词模板
Step 4: 对比测试
    ↓ 多模型输出对比，确保知识点的准确性和完整性
```

### 已识别的LLM典型错误模式（部分）

1. **法规时效性错误**：引用已废止的旧版法规条文
2. **重量阈值混淆**：微型/轻型/小型的重量分界线记忆错误
3. **空域高度单位错误**：将真高与海拔高度混淆
4. **执照等级对应错误**：将视距内与超视距的权限范围说反
5. **地方与中央法规混淆**：将某地试点政策当作全国性法规
6. **UOM平台功能误述**：对系统功能描述与实际操作不符
7. **考试标准过时**：引用已更新的考试大纲旧标准
8. **特殊空域范围错误**：机场净空区范围描述不准确

---

## 项目结构

```
UAV-Knowledge-Base/
├── README.md              # 项目说明
├── build.py               # 静态站点构建脚本
├── .github/
│   └── workflows/
│       └── pages.yml      # GitHub Pages自动部署
├── docs/                  # 知识库文档目录
│   ├── 法规概述.md
│   ├── 飞行分类.md
│   ├── 执照体系.md
│   ├── 空域管理.md
│   └── 安全规范.md
└── site/                  # 构建输出目录（自动生成）
    ├── index.html
    ├── 法规概述.html
    ├── 飞行分类.html
    ├── 执照体系.html
    ├── 空域管理.html
    └── 安全规范.html
```

---

## 快速开始

### 本地预览

```bash
# 克隆仓库
git clone https://github.com/zhouloukai/UAV-Knowledge-Base.git
cd UAV-Knowledge-Base

# 安装依赖
pip install markdown

# 构建站点
python build.py

# 打开 site/index.html 查看
```

### GitHub Pages自动部署

本项目已配置GitHub Actions工作流，每次推送至 `main` 分支时自动构建并部署到GitHub Pages。

**启用方式**：
1. 在仓库设置中启用GitHub Pages
2. 选择部署来源为 "GitHub Actions"
3. 推送代码即可自动部署

---

## 在线访问

项目文档站点：[https://zhouloukai.github.io/UAV-Knowledge-Base/](https://zhouloukai.github.io/UAV-Knowledge-Base/)

---

## 贡献指南

欢迎提交Issue或Pull Request。对于法规内容的修改，请提供官方法规来源链接以便核验。

### 贡献流程

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/新增内容`
3. 提交修改：`git commit -m '添加：XXX法规知识点'`
4. 推送分支：`git push origin feature/新增内容`
5. 提交 Pull Request

---

## 作者信息

**周富凯**

- CAAC 超视距机长（多旋翼）
- 千机科技教培部
- GitHub: [@zhouloukai](https://github.com/zhouloukai)

如有法规相关问题或合作意向，欢迎通过GitHub Issue联系。

---

## 许可证

本项目采用 [MIT License](LICENSE) 开源许可。

---

## 免责声明

> **重要提示**：本知识库中的法规内容仅供参考学习之用。
>
> 1. 无人机法规处于持续更新中，请以 **CAAC官方最新发布的法规文件** 为准。
> 2. 本知识库力求准确，但不保证内容的完整性、时效性或适用性。
> 3. 因使用本知识库内容而产生的任何法律后果，作者及贡献者不承担任何责任。
> 4. 进行任何无人机飞行活动前，请务必查阅 [CAAC官网](https://www.caac.gov.cn/) 和 [UOM平台](https://uom.caac.gov.cn/) 获取最新法规要求。
>
> **官方参考来源**：
> - 中国民用航空局官网：https://www.caac.gov.cn/
> - 民用无人驾驶航空器综合管理平台（UOM）：https://uom.caac.gov.cn/
> - 《无人驾驶航空器飞行管理暂行条例》（国务院、中央军委令第761号）
> - 《民用无人驾驶航空器运行安全管理规则》（CCAR-92部）
