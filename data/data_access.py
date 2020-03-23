import pymysql
import time
import datetime


class DataAccess():
    def __init__(self, host='localhost', user='root', password='123456', db='test', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.conn = None
        self.cursor = None

    def open_conn(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, port=self.port,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def select_(self, sql):
        try:
            self.open_conn()
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            raise e
        finally:
            self.conn.close()
            self.cursor.close()

    def update_(self, sql):
        try:
            self.open_conn()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
        finally:
            self.conn.close()
            self.cursor.close()

    def select_version(self):
        # import functools
        # s = functools.partial(self.select, sql='SELECT VERSION()')
        # return s()[0]
        return self.select(sql='SELECT VERSION()')[0][0]

    def insert_action(self, DZ, FLAG='start'):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into DZ(SJC,GRGH,LJGH,DZ,FLAG) values("%s","%s","%s","%s","%s")' % (
        current_time, '1A', '0A', DZ, FLAG)
        self.update_(sql)


# 耗材分时监控表
class MaterialData(DataAccess):
    def __init__(self):
        super(MaterialData, self).__init__()

    def select(self):
        sql = ''
        result = self.select_(sql)
        return result

    def update(self, sql):
        sql = ''
        self.update_(sql)


# OEE效能日推表
class OEEData(DataAccess):
    def __init__(self):
        super(OEEData, self).__init__()

    def select(self):
        sql = 'Select * from oee_date'
        result = self.select_(sql)
        return result

    def update(self, sql):
        self.update_(sql)



# 设备工作损失时间统计表
class EquipmentTimeData(DataAccess):
    def __init__(self):
        super(EquipmentTimeData, self).__init__()

    def select(self):
        sql = 'Select * from loss'
        result = self.select_(sql)
        return result

    def update(self, sql):
        self.update_(sql)


# 设备工作损失时间占比表
class EquipmentData(DataAccess):
    def __init__(self):
        super(EquipmentData, self).__init__()

    def select(self):
        sql = 'Select * from loss'
        result = self.select_(sql)
        return result

    def update(self, sql):
        self.update_(sql)


if __name__ == "__main__":
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    da_oee = OEEData()  # 对oee实时利用率进行统计
    result_oee = da_oee.select_('select * from oee_date ORDER BY SJC DESC limit 1')
    if str(result_oee[0][0]) != current_time:
        da_oee.update_('insert into oee_date(SJC,O8,O9,O10,O11,O12,O13,O14,O15,O16,O17,O18)values'
                      '("'+current_time+'",0,0,0,0,0,0,0,0,0,0,0)')
    else:
        pass

    # dz="action2"
    # time_diff=160
    # lossTime=EquipmentTimeData()
    # current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # #lossTime.update_('insert into loss(SJ,action1,action2,action3,action4,action5,action6)values("%s",%d,%d,%d,%d,%d,%d)'%(current_time,0,0,0,0,0,0))
    # result=lossTime.select_("select * from loss ORDER BY SJ DESC limit 1")
    # zongshijian=time.strftime('%H:%M:%S',time.localtime(time.time()))
    # print(zongshijian)
    # huanxing=result[0][1]
    # dailiao=result[0][2]
    # shebeiguzhang=result[0][3]
    # tingzhi=result[0][4]
    # # qitashijian=result[0][5]
    # # kongyunzhuan=result[0][6]
    # fuheshijian=(int(zongshijian.split(':')[0])-8)*3600+int(zongshijian.split(':')[1])*60+int(zongshijian.split(':')[2])-tingzhi
    # shijijiagong_1=fuheshijian-huanxing-dailiao-shebeiguzhang
    # eff=int(shijijiagong_1/fuheshijian*100)
    # print(eff)

