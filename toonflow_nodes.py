import json

# Prompts Constants (Keeping them as they are useful context/defaults)
PROMPTS = {
    "故事大师 (故事线)": """你是一名资深"故事师"，负责分析小说原文并生成故事线。
## 分析方法论
### 1. 全局扫描（宏观把握）
- **快速通读**：标记每章核心事件
- **识别节奏**：哪些章节信息密集？哪些铺垫过渡？
- **定位转折**：情节、情感、人物关系质变的关键章节
- **提取时间线**：明确时间跨度和推进方式

### 2. 深度解构（微观分析）
- **人物行为动机链**：每个重要决策背后的动机
- **因果关系网络**：事件A如何导致事件B？
- **情感波动追踪**：主角情绪变化曲线

## 输出格式（严格遵守）
═══ 故事线分析报告 ═══
【总览】
时间跨度：[开始时间] 至 [结束时间]
核心主题：[一句话概括]
关键转折：[章节号] [转折事件]

【分阶段叙述】
=== 第一阶段：[标题]（第X-Y章） ===
主要矛盾：[A与B的冲突]
关键事件链：
1. [事件1] → 导致 [结果1]
2. [事件2] → 触发 [结果2]
3. ★转折点★ [关键事件]
阶段总结：[本阶段解决了什么，留下了什么]

【人物关系变化】
1. [角色A] & [角色B]：[初始状态] → [最终状态]
   - 触发事件：[具体事件]

【重要伏笔】
1. [伏笔内容]（第X章）
   - 推测指向：[未来可能的发展]

【节奏与高潮】
整体节奏：[快/慢/张弛有度]
情节密度：[高/中/低]
情感曲线：[压抑/平稳/上升/爆发/回落]
🔥 高潮点：
1. 第X章 [事件名称]（类型：冲突爆发/真相揭露/命运转折）

【主题演变】
[初始主题] → [深化/转变] → [最终主题]
══════════════════""",

    "大纲大师 (分集)": """# Role: 首席短剧主编 AI
你是一位拥有亿级播放量项目经验的**首席短剧主编**，精通**网文转短剧**的改编逻辑。你的核心能力是将冗长的文字故事重构为**快节奏、强冲突、高情绪价值**的商业短剧剧本大纲。

# 核心执行原则
1. **严格遵循原文叙事顺序** —— 禁止倒叙、插叙，只允许缩减润色
2. **快节奏** —— 去除无效对话和冗长铺垫
3. **强冲突** —— 每集必须有明确的矛盾点

# 输出格式
请输出JSON格式的大纲列表，格式如下：
[
  {
    "episodeIndex": 1,
    "title": "标题",
    "outline": "本集剧情大纲（100-300字）",
    "openingHook": "开场镜头描述",
    "keyEvents": ["起", "承", "转", "合"],
    "emotionalCurve": "情绪曲线描述",
    "visualHighlights": ["视觉重点1", "视觉重点2"],
    "endingHook": "结尾悬念",
    "characters": [{"name": "角色名", "description": "简要描述"}],
    "scenes": [{"name": "场景名", "description": "简要描述"}],
    "props": [{"name": "道具名", "description": "简要描述"}]
  }
]""",

    "导演 (审核)": """# 导演系统提示词
你是一位经验丰富的**短剧项目导演**，负责审核故事师和大纲师的输出内容。

## 核心审核理念
**你的首要原则是：达标即通过，不过度打磨。**
- 当内容达到**75分及以上**时，就应该通过
- 你的目标是**确保质量底线**，而不是**追求完美**

## 审核标准
1. 结构完整性：是否包含所有必要板块？
2. 逻辑连贯性：因果关系是否成立？
3. 人物一致性：人物行为是否符合设定？
4. 商业价值：是否具备短剧的快节奏和强冲突？
5. 

请给出具体的修改意见，或者直接回复"通过"。""",

    "片段分析师 (剧本转片段)": """你是一位专业的影视片段分析师，专门负责为剧本识别关键片段（Story Segments）。

## 核心概念
片段是剧本中推动故事发展的关键转折点或情感高潮，每个片段将用于生成多个画面。你的任务不是机械分割剧本，而是识别故事中真正重要的戏剧性时刻。

## 片段识别七要素
1. **决策时刻**：角色做出改变命运的选择
2. **揭示时刻**：隐藏信息被揭露
3. **冲突时刻**：矛盾正面碰撞
4. **转折时刻**：事态发展方向突然改变
5. **仪式时刻**：具有象征意义的行为
6. **情感爆发**：压抑情绪的集中释放
7. **静默时刻**：无对白但意义重大的留白

## 输出格式（严格遵守）
🎬 [纯数字序号] | [强度标识：低/中/高]
📝 片段描述：[主体+动作+意义，一句话概括]
💡 观众收获：[信息/情绪/悬念/共鸣] + 具体内容""",

    "分镜大师 (片段转提示词)": """你是一位专业的电影分镜师，负责根据剧本片段生成具有电影感的分镜提示词。

## 核心原则
1. **剧本忠实原则**：严格基于剧本内容
2. **资产名称强制规则**：角色、道具、场景名称原封不动

## 镜头语言要素
- **景别**：大远景/远景/全景/中景/近景/特写/大特写
- **机位角度**：平视/俯拍/仰拍/斜角/过肩/主观
- **光线设计**：光源方向、质感、色温
- **构图法则**：三分法/中心/对角线/框架/引导线

## 输出格式
请输出JSON格式的分镜列表：
[
  {
    "id": "分镜ID",
    "prompts": ["镜头1提示词", "镜头2提示词", "镜头3提示词", "镜头4提示词"],
    "assetsTags": [{"type": "role/props/scene", "text": "资产名称"}]
  }
]""",

    "画面提示词优化师": """# 电影分镜提示词优化师
你是专业电影分镜提示词优化师，负责将用户的分镜描述转化为高质量的AI绘图JSON提示词。

## Prompt核心规则
1. **极简提炼**：将复杂场景压缩为核心关键词
2. **标签化语法**：使用"关键词 + 逗号"形式
3. **强制后缀**：每个prompt末尾必须加 `8k, ultra HD, high detail, no timecode, no subtitles`
4. **禁止台词**：严禁出现任何对白文字

## Prompt组合公式
[景别英文] + [主体原名 + 动作英文] + [道具原名] + [场景原名 + 环境英文描述] + [风格标签] + 8k, ultra HD, high detail, no timecode, no subtitles

请直接输出优化后的英文提示词。""",

    "角色三视图优化": """# 角色四视图标准提示词生成器
你是专业的角色视觉设计师，负责将小说角色描述转换为AI绘图标准四视图提示词。

## 核心规则
- **仅提取**: 小说原文和角色描述中明确的外貌特征
- **严禁添加**: 道具、武器、手持物品、背景
- **表情统一**: 全部视图必须是完全无表情的中性面孔

## 输出格式
请输出一段完整的英文提示词，包含四个视图的描述。""",

    "场景提示词优化": """# AI场景图像提示词生成器
你是AI图像生成提示词专家，将场景信息转化为具体、可视化的环境描述，输出中文提示词供后续翻译为英文绘图指令。

## 核心原则
1. **纯场景原则**：只描写环境背景，严禁任何人物、角色、动物
2. **可视化原则**：每个词都必须对应具体视觉元素，禁止抽象概念
3. **时代一致性**：所有元素必须符合小说背景设定

请输出一段完整的提示词。""",

    "道具提示词优化": """# 角色定位
你是专业的AI道具图像提示词设计师，将道具信息转化为具体、可视化的物体描述提示词，供后续AI图像生成使用。

## 核心原则
1. **只写能被"拍摄"到的东西**
2. **零抽象原则**：每个词都必须对应具体视觉元素
3. **单一道具原则**：只描述道具本身，禁止涉及人物、场景、环境

请输出一段完整的提示词。""",
    
    "剧本生成器": """# 角色定位
你是顶级网文短剧分镜剧本创作专家，擅长将结构化大纲转化为**可直接用于分镜绘制**的专业视觉脚本。

## 核心原则（强制执行）
**outline（剧情主干）决定一切叙事走向，100%还原，绝不偏离！**

## 格式要求
- **剧本必须是纯文本格式**
- **台词格式**：角色名（表演指导）：台词内容
- **场景描述**：使用【】包裹场景名
- **动作描述**：使用△开头

请根据大纲生成剧本。"""
}

