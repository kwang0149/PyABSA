# -*- coding: utf-8 -*-
# file: 2_classification_glove.py
# time: 2021/8/5
# author: YANG, HENG <hy345@exeter.ac.uk> (杨恒)
# github: https://github.com/yangheng95
# Copyright (C) 2021. All Rights Reserved.

from pyabsa import TextClassification as TC

model_path = "bert_mlp"  # 'lstm' is a keyword to search the checkpoint in the folder
text_classifier = TC.TextClassifier(model_path)

# batch inference works on the dataset files
inference_sets = TC.TCDatasetList.SST2
results = text_classifier.batch_predict(
    target_file=inference_sets,
    print_result=True,
    save_result=True,
    ignore_error=False,
)
