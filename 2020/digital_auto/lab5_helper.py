from binVectors import gen_bin_vector_5 as gen_bin_vector
from tabulate import tabulate

def del_dup(list):
    res = [] 
    for i in list: 
        if i not in res: 
            res.append(i) 
    return res

def diff_pos(str_a,str_b):
    list_a=list(str_a)    
    list_b=list(str_b)
    i=0
    while(i<len(list_a)):
        if(list_a[i]!=list_b[i]):
            return i
        i = i + 1
        
def hamming_dist(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2)) 

def truth_table(vector):
    result = []
    for i in range(0,len(vector)):
        args = vector[i][0]
        result.append([
            i+1,
            args,
            int(f_v9(args)),
            int(f_v10(args)),
            int(f_v11(args)),
            int(f_v12(args)),
            int(f(f_v9,f_v12,args)),
            int(f(f_v10,f_v12,args)),
            int(f(f_v11,f_v12,args))
            #int(f(f_v16,f_v19,args)),
            #int(f(f_v17,f_v19,args)),
            #int(f(f_v18,f_v19,args)),
        ])
    return result

def sdnf(table):
    result = []
    for i in table:
        if(bool(i[6]) or bool(i[7]) or bool(i[8])):
            signs = set()
            if bool(i[6]):
                signs.add(1)
            if bool(i[7]):
                signs.add(2)
            if bool(i[8]):
                signs.add(3)
            result.append([
                set([i[0]]),
                i[1],
                '*',
                signs
            ])
    return result

def to_next_imp(table):
    result = []
    flag = False
    for i in range(0,len(table)):
        for j in range(i,len(table)):
            if (hamming_dist(table[i][1],table[j][1]) == 1) and (not table[j][3].isdisjoint(table[i][3])):
                flag = True
                table[j][2] = ""
                table[i][2] = ""
                pos = diff_pos(table[i][1],table[j][1])
                print(table[i],'            ',table[j])
                result_str = list(table[i][1])
                result_str[pos] = '-'
                result_index_list = table[i][0] | table[j][0]
                #этот кусок поправить
                signs = table[j][3].intersection(table[i][3])
                result.append([
                    result_index_list,
                    "".join(result_str),
                    "*",
                    signs
                ])
    if(flag):
        return [table,del_dup(result)]
    else:
        return None

def impl_combination(table):
    impl_list = []
    result = []
    steps = 0
    impl_list.append(table)
    while True:
        result = to_next_imp(impl_list[steps])
        if(result == None):
            break
        impl_list[steps] = result[0]
        impl_list.append(result[1])
        steps = steps + 1
    print("Склейка закончилась на импликантах "+str(steps)+" порядка.")
    return impl_list

def simple_impl(impl_list):
    result = []
    for i in impl_list:
        for j in i:
            if (j[2] == "*"):
                result.append(j)
    return result

def impl_group(impl_list):
    result_list = []
    del_list = []
    for i in range(0,len(impl_list)):
        for j in range(i,len(impl_list)):
            if(impl_list[i][0].issuperset(impl_list[j][0]) and impl_list[i]!=impl_list[j] and (impl_list[i][1] == impl_list[j][1])):
                print(impl_list[i],impl_list[j])
                del_list.append(impl_list[i])
                del_list.append(impl_list[j])
                result_list.append([
                    impl_list[i][0],
                    impl_list[i][1],
                    impl_list[i][2],
                    impl_list[i][3] | impl_list[j][3]
                ])
            else:
                if impl_list[i] not in result_list:
                    result_list.append(impl_list[i])
                if impl_list[j] not in result_list:
                    result_list.append(impl_list[j])
    for i in del_list:
        while i in result_list:
            result_list.remove(i)
    return result_list

def implicant_table(impl_list,table):
    #заполнение заголовка
    table_head = []
    for i in impl_list:
        table_head = table_head + i[0]
    table_head = del_dup(table_head)
    table_head.sort()
    table_head.insert(0,"Простая импликанта")
    #заполнение тела
    table_body = []
    for i in impl_list:
        table_str = []
        table_str.append(i[1])
        for j in range(1,len(table_head)):
            if table_head[j] in i[0]:
                table_str.append("*")
            else:
                table_str.append("")
        table_body.append(table_str)
    list_to_remove = []
    for index,i in enumerate(table,start=0):
        if(i[3]==False):
            list_to_remove.append(index+1)
    for i in list_to_remove:
        for index,j in enumerate(table_head,start=0):
            if(i==j):
                del table_head[index]
                for k in table_body:
                    del k[index]
    return (table_head,table_body)

def latex_sdnf_func(impl_list):
    result_str = ""
    for i in impl_list:
        result_str = result_str+"( "
        pos = 1
        for j in i[1]:
            if (j == '1'):
                result_str = result_str + 'x_' + str(pos)
            elif(j == '0'):
                result_str = result_str + r'\overline '+'x_'+str(pos)
            pos = pos + 1
        result_str = result_str + r" ) \lor "
    return result_str[0:-6]

def latex_sknf_func(impl_list):
    result_str = ""
    for i in impl_list:
        result_str = result_str+"( "
        pos = 1
        for j in i[1]:
            if (j == '1'):
                result_str = result_str + r'\overline '+'x_'+str(pos) + ' \lor '
            elif(j == '0'):
                result_str = result_str + 'x_' + str(pos) + ' \lor '
            result_str = result_str[0:-5]
            pos = pos + 1
        result_str = result_str + r" ) \land "
    return result_str[0:-7]

