# UAV-Knowledge-Base：无人机法规知识库

基于LLM辅助构建的CAAC无人机法规结构化知识库，覆盖**257+个结构化知识点**，包含8大分类。

---

## 核心成果

| 指标 | 数据 |
|------|------|
| 结构化知识点 | **257+** |
| 知识分类 | **8大模块** |
| 法规覆盖 | CAAC/CCAR-61/CCAR-92/暂行条例 |
| LLM错误模式分析 | **15+类** |

---

## 知识库导航

| 分类 | 文件 | 知识点数 |
|------|------|----------|
| **法规概述** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main/法规概述.md) | ~30 |
| **飞行分类** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main飞行分类.md) | ~20 |
| **执照体系** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main/执照体系.md) | ~25 |
| **空域管理** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main空域管理.md) | ~20 |
| **安全规范** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main安全规范.md) | ~35 |
| **多轴飞行器** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main多轴飞行器.md) | 23 |
| **飞行原理** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main/飞行原理.md) | 70 |
| **概述与系统** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main/概述与系统.md) | 15 |
| **气象知识** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main/气象知识.md) | 26 |
| **空域法规与任务规划** | [查看](https://github.com/s9rgbpmy4n-cyber/UAV-Knowledge-Base/blob/main/空域法规与任务规划.md) | 28 |

## 技术方法

本项目采用"LLM辅助+人工审核"的四步法构建：

1. **法规收集**：整理CAAC法规原文（暂行条例/CCAR-92/CCAR-61等）
2. **LLM拆解**：使用DeepSeek进行初步知识结构化，设计迭代Prompt优化输出质量
3. **人工审核**：基于CAAC超视距机长的专业背景，对LLM输出进行准确性校正
4. **对比测试**：系统性对比DeepSeek/Claude/GPT在无人机专业领域的回答质量

---

## LLM在垂直领域的15类典型错误模式

### 事实性错误（5类）
1. **重量分类混淆**：把微型的管理要求套到轻型上
2. **条款引用错误**：编造不存在的法规条款编号
3. **执照等级混淆**：视距内/超视距的权限对应关系错误
4. **空域分类错误**：管制空域和非管制空域搞混
5. **高度限制错误**：不同地区的高度限制给出统一错误数字

### 理解性错误（5类）
6. **视距内理解字面化**：不考虑FPV等特殊情况
7. **法规时效性忽略**：引用已废止的旧版规定
8. **备案审批混淆**：对"备案"和"审批"的区别理解不清
9. **地方规定忽略**：忽略各地对无人机管理的差异性补充规定
10. **禁飞区范围不准**：对禁飞区范围的描述不准确

### 表达性错误（5类）
11. **术语过于专业**：输出不适合科普场景
12. **格式不稳定**：同样Prompt每次输出格式不同
13. **过度简化**：对复杂条款拆解丢失关键信息
14. **缺乏关联**：多个相关条款之间缺乏关联性整理
15. **例外说明不足**：对"例外情况"和"特殊许可"说明不足
