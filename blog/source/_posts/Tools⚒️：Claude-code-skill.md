---
title: Tools⚒️：安装Claude-code-skill指南
date: 2026-02-13 15:07:00
tags:
---

官方文档：https://code.claude.com/docs/zh-CN/skills
# Claude Skill
Claude 官方开发了Skill的标准，并开源了16个官方默认使用的Skill。
这个应该是预装装好的，但是我在电脑没有找到，需要手动安装下来。这里记录的是如何下载安装并进行测试使用。
[**Claude Skill官方仓库Skill**](https://github.com/anthropics/skills)

<code>
git clone https://github.com/anthropics/skills
</code>

skills-main/
├── .claude-plugin/
│   └── marketplace.json                          # Claude插件市场配置文件
├── .gitignore                                    # Git版本控制忽略文件
├── README.md                                     # 仓库主要说明文档
├── agent_skills_spec.md                          # 代理技能规范文档
├── THIRD_PARTY_NOTICES.md                       # 第三方许可证声明文件
├── document-skills/                              # 📄 文档处理技能包（专有）
├── algorithmic-art/                              # 🎨 算法艺术生成技能
├── artifacts-builder/                            # 🔧 HTML工件构建技能
├── brand-guidelines/                             # 🏢 品牌规范应用技能
├── canvas-design/                                # 🖼️ 画布设计技能
├── internal-comms/                              # 📧 内部沟通写作技能
├── mcp-builder/                                 # 🌐 MCP服务器构建技能
├── skill-creator/                               # 📚 技能创建指南技能
├── slack-gif-creator/                           # 🎬 Slack GIF创建技能
├── template-skill/                              # 📋 基础技能模板
├── theme-factory/                               # 🎨 主题工厂技能
└── webapp-testing/                              # 🧪 Web应用测试技能

# Step1:
克隆仓库后，输入`explorer .`即可在当前终端的工作目录下打开文件管理器，找到对应文件夹。

![](/images/2026-0213-2.png)

# Step2:
找到Claude的安装目录，默认在：C:\Users\ASUS\\ .claude
**把内层skills文件夹拖进这个目录，即可完成安装。**

Claude成功识别检查方式：
<img src="/images/2026-0213-1.png" width="960" height="540" alt="">

更多Claude Skill：
https://github.com/ComposioHQ/awesome-claude-skills
https://github.com/affaan-m/everything-claude-code