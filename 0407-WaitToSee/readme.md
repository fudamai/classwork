# fudamai_demo

> Author: fudamai

代码文件在core文件夹。执行时，将在db文件夹下保存一个json文件，保存抓取的数据。

要求一：完成

要求二：鉴于疫情信息的更新频率不高，一天只保存一次。未设置redis记录过期时间。

要求三：没写。但在对json文件的分析中发现，json文件中包含了更新时间，以及精确到到市一级的国内数据。如果要实现查询全国数据，需对这些数据进行处理。

示例代码，从redis中取保存的数据
```
client = redis.Redis()

data = client.get('celery-task-meta-fedecad9-e593-4fdd-b8e7-fb30d0b7186d')

json_data = json.loads(data) 

json_data['result']['component'][0]['mapLastUpdatedTime']  
```
``` 
In [27]: json_data['result']['component'][0]['mapLastUpdatedTime']                                       
Out[27]: '2020.04.11 16:48'

```

在Linux虚拟机上的运行目录只有core与db。
