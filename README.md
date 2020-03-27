# 通过restful方式对外提供已经训练好的模型

## Flask

Flask算是Non Full-Stack Web框架代表，是一个轻量级的Web Framework，它在中国的应用其实挺广的。它的设计目的是帮助构建一个稳定的Web基础应用。它的灵活性体现在，它的模块化设计可以轻松适合开发者的需求。Flask跟Django比起来，你可以自己造轮子，也可以是以插件的形式使用第三方库。使用Restful request的风格，很适合开发web api，Flask也更加pythonic。

## 步骤

1. 安装web框架

'pip install flask'

2. clone 代码到本地

3. 命令行运行

flask run

4. 浏览器访问

输入一个词，则去寻找前10个相似的词

http://localhost:5000/demo?word=张飞

输入两个词，计算两个词的相似度

http://localhost:5000/demo?word=刘备 关羽

输入三个词，则进行词类推

http://localhost:5000/demo?word=刘备 关羽 张飞