def factor_sdnf_table(simple_impl_list):
    table_head = ['']
    table_body = []
    for i in range(0,len(simple_impl_list[0][1])):
        table_head.append(r'$'+r'x'+str(i+1)+r'$')
        table_head.append(r'$'+r'\overline x'+str(i+1)+r'$')
    for i in simple_impl_list:
        temp_list = [i[1]]
        for j in i[1]:
            if (j =='0'):
                temp_list.append('')
                temp_list.append('*')
            elif (j =='1'):
                temp_list.append('*')
                temp_list.append('')
            else:
                temp_list.append('')
                temp_list.append('')
        table_body.append(temp_list)
    return (table_head,table_body)

def factor_sknf_table(simple_impl_list):
    table_head = ['']
    table_body = []
    for i in range(0,len(simple_impl_list[0][1])):
        table_head.append(r'$'+r'x'+str(i+1)+r'$')
        table_head.append(r'$'+r'\overline x'+str(i+1)+r'$')
    for i in simple_impl_list:
        temp_list = [i[1]]
        for j in i[1]:
            if (j =='0'):
                temp_list.append('*')
                temp_list.append('')
            elif (j =='1'):
                temp_list.append('')
                temp_list.append('*')
            else:
                temp_list.append('')
                temp_list.append('')
        table_body.append(temp_list)
    return (table_head,table_body)

def factorisation(table_tuple):
    table_head = table_tuple[0]
    table_body = table_tuple[1]
    #поиск строки с наибольшим вхождением
    def find_max_str(list):
        max_value = 0
        max_index = 0
        for index,i in enumerate(list,start=0):
            if(max_value<i.count('*')):
                max_index = index
                max_value = i.count('*')
        if max_value == 2:
            return None
        return max_index
    def max_sim(list,row):
        max_index = 0
        max_sim_count = 0
        for index,i in enumerate(list,start=0):
            if list[row] == i:
                continue
            else:
                sim_count = 0
                for j in range(1,len(i)):
                    if i[j]==list[row][j]:
                        sim_count = sim_count+1
                if(sim_count>max_sim_count):
                    max_sim_count = sim_count
                    max_index = index
        return max_index
    current_rows_count = len(table_body)
    current_columns_count = len(table_body[0])

    max_str_index = find_max_str(table_body) 
    max_sim_index = max_sim(table_body,max_str_index)
    for step in range(1,10):
        new_list = ['z'+str(step)]
        table_head.append('u'+str(step))
        #заполнение новой строки
        for j in range(1,len(table_body[max_str_index])):
            if (table_body[max_str_index][j] == '*') and (table_body[max_sim_index][j] == '*'):
                table_body[max_str_index][j] = ''
                table_body[max_sim_index][j] = ''
                new_list.append('*')
            else:
                new_list.append('')
        table_body.append(new_list)
        #заполнение нового столбца
        for index,i in enumerate(table_body,start=0):
            if index == max_str_index:
                table_body[index].append('*')
            elif index == max_sim_index:
                table_body[index].append('*')
            else:
                table_body[index].append('')
    return (table_head,table_body)

def f_v9(str_val):
    x1 = str_val[0]
    x2 = str_val[1]
    x3 = str_val[2]
    x4 = str_val[3]
    x5 = str_val[4]
    return (
        3 < (int(x4 + x5,2) + int(x1 + x2 + x3,2)) < 8 
    ) 

def f_v10(str_val):
    x1 = str_val[0]
    x2 = str_val[1]
    x3 = str_val[2]
    x4 = str_val[3]
    x5 = str_val[4]
    return (
        4 <= (int(x4 + x5,2) + int(x1 + x2 + x3,2)) <= 6 
    ) 

def f_v11(str_val):
    x1 = str_val[0]
    x2 = str_val[1]
    x3 = str_val[2]
    x4 = str_val[3]
    x5 = str_val[4]
    return (
        5 <= (int(x2 + x3,2) + int(x4 + x5 + x1,2)) <= 8 
    ) 

def f_v12(str_val):
    x1 = str_val[0]
    x2 = str_val[1]
    x3 = str_val[2]
    x4 = str_val[3]
    x5 = str_val[4]
    return (
        -2 <= (int(x1 + x2,2) - int(x3 + x4 + x5,2)) <= 1 
    ) 

def f(f1,f2,str_val):
    return f1(str_val) and f2(str_val)

table_head = ["№","$x_1x_2x_3x_4x_5$","f_v9","f_v10","f_v11","f_v12","f1","f2","f3"]
table = truth_table(gen_bin_vector())
print(tabulate(table,table_head,tablefmt="simple"))

sdnf_table = sdnf(table)
table_head = ["№","$x_1x_2x_3x_4x_5$","Простая импликанта?","Признаки принадлежности"]
print(tabulate(sdnf_table,table_head,tablefmt="simple"))
impl_list = impl_combination(sdnf_table)
impl_list_head = ["№","$x_1x_2x_3x_4x_5$","Простая импликанта?","Признаки принадлежности"]
for i in impl_list:
    print(tabulate(i,impl_list_head,tablefmt="simple"))

simple_impl_list = simple_impl(impl_list)
simple_impl_list = impl_group(simple_impl_list)
print('Список простых импликант')
print(tabulate(simple_impl_list,impl_list_head,tablefmt="simple"))

#print('\nТаблица простых импликант')
#impl_table = implicant_table(simple_impl_list,table)
#print(tabulate(impl_table[1],impl_table[0],tablefmt="latex"))

#print(latex_sknf_func(simple_impl_list))
#result = factor_sknf_table(simple_impl_list)
#print(tabulate(result[1],result[0],tablefmt="fancy_grid"))
