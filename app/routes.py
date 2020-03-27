from app import app
from gensim.models import word2vec
from gensim import models
import logging
from flask import Flask,request
import os
import sys


@app.route('/')
@app.route('/index')
def index():
    get_current_path()
    return "Hello, World!"

@app.route('/demo')
def demo():
  logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
  model = models.Word2Vec.load('word2vec.model')
  print("提供3种测试模式\n")
  print("输入一个词，则去寻找前10个相似的词")
  print("输入两个词，计算两个词的相似度")
  print("输入三个词，则进行词类推")
  try:
    q_list = request.args.get("word").split(" ")
    result = ' '
    if len(q_list) == 1:
      print("相似词 10 排序")
      res = model.most_similar(q_list[0],topn = 10)
      for item in res:
        result += str(item[0])+ ',' + str(item[1]) + ' <br/>' 
        print(item[0]+ ',' +str(item[1]))
    elif len(q_list) == 2:
      print("计算 Cosine 相似度")
      res = model.similarity(q_list[0],q_list[1])
      result = str(res)
      print(res)
    else:
      print("%s之于%s，如%s之于" % (q_list[0],q_list[2],q_list[1]))
      res = model.most_similar([q_list[0],q_list[1]], [q_list[2]], topn= 10)
      for item in res:
        result += item[0]+ ',' +str(item[1]) + ' <br/>'
        print(item[0]+ ',' +str(item[1]))
        print("----------------------------")
    return result
  except Exception as e:
    print(repr(e))

def get_current_path():
  paths = sys.path
  current_file = os.path.basename(__file__)
  for path in paths:
    try:
      print(path)
    except (FileExistsError,FileNotFoundError) as e:
      print(e)