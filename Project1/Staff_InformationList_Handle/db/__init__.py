# _*_coding:utf-8_*_
# creat by John Green
import os
import sys

PATH_DB = os.path.dirname(os.path.abspath(__file__))
print(PATH_DB)
sys.path.append(PATH_DB)

COLUMNS = ['id','name','age','phone','dept','enrolled_date']

# 打印颜色
def print_log(msg,log_type='info'):
    if log_type =='info':
        print("\033[32;1m%s\033[0m" % msg)
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m"%msg)

# 加载数据
def load_db():
    '''
    加载数据
    :return:
    '''
    data = {}
    for i in COLUMNS:
        data[i] = []


    f = open("staff", 'r')

    for line in f:
        staff_id,name,age,phone,dept,enrolled_date = line.split(',')
        data['id'].append(staff_id)
        data['name'].append(name)
        data['age'].append(age)
        data['phone'].append(phone)
        data['dept'].append(dept)
        data['enrolled_date'].append(enrolled_date)
    #print(data)
    return data

STAFF_DATA = load_db()

# 保存数据
def save_db():
    '''
    把内存数据存回硬盘
    :return:
    '''
    f = open("staff",'w',encoding='utf-8')
    for index,staff_id in enumerate(STAFF_DATA['id']):
        row = []
        for col in COLUMNS:
            row.append( STAFF_DATA[col][index] )
        f.write(",".join(row))
    f.close()
    #os.rename("","")

#删除数据
def del_db(staff_id):
    '''
    把内存数据存回硬盘
    :return:
    '''
    f = open("staff",'r+',encoding='utf-8')
    print(staff_id)

    print(load_db())
    #for index,staff_id in enumerate(STAFF_DATA['id']):


    #STAFF_DATA.pop( STAFF_DATA['id'][8] )
    #f.write(",".join(STAFF_DATA))

    f.close()


# '>','<',' ,'=','like'
def op_gt(column,condition_val):
    '''
    :param column: age
    :param condition_val: 22
    :return:
    '''
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):
        if float(val) >float(condition_val): #匹配上了
            print("match",val)

            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)

    return matched_records
def op_lt(column,condition_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if float(val) < float(condition_val):  # 匹配上了
            print("match", val)

            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)

    return matched_records
def op_eq(column,condition_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if val == condition_val:  # 匹配上了
            print("match", val)

            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)

    return matched_records
def op_like(column,condition_val):
    matched_records = []
    for index, val in enumerate(STAFF_DATA[column]):
        if condition_val in val:  # 匹配上了
            print("match", val)

            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)

    return matched_records

def syntax_where(clause):
    '''
    解析where条件，并过滤数据
    :param clause:
    :return:
    '''
    operators = {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like,
    }
    for op_key,op_func in operators.items():
        if op_key in clause:
            print("clause:",clause)
            column,val = clause.split(op_key)
            matched_data = op_func(column.strip(),val.strip()) #真正的查询数据
            print(matched_data)
            return matched_data

    else: #只有在for执行完成，且中间没有被break,才执行。(没有匹配上任何条件公式)
        print_log("语法错误：where条件只支持(>,<,=,like)",'error')


def syntax_find(data_set,left_clause):
    '''
    解析查询语句并从data_set中打印指定的列
    :param data_set: [['2011-04-01\n', '24', 'IT', '1', 'Jack Ma', '15555182321'], ['2012-04-01\n', '34', 'IT', '2', 'Black Ja', '13555181425'],
    :param query_clause: eg: find name,age from staff_table
    :return:
    '''
    #filter_cols = query_clause.split("from")[0].split()[1:][0].split(',')
    filter_cols_tmp = left_clause.split("from")[0][4:].split(',') #万一有逗号
    filter_cols = [i.strip() for i in filter_cols_tmp] #去掉空格
    if '*' in filter_cols[0]:
        print(data_set,filter_cols)
        #print_log(filter_cols)
    else:
        reformat_data_set = []
        for row in data_set:
            filtered_vals = []  # 把要打印的字段放在这个列表里
            for col in filter_cols:
                col_index = COLUMNS.index(col)  # 拿到列的索引，依次取出每条记录里对应索引的值
                filtered_vals.append(row[col_index])
            reformat_data_set.append(filtered_vals)
        for r in reformat_data_set:
            print(r)
    print_log("成功找到了%s 条语句！" % len(data_set))
        # for row in matched_data:
        #     for col in filter_cols:
        #         col_index = COLUMNS.index(col)
        #         print(col, row[col_index])