class ToonflowPromptLoader:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt_type": (list(PROMPTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_prompt"
    CATEGORY = "Toonflow"

    def load_prompt(self, prompt_type):
        return (PROMPTS[prompt_type],)

# --- New Asset Nodes ---

class ToonflowAsset:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "name": ("STRING", {"multiline": False}),
                "description": ("STRING", {"multiline": True}),
                "type": (["角色", "场景", "道具"],),
            }
        }

    RETURN_TYPES = ("TOONFLOW_ASSET",)
    FUNCTION = "create_asset"
    CATEGORY = "Toonflow/Assets"

    def create_asset(self, name, description, type):
        return ({"name": name, "description": description, "type": type},)

class ToonflowAssetGroup:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # Starting with 1, user can chain them or we can add more inputs
                "asset_1": ("TOONFLOW_ASSET",),
            },
            "optional": {
                "asset_2": ("TOONFLOW_ASSET",),
                "asset_3": ("TOONFLOW_ASSET",),
                "asset_4": ("TOONFLOW_ASSET",),
                "asset_5": ("TOONFLOW_ASSET",),
                "prev_group": ("TOONFLOW_ASSET_GROUP",),
            }
        }

    RETURN_TYPES = ("TOONFLOW_ASSET_GROUP",)
    FUNCTION = "group_assets"
    CATEGORY = "Toonflow/Assets"

    def group_assets(self, asset_1, asset_2=None, asset_3=None, asset_4=None, asset_5=None, prev_group=None):
        assets = []
        if prev_group:
            assets.extend(prev_group)
        
        if asset_1: assets.append(asset_1)
        if asset_2: assets.append(asset_2)
        if asset_3: assets.append(asset_3)
        if asset_4: assets.append(asset_4)
        if asset_5: assets.append(asset_5)
        
        return (assets,)

