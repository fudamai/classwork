# 作业说明
- 两个答案代码都定义了入口函数，路径 ./bin/main.py

## 差评分析：
- 爬取差评之前试过能爬，但写完入口函数后再爬就只返回“userClientShow”,没法爬新数据了，   新添加的手动命名没测试。
- 评论分析正常，自动命名功能正常
## 数据处理：
- 使用装饰器处理验证、登录，并返回用户信息。
- 功能：根据json中的operation确定用户可使用功能。weighting、blacklist操作必须是用户身份  （type）为admin时才可使用。
- 问题：切换用户必须退出程序重新登录。