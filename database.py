import sqlite3
import time
conn = sqlite3.connect('yq.db',check_same_thread=False)

print("数据库打开成功")
c = conn.cursor()
# c.execute('''CREATE TABLE ZZYQ
#        (ID INT PRIMARY KEY     NOT NULL,
#        release_index           TEXT    NOT NULL,
#        home_address    TEXT     NOT NULL,
#        com_address     TEXT,
#        release_date    INTEGER,
#        location_x        double,
#        location_y      duoble);''')
# print ("数据表创建成功")
# conn.commit()
# conn.close()


def inser_data(info={}):
    insql = "INSERT INTO ZZYQ VALUES ({},'{}','{}','{}',{},{},{})"
    release_index = info['release_index']
    home_address = info['home_address']
    com_address = info['com_address']
    release_date = info['release_date']
    location_x = info['location_x']
    location_y = info['location_y']
    insql = insql.format(create_id(),
                         release_index,
                         home_address,
                         com_address,
                         release_date,
                         location_x,
                         location_y)
    print(insql)
    try:
        c.execute(insql)
        conn.commit()
    except Exception as e:
        print("insert error :",e)



def query_data():
    query_sql = "select * from ZZYQ"
    r = c.execute(query_sql)
    result_list=[]
    for i in r:
        result={}
        result['release_index']=i[1]
        result['location_x']=i[5]
        result['location_y']=i[6]
        result_list.append(result)
        print("id :"+str(i[0]))
        print("release_index :"+i[1])
        print("home_address :"+i[2])
        print("com_address :"+i[3])
        print("release_date :"+str(i[4]))
        print("location_x :"+str(i[5]))
        print("location_y :"+str(i[6]))
    return result_list
    



def create_id():
    return int(str(time.time()).split('.')[1])



