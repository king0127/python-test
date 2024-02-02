
import pymysql

# conn = pymysql.connect(host='localhost', user='root', passwd='wang0127', port=3306, db='wms_order', charset='utf8')
# 查询老版本数据
def old_schedule_mysql(sql):
    conn = pymysql.connect(host='tidb.it.lixiangoa.com', user='new_wb_r', passwd='N0vzrIJliiZZsGwW', port=4000, db='vds_schedule', charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data

def old_vdp_mysql(sql):
    conn = pymysql.connect(host='tidb.it.lixiangoa.com', user='new_wb_r', passwd='N0vzrIJliiZZsGwW', port=4000, db='vds_vdp', charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data


def new_schedule_mysql(sql):
    conn = pymysql.connect(host='testone57-mysql-testone.chj.cloud', user='vrdos_workbench_schedule_rw', passwd='&f5jAj0Iuh^L*BAR9pj', port=37002, db='vrdos_workbench_schedule', charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data


def new_doc_mysql(sql):
    conn = pymysql.connect(host='testone57-mysql-testone.chj.cloud', user='vrdos_workbench_document_rw', passwd='iYpw6KSisOlT6!!D^%@', port=37002, db='vrdos_workbench_document', charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    return data


