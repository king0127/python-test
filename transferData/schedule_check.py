

# 验证计划模块

import old_mysql_util

sql = "SELECT GROUP_CONCAT(t.id SEPARATOR ',') as taskId from task t LEFT JOIN task_attribute ta on t.id = ta.task_id where t.deleted_at is null and ta.deleted_at is null and ta.schedule_id = 122468 ORDER BY t.id"

def old_schedule_info(sql):
    # 通过计划ID查询计划基础信息
    return old_mysql_util.old_schedule_mysql(sql)


def new_schedule_info(sql):
    # 通过计划ID查询计划基础信息
    return old_mysql_util.new_schedule_mysql(sql)


