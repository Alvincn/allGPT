# AllGPT

## 所用接口链接

项目使用百度ai接口需要使用到的：

1. 短文本在线合成 √

   [在线语音合成_高度拟人的语音合成服务-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/speech/tts_online)

2. 长文本在线合成 √

   [百度AI开放平台-全球领先的人工智能服务平台-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/speech/long_tts)

3. 通用文字识别  √

   [百度文字识别,覆盖全面,响应迅速,准确率超99%-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/ocr/general)

4. 办公文档识别

   [办公文档识别_文档识别-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/ocr/doc_analysis_office)

5. 人体检测与属性识别

   [人体检测与属性识别_人体检测识别-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/body/attr)

6. 检查有几个人

   [人体关键点识别_人体关键点检测_人体分析-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/body/pose)

7. 查查这是什么车

   [车型识别,可用于拍照识车和智能卡口等场景-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/vehicle/car)

8. 物体识别

   [通用物体和场景识别_可识别10万多类常见物体和场景-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/imagerecognition/general)

9. logo识别

   [品牌logo识别_拍照识别2万多类商品logo-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/imagerecognition/logo)

10. 植物识别

    [植物识别_拍照识别植物-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/imagerecognition/plant)

11. 图像修复

    [图像修复_图像修复算法-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/imageprocess/inpainting)

12. 黑白图片上色

    [黑白图像上色-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/imageprocess/colourize)

13. 人像动漫化

    [人像动漫化-百度AI开放平台 (baidu.com)](https://ai.baidu.com/tech/imageprocess/selfie_anime)

14. 对话情绪识别

    [语言与知识 - 对话情绪识别 | 百度AI开放平台 (baidu.com)](https://ai.baidu.com/ai-doc/NLP/rk6z52hlz)

## 总体功能

点击下方选择框可以进行选择功能

其中，唠唠嗑 以及 文本合成 功能使用输入框，其余功能使用文件上传

技术栈：

- 前端使用Vue+elementui

- 交互技术使用axios

- 后端使用Python Flask框架

主要功能：

1. 唠唠嗑
   1. 调用对话情绪识别，调用ai回复内容
   2. 输入【某某市天气】可查询某某市天气
   3. 输入【时间】可查询当前机器时间
2. 文本合成
3. 通用识别
   1. 通用文字识别
   2. 文档识别
   3. 人体检测与属性识别
   4. 物体识别
   5. 车辆识别
   6. logo识别
   7. 植物识别
4. 图像
   1. 图像修复
   2. 黑白图像上色
   3. 人物动漫化

## 实现原理

### 唠唠嗑

检测用户输入的内容

- 如果包含【时间】，返回当前系统时间
- 如果包含【天气】，以天气进行截取，取市发送天气请求接口，展示数据
- 上述都不包含，则将用户输入发送到后端，由接口进行情绪检测，将情绪返回给前端，通过返回的情绪选择对应的回复

### 文本合成

将用户输入的内容发送给后端，后端通过sdk将文本转化成语音，保存到 temp/audio 文件夹中，其中文本名使用当前时间戳，确保文件的唯一性，将文件名返回给前端，通过前端生成 audio 标签的 src 属性链接该音频

### 通用识别

将用户上传图片文件发送给后端，后端将其保存再 temp/img 文件夹下，并使用当前时间戳进行命名，调用 sdk 对文件进行识别，将识别后的结果发送给前端，前端展示

### 图像

将用户上传图片文件发送给后端，后端将其保存再 temp/img文件夹下，并使用当前时间戳进行命名，调用 sdk 对该图片进行处理，将处理之后的图片保存到  temp/fiximg 文件夹中，使用当前时间戳进行命名，将文件名返回给前端，通过前端生成的 img 标签的 src 属性链接到该图片



