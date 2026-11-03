# EmotionLab

一个基于 Python 的文本情感识别学习项目。

## 项目介绍

EmotionLab 是一个用于学习机器学习、自然语言处理和 AI 应用开发的项目。

目前使用关键词规则完成基础的英文情感判断，后续将逐步引入机器学习模型、深度学习模型和 FastAPI。

## 技术栈

- Python 3.11
- Conda / Miniforge
- NumPy
- Requests
- Git / GitHub

## 项目结构

```text
EmotionLab/
├── emotionlab/
│   ├── __init__.py
│   └── predictor.py
├── main.py
├── requirements.txt
├── environment.yml
├── README.md
└── .gitignore
```

## 环境安装

首先克隆项目：

```bash
git clone https://github.com/pangpei857/EmotionLab.git
cd EmotionLab
```

然后使用 Conda 创建环境：

```bash
conda env create -f environment.yml
conda activate emotionlab
```

## 运行项目

执行：

```bash
python main.py
```

示例输入：

```text
I am happy today
```

示例输出：

```text
情感识别结果：joy
```

## 当前进度

- [x] 配置 WSL + VS Code 开发环境
- [x] 创建 Conda 虚拟环境
- [x] 实现基础关键词情感分类
- [x] 使用 Python 包组织项目代码
- [x] 配置 Python 项目依赖
- [ ] 使用机器学习训练分类器
- [ ] 添加模型评估功能
- [ ] 使用 FastAPI 开发接口
- [ ] 使用 Docker 部署

## 项目说明

当前版本仅用于学习 Python 工程开发，还不具备成熟的情感识别能力。
后续将使用真实数据集训练和评估模型。