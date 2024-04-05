# 🌟 [NAACL 2024] Investigating Data Contamination in Modern Benchmarks for Large Language Models
<div style="width:40% float:center diaplay:inline">
     <img src=./logo/gt_logo.png width=7%/> <img src=./logo/yale_logo.png width=12%/> &nbsp; &nbsp; <img src=./logo/logo-ai2.svg width=35%/>
</div>

<a target="_blank" href="https://arxiv.org/abs/2311.09783">
<img style="height:22pt" src="https://img.shields.io/badge/-Paper-black?style=flat&logo=arxiv">
</a><a target="_blank" href="https://github.com/CharlesDDDD">
<img style="height:22pt" src="https://img.shields.io/badge/-Code-green?style=flat&logo=github">
</a><a target="_blank" href="https://huggingface.co/papers/2311.09783">
<img style="height:22pt" src="https://img.shields.io/badge/-🤗%20HuggingFace-red?style=flat"></a><a target="_blank" href="https://huggingface.co/llm-blender">
<!-- <img style="height:22pt" src="https://img.shields.io/badge/-🤗%20Models-red?style=flat"> -->
</a><a target="_blank" href="https://twitter.com/billyuchenlin/status/1668666357058277377">
<img style="height:22pt" src="https://img.shields.io/badge/-Tweet-blue?style=flat&logo=twitter">
</a>
<br>

<span style="color:#183385; font-size: 14pt; font-family: Roboto, Helvetica, Arial, Heveltica Neue, sans-serif">
     <b>Authors:</b> <a class="name" target="_blank" href="https://charlesdddd.github.io/">Chunyuan Deng</a>, 
     <a class="name" target="_blank" href="https://yilunzhao.github.io/">Yilun Zhao</a>,
     <a class="name" target="_blank" href="https://xiangrutang.github.io/">Xiangru Tang</a>&nbsp; 
     <a class="name" target="_blank" href="https://medicine.yale.edu/profile/mark-gerstein/">Mark Gerstein</a>,
     <a class="name" target="_blank" href="https://armancohan.com/">Arman Cohan</a>&nbsp; @
     <a class="btna" target="_blank" href="https://yale-nlp.github.io/">Yale NLP</a> 
     </span>

## 🔥News

- [2024/4/5] Our paper was accpeted at NAACL 2024 main conference! Working on clean our codes and make it public for the first version. 

- [2023/11/15] We release out preprint at arxiv! Feel free to check out preprint [here](https://arxiv.org/abs/2311.09783)

## 🪐Introooo

![LLM-BLender](./docs/llm_blender.png)

<details><summary>Abstract</summary> 

- We introduce LLM-Blender, an innovative ensembling framework to attain consistently superior performance by leveraging the diverse strengths of multiple open-source large language models (LLMs). LLM-Blender cut the weaknesses through ranking and integrate the strengths through fusing generation to enhance the capability of LLMs.


- Our framework consists of two complementary modules: **PairRanker** and **GenFuser**, addressing the observation that optimal LLMs for different examples can significantly vary. **PairRanker** employs a specialized pairwise comparison method to distinguish subtle differences between candidate outputs. **GenFuser** aims to merge the top-ranked candidates from the aggregation of PairRanker's pairwise comparisons into an improved output by capitalizing on their strengths and mitigating their weaknesses.
- To facilitate large-scale evaluation, we introduce a benchmark dataset, [**MixInstruct**](#data_release), which is a mixture of multiple instruction datasets featuring oracle pairwise comparisons for testing purposes. Our **LLM-Blender** significantly surpasses the best LLMs and baseline ensembling methods across various metrics on **MixInstruct**, establishing a substantial performance gap.

</details>

