import pymysql


# 连接mysql
config = {
    'host': '192.168.1.116',
    'port': 3306,
    'user': 'root',
    'passwd': 'poms@db',
    'db':'mymonitor',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
conn = pymysql.connect(**config)
# conn.autocommit(1)
# 使用cursor()方法获取操作游标
cur = conn.cursor()

# 1.查询操作
# 编写sql 查询语句
sql = "select article_title from article_detail where extracted_time>DATE_SUB(CURRENT_DATE(),INTERVAL 0 day) limit 10"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    # print('{:20}{:100}'.format("website_no", "article_title"))
    # 遍历结果
    article_title_set = ''
    for row in results:
        # website_no = row['website_no']
        article_title = row['article_title']
        # print('{:20}{:100}'.format(website_no, article_title))
        article_title_set = article_title_set + '\n' + article_title
    print(article_title_set)
except Exception as e:
    raise e
finally:
    conn.close()  # 关闭连接

