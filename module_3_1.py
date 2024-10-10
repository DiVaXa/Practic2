calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(stroka):
    stroka = str('Avrora')
    result = (len (stroka),stroka.upper(),stroka.lower())
    count_calls()
    return result
print(string_info('Avrora'))
def string_info(stroka):
    stroka = str('Akkordik')
    result = (len (stroka),stroka.upper(),stroka.lower())
    count_calls()
    return result
print(string_info('Avrora'))
def is_contains(string,list_to_search):
    string = str('Avrora'.lower())
    list_to_search = ['Ava', 'amba', 'AvRoRa']
    count_calls()
    for i in range (len(list_to_search)):
        if str(list_to_search[i].lower())==string:
            result = True
            break
        else:
            result = False
            continue
    return result
print(is_contains('Avrora', ['Ava', 'amba', 'avRorA']))
def is_contains(string,list_to_search):
    string = str('Akkordik'.lower())
    list_to_search = ['Akk', 'akkor', 'kord']
    count_calls()
    for i in range (len(list_to_search)):
        if str(list_to_search[i].lower())==string:
            result = True
            break
        else:
            result = False
            continue
    return result
print(is_contains('Avrora', ['Ava', 'amba', 'avRorA']))
print (calls)