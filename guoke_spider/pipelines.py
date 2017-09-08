# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import MySQLdb
import pymysql as pymysql
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi
import os
from scrapy.exporters import JsonItemExporter




class GuokeSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

#自定义json文件的导出
class JsonWithEncodingPipeline(object):
    '''
    返回json数据到文件
    '''
    def __init__(self):
        self.file = codecs.open("article.json",'w',encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()


class JsonExporterPipeline(object):
    # scrapy提供的Json export 导出json文件
    def __init__(self):
        self.file = codecs.open("articlexport.json",'wb')
        self.exporter=JsonItemExporter(self.file,encoding="utf-8",ensure_ascii=False)
        self.exporter.start_exporting()
    def spider_closed(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item
class MysqlPipeline(object):
    '''
    插入mysql数据库
    '''
    def __init__(self):
        self.conn =pymysql.connect(host='172.24.22.178',port=3306,user='root',passwd='1029384756',db='bole_spider',use_unicode=True, charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        insert_sql = '''
        insert into boleitem(title,create_date,url,url_object_id,front_image_url,front_image_path,comment_nums,fav_nums,praise_nums,tag,content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''
# mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123456' WITH GRANT OPTION;  解决访问被拒绝
        self.cursor.execute(insert_sql,(item["title"],item["create_date"],item["url"],item["url_object_id"],item["front_image_url"],item["front_image_path"],item["comment_nums"],item["fav_nums"],item["praise_nums"],item["tag"],item["content"]))
        self.conn.commit()#connect执行commit


# class MysqlTwistedPipline(object):
#     '''
#     采用异步的方式插入数据，防止造成堵塞（上面那个方法会堵塞）
#     '''
#     def __init__(self,dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls,settings):
#
#         # dbpool = adbapi.ConnectionPool("pymysql",host='172.24.22.178',port=3306,user='root',passwd='1029384756',db='bole_spider',use_unicode=True, charset="utf8")
#
#         dbpool = adbapi.ConnectionPool(DB_SERVER,**DB_CONNECT)
#         return cls(dbpool)
#     def process_item(self,item,spider):
#         '''
#         使用twisted将mysql插入变成异步
#         :param item:
#         :param spider:
#         :return:
#         '''
#         query = self.dbpool.runInteraction(self.do_insert,item)
#
#         query.addErrback(self.handle_error)
#
#     def handle_error(self,failure):
#         #处理异步插入的异常
#         print(failure)
#
#     def do_insert(self,cursor,item):
#         #具体插入数据
#         insert_sql = '''
#         insert into jobbole_article(title,create_date,url,url_object_id,front_image_url,front_image_path,comment_nums,fav_nums,praise_nums,tag,content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#         '''
#         cursor.execute(insert_sql,(item["title"],item["create_date"],item["url"],item["url_object_id"],item["front_image_url"],item["front_image_path"],item["comment_nums"],item["fav_nums"],item["praise_nums"],item["tag"],item["content"]))
#


class ArticleImagePipeline(ImagesPipeline):
    '''
    对图片的处理
    '''
    def item_completed(self, results, item, info):

        for ok ,value in results:
            if ok:
                image_file_path = value["path"]
                item['front_image_path'] = image_file_path
            else:
                item['front_image_path'] = ""


        return item