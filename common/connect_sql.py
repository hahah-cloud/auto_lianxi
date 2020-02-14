import pymysql

dbinfo = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "wangman123",
    "port": 3306
}


class DbConnect():
    def __init__(self, db_cof, database="guest"):
        self.db_cof = db_cof
        # 打开数据库
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

        '''查询数据库'''

    def select(self, sql):
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

        '''执行，删除，修改，提交语句'''

    def execute(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时候回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


if __name__ == '__main__':
    db = DbConnect(db_cof=dbinfo, database="guest")
    select_sql = "select * from test_xuexi where name='xiaohong';"
    result = db.select(select_sql)
    print(result)
