<!-- webApp.md -->
<!-- author:fudamai -->

## 目标
做一个购物网站，从前端到后端。

购物网站还要配合今天的互联网基础，所以最可能的还是小程序。  
但这里只讨论web端的实践。

想做购物网站是因为我家有个小店，一个超市，我想从零开始将超市放  
到线上。这个购物网站以实体店为依撑，实体店不仅要保持原有功能，还要作为网站的仓储空间。以下将购物网站称为网站

首先我们分析以下，将店铺开到线上的好处。  
开店是为了赚钱，也可以说是增加自己的财产。赚钱有两个途径：  
1.开源  
2.节流  
我们分别来描述这两点：

### **开源**
开源也就是增加输入性财产。对于一家超市而言，开源就是增加客流  
量，增加营业性收入。  

*传统情况下，超市如何增加这两点的数据呢。*  
最常见的情况就是，发传单，做活动。通过广撒网，以及在部分商品  
上的让利来增加客流量，然后尽可能地让顾客在店内购买那些没有参加让  
利地活动的商品，以拉高整体销售额，提高利润。这种活动配合会员让利  
让利系统，可以增加顾客的回头率，培养用户来店购物习惯。

*将超市放到线上*  
这种情况下，用户可以直接预定货品。注意这里的货品指的是，本超市里  
没有现货，但超市可以去找供应商采购的货品。这类货品，存在以下三种  
情况：1.购买频次及购买量都不大、2.购买频次低但单词购买量大  
第一种情况，有如下商品：各种低耗的电器、线材、清洁用品  
第二种情况，有如下情况：红白喜事干鲜、定亲礼品、走亲戚礼品

预定商品，主要是将以前线下需要直接找老板联系的预定帮到线上，放入  
一个统一的系统，防止人为操作会发生的遗忘、错配等疏漏

### **节流**
将超市放到线上可以进行节流，下面我们来具体讲以下原理

超市经常会出现尾货处理不掉，或者小件货品由于放置位置不显眼导致  
的成本浪费。

小件货品有相当部分是小型的日用品，这种商品在销售过程中呈现细、  
碎的特征。时间一久，销售人员也不记得是否有这件货品。这种情况下  
很容易出现成本的损失。

将超市上线，并将这些货物信息存入数据库中。首先就解决了由于货物  
信息丢失导致的成本损失，也让消费者能更方便的找到这些小型的日用品。

## 功能需求分析
1.超市库存管理系统  
- 库存管理，为购物网站提供商品信息接口

2.信息分发系统  
- 向会员分发各种优惠信息，形式可为：短信、邮件。。。

3.商品信息快照  
- 输出图文照片，方便宣传

4.购物网站  
- 用于商品信息展示，要能连上公网