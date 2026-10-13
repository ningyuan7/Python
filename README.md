# Python 作业与实验 01

姓名：宋高峰  
学号：20244081129

## 文件说明

| 文件 | 内容 |
| --- | --- |
| `20244081129_宋高峰_hw01.ipynb` | HW01：函数、最大公约数、欧拉数近似、整数幂判断 |
| `20244081129_宋高峰_exp01.ipynb` | EXP01：Python 基础、统计、文件处理、模块和类 |
| `student_utils.py` | 实验 4 的学生记录解析模块 |
| `exp01_data/students.txt` | 题目指定的模拟数据，含三条无效记录 |
| `exp01_data/report.txt` | 统计报告和无效记录明细 |
| `exp01_data/students.pkl` | 实验生成的序列化数据 |
| `exp01_data/mode_demo.txt` | w / a 模式演示文件 |
| `environment.yml` | 用于重建独立 conda 环境的依赖配置 |

## 使用独立 conda 环境运行

本次已在现有的独立 conda 环境 `d2l` 中运行两个 Notebook，实际 Python 版本和解释器路径见首个代码单元。
下列配置新建轻量环境 `hw01_exp01`，不需要安装原有 `d2l` 环境中的其他软件包。

在 Anaconda Prompt 中进入本文件夹后执行：

```bat
conda env create -f environment.yml
conda activate hw01_exp01
python -m ipykernel install --user --name hw01_exp01 --display-name "Python (hw01_exp01)"
python -m notebook
```

打开 Notebook 后选择 `Python (hw01_exp01)` 内核。两份 Notebook 的首个单元会检查当前解释器属于实际激活的独立 conda 环境。
从本文件夹启动 Jupyter，使实验数据和模块保存在 Notebook 同级目录。
提交前分别选择“重启内核并运行全部单元”，确认没有未捕获的异常并保存运行结果。
Notebook 中预期出现的错误案例都已捕获，属于题目要求的演示。

完整运行实验 Notebook 会重写模拟数据、统计报告和模块，并重置 w / a 演示文件，因此可以重复运行。

## 已完成的验证

两份 Notebook 分别使用新内核从头执行：作业 9 个代码单元、实验 22 个代码单元，均无未捕获的异常。
首个代码单元确认实际独立 conda 环境为 `d2l`，Python 为 3.9.23。
统计结果为 6 条有效记录、3 条无效记录，平均分 76.67，及格率 83.33%。

## 上传 GitHub

可把整个文件夹的内容作为一个仓库上传。保留两个已执行的 `.ipynb`，GitHub 页面即可显示代码及输出；
也保留模块、模拟数据和环境配置，便于他人重现。
`.gitignore` 排除了 Python、Jupyter 和编辑器缓存。