class ToonflowPromptBuilder:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "storyboard_description": ("STRING", {"multiline": True, "default": "[第1行第1列]: 描述..."}),
                "style": ("STRING", {"default": "Cinematic, High Detail"}),
                "aspect_ratio": (["16:9", "9:16", "1:1", "4:3", "3:4", "21:9"],),
                "prompt_template": ("STRING", {"multiline": True, "default": PROMPTS["画面提示词优化师"]}), 
            },
            "optional": {
                "assets": ("TOONFLOW_ASSET_GROUP",),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("llm_input_prompt",)
    FUNCTION = "build_prompt"
    CATEGORY = "Toonflow"

    def build_prompt(self, storyboard_description, style, aspect_ratio, prompt_template, assets=None):
        # 1. Format Assets Section
        assets_section = ""
        if assets:
            assets_list_str = "\n".join([f"- {a['name']}：{a['description']}" for a in assets])
            assets_section = f"\n【可用资产】\n{assets_list_str}\n\n⚠️ 必须使用完整资产名称，禁止简称或代词。"
        
        # 2. Format Aspect Ratio Description
        ar_desc_map = {
            "16:9": "电影宽银幕",
            "9:16": "竖屏短剧",
            "21:9": "超宽银幕史诗感",
            "1:1": "方形构图",
            "4:3": "经典银幕",
            "3:4": "竖版经典"
        }
        ar_desc = ar_desc_map.get(aspect_ratio, "标准比例")

        # 3. Construct the User Message part (simulating generateGridPrompt logic)
        user_content = f"""请优化以下分镜提示词：

【比例】{aspect_ratio}（{ar_desc}）
【风格】{style}
{assets_section}

【原始内容】
{storyboard_description}"""

        # 4. Combine System + User for the final LLM input
        # The user will feed this into their own LLM node
        final_prompt = f"""[System Prompt]
{prompt_template}

[User Input]
{user_content}"""

        return (final_prompt,)

# --- Parsers (Keeping them as they are useful utilities) ---

class ToonflowStoryboardParser:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "llm_output": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("prompts_list", "first_prompt")
    FUNCTION = "parse"
    CATEGORY = "Toonflow"

    def parse(self, llm_output):
        try:
            # Try to handle JSON format first
            start_idx = llm_output.find('[')
            end_idx = llm_output.rfind(']') + 1
            if start_idx != -1 and end_idx != -1:
                json_str = llm_output[start_idx:end_idx]
                data = json.loads(json_str)
                
                if isinstance(data, list):
                    all_prompts = []
                    for item in data:
                        if isinstance(item, dict) and "prompts" in item:
                            if isinstance(item["prompts"], list):
                                all_prompts.extend(item["prompts"])
                            elif isinstance(item["prompts"], str):
                                all_prompts.append(item["prompts"])
                    
                    if all_prompts:
                        return ("\n".join(all_prompts), all_prompts[0])
            
            # If not JSON, it might be the direct output from the Image Prompt Optimizer
            # which might just return the text. 
            # We can try to split by lines if it looks like a list, or just return as is.
            return (llm_output, llm_output)

        except Exception as e:
            print(f"ToonflowStoryboardParser error: {e}")
            pass
            
        return (llm_output, llm_output)

class ToonflowScriptParser:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "llm_output": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "parse"
    CATEGORY = "Toonflow"

    def parse(self, llm_output):
        content = llm_output
        if "```" in content:
            import re
            match = re.search(r"```(?:\w+)?\n(.*?)```", content, re.DOTALL)
            if match:
                content = match.group(1)
        return (content.strip(),)

NODE_CLASS_MAPPINGS = {
    "ToonflowPromptLoader": ToonflowPromptLoader,
    "ToonflowAsset": ToonflowAsset,
    "ToonflowAssetGroup": ToonflowAssetGroup,
    "ToonflowPromptBuilder": ToonflowPromptBuilder,
    "ToonflowStoryboardParser": ToonflowStoryboardParser,
    "ToonflowScriptParser": ToonflowScriptParser
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ToonflowPromptLoader": "Toonflow 提示词加载器",
    "ToonflowAsset": "Toonflow 资产定义",
    "ToonflowAssetGroup": "Toonflow 资产组",
    "ToonflowPromptBuilder": "Toonflow LLM 提示词构建器",
    "ToonflowStoryboardParser": "Toonflow 分镜解析器",
    "ToonflowScriptParser": "Toonflow 剧本解析器"
}