def syntax_delete(data_set,left_clause):
    '''
    删除数据
    :param data_set:
    :param left_clause: eg,update staff_table set age=95 where name=Jack Ma
    :return:
    '''
    print("aaaa:%s"%data_set)
    formula_raw = left_clause.split('set')
    if len(formula_raw) > 1:  # 有set关键字
        col_name, new_val = formula_raw[1].strip().split('=')  # age=25
        #col_index = COLUMNS.index(col_name)
        # 循环data_set,取到每条记录的id,拿着这个id到STAFF_DATA['id']里找到对应的id索引
        # 再拿这个索引，去STAFF_DATA['age']列表里，修改对应的索引的值

        for matched_row in data_set:

            staff_id = matched_row[0]
            print(staff_id)
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        print("ggggggg:%s"%data_set)

        #print(STAFF_DATA)
        del_db(staff_id) #把修改的数据刷到硬盘上

        print_log("成功删除了%s 条语句！"%len(data_set))
    else:
        print_log("语法错误：未检测到关键词", 'error')


def syntax_update(data_set,left_clause):
    '''
    修改数据
    :param data_set:
    :param left_clause: eg,update staff_table set age=95 where name=Jack Ma
    :return:
    '''
    formula_raw = left_clause.split('set')
    if len(formula_raw) > 1:  # 有set关键字
        col_name, new_val = formula_raw[1].strip().split('=')  # age=25
        #col_index = COLUMNS.index(col_name)
        # 循环data_set,取到每条记录的id,拿着这个id到STAFF_DATA['id']里找到对应的id索引
        # 再拿这个索引，去STAFF_DATA['age']列表里，修改对应的索引的值

        for matched_row in data_set:

            staff_id = matched_row[0]
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        print(STAFF_DATA)
        save_db() #把修改的数据刷到硬盘上

        print_log("成功修改了%s 条语句！"%len(data_set))
    else:
        print_log("语法错误：未检测到关键词", 'error')


def syntax_add(data_set,query_clause):
    pass

def syntax_parser(cmd):
    '''
    解析语句，并执行
    :return:
    '''
    syntax_list = {
        'find': syntax_find,
        'del': syntax_delete,
        'update': syntax_update,
        'add': syntax_add,
    }
    #find name,age from staff_table where age>22
    if cmd.split()[0] in ('find','add','del','update'):
        if ' where' in cmd:
            left_clause,right_clause = cmd.split('where')
            matched_records = syntax_where(right_clause)
            print(left_clause,right_clause)
        else:
            matched_records = []
            for index, staff_id in enumerate(STAFF_DATA['id']):
                record = []
                for col in COLUMNS:
                    record.append(STAFF_DATA[col][index])
                matched_records.append(record)
            left_clause = cmd
        cmd_action = cmd.split()[0]

        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records, left_clause)

            # cmd_action = left_clause.split()[0]
            # if cmd_action in syntax_list:
            #     #调用synatax_find,delete.. 函数，把matched_records,和left_clause的值传过去
            #     syntax_list[cmd_action](matched_records, left_clause)
        else:
            print_log("语法错误：只支持find，add,del,update指令")

    else:
        print_log("Syntax Error[only find,add,del,update]",'error')

def main():
    '''
    让用户数据语句，并执行
    :return:
    '''
    while True:
        cmd = input("[staff_db]:").strip()
        if not cmd: continue

        syntax_parser(cmd)
main()







