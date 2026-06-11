---
title: Tools⚒️：安装Claude-code指南
date: 2026-01-01 11:15:17
tags:
---
Claude Code是一个基于大语言模型（LLM）的智能体，属于AI助手产品形态。它不是单纯的微调模型、协议或开发框架，而是通过对大模型的工程化封装和任务指令优化，面向编程场景提供自然语言到代码的智能生成与辅助能力。(在终端命令行中使用)


# 安装ClaudeCode
之后就是安装ClaudeCode，这个在官网下载也是需要翻墙的。这里可以使用国内镜像完成安装：
一般使用npm包管理器安装：
<pre><code class="language-bash">npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
</code></pre>
如果电脑没有npm，可以在powershell里边安装：
[更多资料参考](https://github.com/Ruanweiqiao/claude-code-windows-setup)
<pre><code class="language-bash">irm https://claude.ai/install.ps1 | iex
</code></pre>
<img src="/images/16.png" alt="" width="960" height="540" style="max-width: 100%; height: auto; display: block;" />

安装好后，任意终端运行命令：`Claude`即可在当前目录下运行Claude代码编辑智能体。

<img src="/images/17.png" alt="" width="960" height="540" style="max-width: 100%; height: auto; display: block;" />

但是想在国内用 Claude 模型与智能体并不容易，你至少需要：

① 能翻墙 
② 有外币信用卡或外区 Apple ID

为了解决这个问题，这里提出两个解决方法：

# 1.替换Claude后端模型

一般情况下，Claude Code默认搭配的是Anthropic公司的 Claude Opus 4.5，编程能力当前最强的大模型。用户无法自行替换为其他大模型。但是也有一些工具能够帮助我们实现模型请求的代理，将ClaudeCode向其自有模型发起的请求包欺骗至我们所指定的大模型提供商。

### ClaudeCode on Windows配置方法
下载一个Github项目：CC-Switch，接管本地的模型请求代理，下边已经找好了Windows 10+可用的msi安装包：
# CC-Switch
(下载链接)[https://github.com/farion1231/cc-switch/releases/download/v3.10.3/CC-Switch-v3.10.3-Windows.msi]


<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 10px; align-items: start;">
	<img src="/images/11.png" alt="" width="640" height="360" style="width: 100%; height: auto; display: block;" />
	<img src="/images/14.png" alt="" width="640" height="360" style="width: 100%; height: auto; display: block;" />
	<img src="/images/12.png" alt="" width="640" height="360" style="width: 100%; height: auto; display: block;" />
	<img src="/images/13.png" alt="" width="640" height="360" style="width: 100%; height: auto; display: block;" />
	<img src="/images/15.png" alt="" width="640" height="360" style="width: 100%; height: auto; display: block;" />
	<img src="/images/19.png" alt="" width="640" height="360" style="width: 100%; height: auto; display: block;" />
</div>

# Further Exploration on Model Backend Configuration
类似一个网站的前后端架构，我们与大模型交互的所有应用（Web对话界面，Copilot聊天窗，命令行中的ClaudeCode）都是一个前端。
前端通过向大模型后端发起请求(API请求)获得大模型的回复响应。
由于一些大模型提供商不方便访问(eg: OpenAI)，于是出现了一系列API转接服务提供商。
通过转接服务提供商，你不仅能够绕过访问地域限制，也可以调用各个大模型提供商的大模型产品(deepseek,openai,doubao等)。你可以让Claude支持不同的模型后端：

<img src="/images/20.png" alt="" width="640" height="320" style="max-width: 100%; height: auto; display: block;" />


### 使用转接服务的方式就是修改环境变量
eg:
- BASE_URL=""
- API_KEY=""

在我们的场景中，cc-switch相当于科学上网用的Clash，而API_Key和BASE_URL相当于你向Clash导入的订阅链接（由VPN提供商提供的配置文件链接）。

<img src="/images/21.png" alt="" width="640" height="320" style="max-width: 100%; height: auto; display: block;" />

推荐一个我们在用的API转接提供商：云雾API https://yunwu.ai
所以你可以使用一个API_KEY去调用几乎市面上所有的大模型，体验对比使用效果，或者Benchmark各个大模型的性能表现。
MODEL HUB是提供商用于展示其支持服务的界面。
云雾API MODEL HUB： https://yunwu.ai/console/playground
<img src="/images/18.png" alt="" width="960" height="540" style="max-width: 100%; height: auto; display: block;" />


你也可以选择直接使用模型供应商提供的API，需要在网站注册并充值，获取API：
注意，填写模型名就是该模型公布的唯一模型ID（在提供商网页中翻到）

我这里提供一个DeepSeek的API供使用：sk-bea2f61ad6cd44b9a8dbb24850d71b99

eg：
### DeepSeek：
官网链接：https://platform.deepseek.com
请求地址：https://api.deepseek.com/anthropic  
模型名：DeepSeek-V3.2

### Qwen:
官网链接：https://bailian.console.aliyun.com
请求地址：https://dashscope.aliyuncs.com/apps/anthropic
模型名：qwen3-max


### Chatgpt-5.2(转接)
官网链接：https://chatgpt.com
请求地址：https://yunwu.ai
模型名：gpt-5.2

# 2.设置环境变量，开代理连接
<pre><code>setx http_proxy http://127.0.0.1:7890
setx https_proxy http://127.0.0.1:7890
setx HTTP_PROXY http://127.0.0.1:7890
setx HTTPS_PROXY http://127.0.0.1:7890
</code></pre>

