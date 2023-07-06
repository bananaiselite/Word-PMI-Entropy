## **新詞探勘**
------
### ***目的:***
在做中文斷詞的時候，有時候效果不盡理想，需要靠字典來加強，但是建立字典曠日廢時，靠自由度與凝合度可以幫助您快速建立字典
### ***方法:***
* 安裝
 > pip install git+https://github.com/bananaiselite/Word-PMI-Entropy.git
* 使用
```python
from volcab_finding import volcab_finding

vol = volcab_finding()
vol.run()
```
* 注意
此方法要使用在文章數量大或長篇文章中效果較佳，且勿使用單篇或短文，可去example中看使用範例

### ***函式說明:***
***檔案 : volcab_finding.py***

***n_gram_words:***
從原文中擷取從 1 到 n_gram 長度的字串，並作為單詞計算詞頻。

***PMI_filter:***
計算單詞內部字詞一起出現的頻率，並將其與單詞本身出現的頻率相除，以計算出單詞的凝合度。如果凝合度大於給定的閾值，則將該單詞加入新單詞列表作為候選字詞。

***calculate_entropy:*** 
計算熵的公式。

***Entropy_left_right_filter :*** 
找出候選字詞的前後字，去計算計算熵值。

