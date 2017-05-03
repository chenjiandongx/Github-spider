# Github 用户及仓库分析爬虫  

### 爬虫介绍
写完了 Stackoverflow 的爬虫，这回打算写 Github 的，利用 Scrapy 框架对 Github 用户和仓库信息进行爬取，图片利用管道下载。  
Github 是一个很棒的社区，这里可以找到很多优秀的项目，很多实用的库类，简直是 coder 的天堂，同时也是全球最大的同性交友社区？
爬取的数据主要分为两大类， User 类 和 Repo 类 ，也就是针对用户情况和仓库信息

## User 类

先来看看 Github 全站 followers 人数 top10 都是哪些大犇

| Avatar | User                            | Repos | Stars | Followers | Following |
|--------|---------------------------------|-------|-------|-----------|-----------|
|![](http://oog4yfyu0.bkt.clouddn.com/torvalds.jpg)      | https://github.com/torvalds     |     4 |     2 |   53500 |    0 |
|![](http://oog4yfyu0.bkt.clouddn.com/JakeWharton.jpg)   | https://github.com/JakeWharton  |    93 |   213 |   34000 |   12 |
|![](http://oog4yfyu0.bkt.clouddn.com/tj.jpg)            | https://github.com/tj           |   253 |  1700 |   27600 |   46 |
|![](http://oog4yfyu0.bkt.clouddn.com/ruanyf.jpg)        | https://github.com/ruanyf       |    43 |   125 |   24700 |    0 |
|![](http://oog4yfyu0.bkt.clouddn.com/addyosmani.jpg)    | https://github.com/addyosmani   |   292 |   732 |   24700 |  241 |
|![](http://oog4yfyu0.bkt.clouddn.com/paulirish.jpg)     | https://github.com/paulirish    |   261 |   683 |   23300 |  239 |
|![](http://oog4yfyu0.bkt.clouddn.com/mojombo.jpg)       | https://github.com/mojombo      |    61 |   121 |   20100 |   11 |
|![](http://oog4yfyu0.bkt.clouddn.com/gaearon.jpg)       | https://github.com/gaearon      |   202 |  1100 |   17000 |  171 |
|![](http://oog4yfyu0.bkt.clouddn.com/sindresorhus.jpg)  | https://github.com/sindresorhus |   877 |  2200 |   16900 |   40 |
|![](http://oog4yfyu0.bkt.clouddn.com/daimajia.jpg)      | https://github.com/daimajia     |    60 |  2900 |   16400 |  236 |

Linus 大神以压倒性的优势夺得第一名，说实在不知道 Linus 的真不好意思说自己是写代码的，这是信仰。然而大神还是很傲娇的，毕竟没有 following anybody，可能是强到了没朋友了吧，毕竟 ***talk is cheap, show me the code***。JakeWharton 以 34000+ 位于第二，以前也看过一点 Android 的东西，不知道说什么，膜拜吧。  

中国区还是有两名种子选手挺进了 top10，阮一峰 和 代码家  

Github 的地区选项自由度很大，所以比较难统计出各国的注册账户的人数。China 关键字的有 77473 人，USA 关键字有 48667 人  
 
那来了解一下国情，在国区的这 77473 人中，followers 人数 top10 如下  

|  Avatar |         User    |	Following | Followers |
|---------|-----------------|-------------|-----------|
|![](http://oog4yfyu0.bkt.clouddn.com/ruanyf.jpg)       |https://github.com/ruanyf	    |  0	 |  25.2k  |
|![](http://oog4yfyu0.bkt.clouddn.com/daimajia.jpg)     |https://github.com/daimajia	|  236   |  16.5k  |
|![](http://oog4yfyu0.bkt.clouddn.com/yyx990803.jpg)    |https://github.com/yyx990803	|  89	 |  16.2k  |
|![](http://oog4yfyu0.bkt.clouddn.com/michaelliao.jpg)  |https://github.com/michaelliao |  0	 |  12.4k  |
|![](http://oog4yfyu0.bkt.clouddn.com/JacksonTian.jpg)  |https://github.com/JacksonTian	|  145	 |  12.1k  |
|![](http://oog4yfyu0.bkt.clouddn.com/Trinea.jpg)       |https://github.com/Trinea	    |  37    |  11.9k  |
|![](http://oog4yfyu0.bkt.clouddn.com/lifesinger.jpg)   |https://github.com/lifesinger	|  12	 |  10k    |
|![](http://oog4yfyu0.bkt.clouddn.com/stormzhang.jpg)   |https://github.com/stormzhang	|  88    |  9.6k   |
|![](http://oog4yfyu0.bkt.clouddn.com/cloudwu.jpg)      |https://github.com/cloudwu	    |  1	 |  9.5k   |
|![](http://oog4yfyu0.bkt.clouddn.com/onevcat.jpg)      |https://github.com/onevcat	    |  120   |  9k     |

vue.js 作者尤雨溪位列第三。廖雪峰紧跟其后排在第四，话说我也看过他的 Python 教程的


个人仓库数量 top10，因为组织的话无法查看具体仓库数，所以就选取了个人的

|               User                | Repos   |
| ----------------------------------|-------  |
| https://github.com/pombredanne    |  35.4k  |
| https://github.com/gitter-badger  |  27.1k  |
| https://github.com/carriercomm    |  18.8k  |
| https://github.com/digideskio     |  16.9k  |
| https://github.com/bestwpw        |  13.8k  |
| https://github.com/modulexcite    |  10.7k  |
| https://github.com/happyqq        |  9.1k   |
| https://github.com/kleopatra999   |  8.2k   |
| https://github.com/treejames      |  7.2k   |
| https://github.com/carabina       |  7.2k   |  

前两名都好多，项目数量都达到了 27k 以上，好强，他们是怎么办到的


## Repo 类
仓库的 stars top10  

| Repo                                          | Fork      | Star      | Watch      |
|-----------------------------------------------|-----------|-----------|------------|
| https://github.com/freeCodeCamp/freeCodeCamp  |     11121 |    261439 |       7638 |
| https://github.com/twbs/bootstrap             |     50468 |    109702 |       6833 |
| https://github.com/vhf/free-programming-books |     20950 |     83871 |       6221 |
| https://github.com/facebook/react             |     12036 |     65030 |       4402 |
| https://github.com/d3/d3                      |     16709 |     63463 |       3171 |
| https://github.com/getify/You-Dont-Know-JS    |      9232 |     57138 |       3279 |
| https://github.com/sindresorhus/awesome       |      7113 |     57119 |       3787 |
| https://github.com/angular/angular.js         |     27738 |     55503 |       4407 |
| https://github.com/tensorflow/tensorflow      |     26135 |     54976 |       4968 |
| https://github.com/robbyrussell/oh-my-zsh     |     12298 |     52575 |       1895 |
  

仓库的 forks top10  

| Repo                                                  | Fork      | Star      | Watch      |
|-------------------------------------------------------|-----------|-----------|------------|
| https://github.com/jtleek/datasharing                 |    170171 |      3858 |        546 |
| https://github.com/rdpeng/ProgrammingAssignment2      |    101258 |       469 |        117 |
| https://github.com/octocat/Spoon-Knife                |     90787 |      9969 |        308 |
| https://github.com/twbs/bootstrap                     |     50468 |    109702 |       6833 |
| https://github.com/rdpeng/ExData_Plotting1            |     43190 |       136 |         18 |
| https://github.com/angular/angular.js                 |     27738 |     55503 |       4407 |
| https://github.com/rdpeng/RepData_PeerAssessment1     |     27072 |        57 |         17 |
| https://github.com/tensorflow/tensorflow              |     26135 |     54976 |       4968 |
| https://github.com/DataScienceSpecialization/courses  |     24094 |      2538 |        819 |
| https://github.com/udacity/frontend-nanodegree-resume |     24044 |       706 |        118 |  

两个 top10 中有多少个是重叠的呢，答案是 3 个  

| Repo                                     | Star      | Fork      | Watch      |
|------------------------------------------|-----------|-----------|------------|
| https://github.com/twbs/bootstrap        |    109702 |     50468 |       6833 |
| https://github.com/angular/angular.js    |     55503 |     27738 |       4407 |
| https://github.com/tensorflow/tensorflow |     54976 |     26135 |       4968 |  

那你知道两者的 top100 中有多少个是重叠的吗，答案是 51 个，top500 是 270 个

forks 数超过 1000 的仓库共有 1586 个，看看各语言都有几个，选取排名前 10 的语言生成条形图  

![](https://github.com/chenjiandongx/Github/blob/master/images/l_forks_1000.png)  

再把维度扩大到 10000，共 41 个  

![](https://github.com/chenjiandongx/Github/blob/master/images/l_forks_10000.png)

JavaScript，Java，Python 基本上是稳居前 3 名，特别是 JavaScript，真是大红大紫，当然我大 Python 也是很有潜力的  

stars 数超过 1000 的仓库有 10410 个  

![](https://github.com/chenjiandongx/Github/blob/master/images/L_stars_1000.png)

超过 10000 的 402 个  

![](https://github.com/chenjiandongx/Github/blob/master/images/L_stars_10000.png)  

各大语言的分布情况基本上和 forks 数是一致的。唯一不同的语言就是 HTML 换成了 CSS，不过也都差不多，这两门语言基本上都是不分家的  

来看个有趣的排名，全站代码量 top3 的仓库  

| Repo                                        |
|---------------------------------------------|
|https://github.com/opengapps/arm             |
|https://github.com/kiang/data.fda.gov.tw     |
|https://github.com/hanxiao/hanxiao.github.io |  


### 了解一下 Python 的情况
Python 仓库 stars 数 top10  

| Repo                                                     | Fork      | Star      | Watch      |
|----------------------------------------------------------|-----------|-----------|------------|
| https://github.com/vinta/awesome-python                  |      6215 |     33163 |       2957 |
| https://github.com/jakubroztocil/httpie                  |      1949 |     29302 |        856 |
| https://github.com/pallets/flask                         |      8430 |     26618 |       1681 |
| https://github.com/nvbn/thefuck                          |      1273 |     26200 |        554 |
| https://github.com/rg3/youtube-dl                        |      4846 |     25453 |       1064 |
| https://github.com/django/django                         |     10298 |     25208 |       1523 |
| https://github.com/kennethreitz/requests                 |      4462 |     24600 |       1007 |
| https://github.com/ansible/ansible                       |      7496 |     22732 |       1634 |
| https://github.com/josephmisiti/awesome-machine-learning |      5320 |     21963 |       2221 |
| https://github.com/scrapy/scrapy                         |      5338 |     20053 |       1430 |

Python 仓库 forks 数 top10  

| Repo                                                     | Fork      | Star      | Watch      |
|----------------------------------------------------------|-----------|-----------|------------|
| https://github.com/shadowsocks/shadowsocks               |     10533 |     17302 |       1520 |
| https://github.com/django/django                         |     10298 |     25208 |       1523 |
| https://github.com/scikit-learn/scikit-learn             |      9952 |     18159 |       1646 |
| https://github.com/pallets/flask                         |      8430 |     26618 |       1681 |
| https://github.com/ansible/ansible                       |      7496 |     22732 |       1634 |
| https://github.com/udacity/fullstack-nanodegree-vm       |      6495 |       122 |         22 |
| https://github.com/vinta/awesome-python                  |      6215 |     33163 |       2957 |
| https://github.com/odoo/odoo                             |      6045 |      6481 |       1130 |
| https://github.com/scrapy/scrapy                         |      5338 |     20053 |       1430 |
| https://github.com/josephmisiti/awesome-machine-learning |      5320 |     21963 |       2221 |  

shadowsocks 在 stars 里排不进 top10，居然在 forks 里勇夺第一了，这梯子圆了多少人的翻墙梦。另外一架梯子 XX-NET 很遗憾，两项都没挤进 top10，扎心了老铁  

| Repo                                                     | Fork | Star | Watch |
|----------------------------------------------------------|-----------|-----------|------------|
| https://github.com/XX-net/XX-Net                         |   4682    |   13787   |       1343 |  

老规矩，看看这两个 top10 交集部分，有 5 个，如下。（ 两个前 top100 中交集有 52 个 ）   

| Repo                                                     | Star | Fork | Watch |
|----------------------------------------------------------|-----------|-----------|------------|
| https://github.com/django/django                         |     25208 |     10298 |       1523 |
| https://github.com/pallets/flask                         |     26618 |      8430 |       1681 |
| https://github.com/ansible/ansible                       |     22732 |      7496 |       1634 |
| https://github.com/vinta/awesome-python                  |     33163 |      6215 |       2957 |
| https://github.com/josephmisiti/awesome-machine-learning |     21963 |      5320 |       2221 |

两大 web 框架 django 和 flask 的表现还是不负众望的，awesome 系列在每种语言里都很受欢迎  

#### 谢谢观赏 (ง •̀_•́)ง  (,,• ₃ •,,)  

