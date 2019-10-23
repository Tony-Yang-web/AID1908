"""
创建数据 dict 使用utf8编码
创建表word 分为三个字段
id word mean
将dict.txt 中的所有单词存入表中
"""
import pymysql
import re

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
# 生成游标对象
cur = db.cursor()
#插入单词
fr = open('dict.txt')
args_list = []
for line in fr:
    #获取单词和解释
    tup=re.findall(r"(\S+)\s+(.*)",line)[0]
    args_list.append(tup)
    # word = line.split(' ', 1)[0]
    # mean = line.split(' ', 1)[-1].strip()
    # args_list.append((word, mean))
fr.close()
#异常报错处理
try:

    sql = "insert into words (word,mean) values (%s,%s); "
    cur.executemany(sql, args_list)
    db.commit()  # 将操作结果立即提交
except Exception as e:
    db.rollback()
    print(e)

# 关闭游标和数据库连接
cur.close()
db.close()


#未发放的广发国际环境恢复速度
