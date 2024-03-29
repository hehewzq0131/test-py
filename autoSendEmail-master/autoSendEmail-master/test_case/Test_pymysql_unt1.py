import pymysql

def get_db():
    # 打开数据库连接
    db = pymysql.connect(
        host='192.168.30.132',
        user='db_read',
        password='DB_Read_7hRLVxSp9pF',
        db='fbs_fdc',
        port=3306,
        charset='utf8'
    )
    return db


def find_one(db, sql):
    try:
        # 使用cursor()方法获取操作游标
        cur = db.cursor()
        cur.execute(sql)
        results = cur.fetchone()
        print("one:\n",results)
        return results
    except Exception:
        print("查询失败 sql-->", sql)
        db.close()


def find_all(db, sql):
    try:
        cur = db.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        print("all:\n",results)
        return results
    except Exception:
        print("查询失败 sql-->", sql)
        db.close()


def find_many(db, sql, size=10):
    try:
        db = get_db()
        cur = db.cursor()
        cur.execute(sql)
        results = cur.fetchmany(size)
        print("many:\n",results)
        return results
    except Exception:
        print("查询失败 sql-->", sql)

def find_data(db,sql,data):
    try:
        db=get_db()
        cur=db.cursor()
        results=cur.execute(sql % data)
        print("select many data:",results)
        return results
    except Exception:
        print("查询失败 sql-->", sql)


def insert_one(db, sql):
    try:
        db = get_db()
        cur = db.cursor()
        result = cur.execute(sql)
        db.commit()
        return result  # 成功返回1
    except Exception:
        print("添加失败 sql-->", sql)
        db.rollback()  # 回滚


def insert_many(db, sql, data):
    try:
        # 使用cursor()方法获取操作游标
        db = get_db()
        cur = db.cursor()
        result = cur.executemany(sql, data)
        db.commit()
        return result  # 成功返回1
    except Exception:
        print("添加失败 sql-->", sql)
        db.rollback()  # 回滚


def update(db, sql, data):
    try:
        # 使用cursor()方法获取操作游标
        db = get_db()
        cur = db.cursor()
        cur.execute(sql % data)
        db.commit()
    except Exception as e:
        print("更新失败 sql-->", sql % data)
        db.rollback()  # 回滚
    finally:
        db.close()


def delete(db, sql, data):
    try:
        # 使用cursor()方法获取操作游标
        db = get_db()
        cur = db.cursor()
        cur.execute(sql % data)
        db.commit()
    except Exception:
        print("删除失败 sql-->", sql % data)
        db.rollback()  # 回滚
    finally:
        db.close()


if __name__ == '__main__':
    db = get_db()
    sql = "SELECT*FROM fbs_user_login_logs w limit 10 "
    # sql="SELECT * FROM  fbs_user_login_logs  WHERE id = %d "
    # find_data(db,sql,("3",7))
    find_one(db,sql)
    # find_all(db,sql)
    # find_many(db,sql)
    # s = find_one(db,"select * from student")
    # s = find_all(db,"select * from student limit 1")
    # s = find_many(db,"select * from student")
    # print(s)
    # res = insert_one(db,"INSERT INTO `kuaik`.`student` (`id`, `name`, `age`) VALUES ('1055', 'Hello', '23')")
    # print(res)

    # data = (("103","tom","24"),("104","tom","24"))
    # data = [["105","tom","24"],["106","tom","24"]] # 2种格式都可以
    # res = insert_many(db,"INSERT INTO `kuaik`.`student` (`id`, `name`, `age`) VALUES (%s,%s,%s)",data)
    # print(res)

    # update(db,"update student set name = '%s' where id = %d",("9999",101))

    # delete(db, "delete from student where id = %d", (101))
