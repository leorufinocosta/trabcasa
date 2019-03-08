logins = {"Leo": '123', "Ana": '123', "Bea": '123'}

disciplinas = {"Leo": [['LPT'],[5.6,7.7,8],['LAB PROG'],[10,8,9.5],['TGA'],[4,4.8,9]],
               'Ana': [['LTP'],[7,9.3,8.3],['LAB PROG'],[1,3.6,6.9],['TGA'],[7,4.5,3.8]],
               'Bea': [['LTP'],[4.9,5.6],["LAB PROG"],[5.6,8,9.3],['TGA'],[8.1,9,7.8]]
               }


def get_login(logg,senha):
    return (logg in logins) and (logins[logg] == senha)

def get_disciplinas(login):
    return disciplinas[login]
    #if logins['Leo']:
     #   return disciplinas[login]
   # elif logins['Ana']:
    #    return disciplinas[login]
   # elif logins['Bea']:
   #     return disciplinas[login]
   # else:
    #    return False
