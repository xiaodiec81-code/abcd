# ComfyUI-Toonflow

一套受 [Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) 启发的 ComfyUI 节点，旨在将强大的 AI 辅助分镜和剧本生成工作流带入 ComfyUI。

## 功能特色

- **Toonflow 提示词加载器**: 加载 Toonflow 优化的各类角色系统提示词（如故事大师、大纲大师、导演、分镜大师、画面提示词优化师等）。
- **Toonflow 资产定义**: 定义角色、场景和道具的详细描述。
- **Toonflow 资产组**: 将多个资产打包成组，方便管理。
- **Toonflow LLM 提示词构建器**: 智能组装分镜描述、资产信息、风格设置和画面比例，生成可直接发送给 LLM 的高质量提示词。
- **Toonflow 分镜解析器**: 解析 LLM 返回的 JSON 格式分镜数据，提取绘图 Prompt。
- **Toonflow 剧本解析器**: 清洗 LLM 生成的剧本内容。

## 安装方法

1.  进入你的 ComfyUI `custom_nodes` 目录。
2.  克隆本仓库：
    ```bash
    git clone https://github.com/YOUR_USERNAME/ComfyUI-Toonflow.git
    ```
3.  本插件仅依赖标准 Python 库，无需安装额外依赖。

## 工作流使用指南

### 1. 资产管理
- 使用 **Toonflow 资产定义** 节点创建你的角色（如 "王林"）、场景和道具。
- 将它们连接到 **Toonflow 资产组** 节点进行打包。

### 2. 提示词构建
- 将资产组连接到 **Toonflow LLM 提示词构建器**。
- 输入你的原始分镜描述（例如："王林站在悬崖边回头看"）。
- 选择画面风格和比例。
- 该节点会输出一段包含系统指令、风格指南、资产详情和原始内容的完整 Prompt。

### 3. LLM 处理（使用你现有的节点）
- 将 **Toonflow LLM 提示词构建器** 的输出连接到你喜欢的 LLM 节点（如 ChatGPT、Claude、DeepSeek 节点）。
- LLM 会根据提供的上下文，生成高质量、一致性强的绘图提示词。

### 4. 解析与绘图
- 如果 LLM 返回 JSON 列表，使用 **Toonflow 分镜解析器** 提取。
- 将最终的 Prompt 发送给你的 **Clip Text Encode** 和 **KSampler** 节点生成图像。

## 节点说明

- **Toonflow 提示词加载器 (Prompt Loader)**: 加载预设 System Prompt。
- **Toonflow 资产定义 (Asset Definition)**: 创建资产对象。
- **Toonflow 资产组 (Asset Group)**: 聚合资产。
- **Toonflow LLM 提示词构建器 (Prompt Builder)**: 组装 LLM 上下文。
- **Toonflow 分镜解析器 (Storyboard Parser)**: 提取 JSON 中的 Prompt。
- **Toonflow 剧本解析器 (Script Parser)**: 清洗剧本文本。

## License

MIT License. See [LICENSE](LICENSE) for details.

## 致谢

本项目基于 [Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) 的提示词和工作流逻辑开发。
