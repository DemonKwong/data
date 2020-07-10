#!/bin/bash
# 激活环境
source activate
# 退出环境
conda deactivate
conda activate spider
nohup python scrapy_start.py > start.log 2>&1 &
