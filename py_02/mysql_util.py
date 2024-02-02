
import pymysql

# conn = pymysql.connect(host='localhost', user='root', passwd='wang0127', port=3306, db='wms_order', charset='utf8')
# 查询数据
def connect_mysql(sql):
    conn = pymysql.connect(host='localhost', user='root', passwd='wang0127', port=3306, db='wms_order', charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def query_mysql(sql):
    # sql = 'select * from order_info where is_del = 0'
    data = connect_mysql(sql)
    for d in data:
        print(d)

# 新增
def insert_mysql(sql):
    conn = pymysql.connect(host='localhost', user='root', passwd='wang0127', port=3306, db='wms_order', charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except:
        print('insert into get a exception')
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# 批量新增
def batch_insert(sql, val):
    print('打印sql', sql, val)
    conn = pymysql.connect(host='localhost', user='root', passwd='wang0127', port=3306, db='wms_order', charset='utf8')
    cur = conn.cursor()
    try:
        cur.executemany(sql, val)
        conn.commit()
    except Exception as e:
        print('异常', e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


# 更新
def update_mysql(sql):
    print('打印更细SQL',  sql)
    conn = pymysql.connect(host='localhost', user='root', passwd='wang0127', port=3306, db='wms_order', charset='utf8')
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print('更新数据异常', e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()


# sql = 'insert into order_info values (7, "华为META60", 0)'
# insert_mysql(sql)

# 批量新增
values = []
for i in range(5):
    values.append((int(8+i), "华为", 0))
sql = "INSERT INTO order_info values(%s,%s,%s)"
# print(sql)
# batch_insert(sql, values)


# update_sql = 'update order_info set name = "华为META70" where id = 12 and is_del = 0'
# update_mysql(update_sql)



part_val = []
for i in range(15000):
    part_val.append((int(i), "V_"+str(i), "", 0))
sql = "INSERT INTO t_part values (%s, %s, %s, %s)"
batch_insert(sql, part_val)






