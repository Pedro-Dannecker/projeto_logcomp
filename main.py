from ast import parse
import string
import sys
import re
class Token :
    def __init__(self, _tipo : str, _valor : int) :
        self.tipo = _tipo
        self.valor = _valor

class Tokenizer :

    posicao = 0
    next = Token("i",0) 

    def __init__(self, _source : str, _posicao : int, _next : Token = None) :
        Tokenizer.source = _source
        self.posicao = _posicao
        self.next = _next

    @staticmethod
    def selectnext():
        numero = ""
        identifier = ""
        tipo = ""

        if Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "+":
            if Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao+1] == "=":
                Tokenizer.posicao += 2
                Tokenizer.next = Token("MAIS IGUAL",0)
                return Tokenizer.next
            Tokenizer.posicao += 1
            Tokenizer.next = Token("MAIS",0)
            return Tokenizer.next

        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "-":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("MENOS",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "(" :
            Tokenizer.posicao += 1
            Tokenizer.next = Token("PARENTESES",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source) and Tokenizer.source[Tokenizer.posicao] == ")":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("FECHA" ,0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "*":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("VEZES",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "/":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("DIVISAO",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "=":
            if Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao+1] == "=":
                Tokenizer.posicao += 2
                Tokenizer.next = Token("COMPARA IGUAL",0)
                return Tokenizer.next
                
            Tokenizer.posicao += 1
            Tokenizer.next = Token("IGUAL",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == ">":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("MAIOR",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "<":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("MENOR",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == ";":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("PONTO E VIRGULA",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "!":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("NOT",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "{":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("ABRE CHAVE",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "}":
            Tokenizer.posicao += 1
            Tokenizer.next = Token("FECHA CHAVE",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == ".":
            Tokenizer.posicao += 1
            #print("to no concatena")
            Tokenizer.next = Token("CONCATENA",0)
            return Tokenizer.next
        
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "&":
            if Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao+1] == "&":
                Tokenizer.posicao += 2
                Tokenizer.next = Token("E",0)
                return Tokenizer.next
            
        elif Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == "|":
            if Tokenizer.posicao < len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao+1] == "|":
                Tokenizer.posicao += 2
                Tokenizer.next = Token("OU",0)
                return Tokenizer.next
        
        elif "\n" in Tokenizer.source:
            if Tokenizer.posicao <= len(Tokenizer.source)-1 and Tokenizer.source[Tokenizer.posicao] == '\n':
                Tokenizer.posicao += 1
                Tokenizer.next = Token("FIM",0)
                #print("deu vommmmmmmmmmmmmmmmm")
                return Tokenizer.next

        
        #print(Tokenizer.source,"dentro")
        # if "\n" in Tokenizer.source:
        #     print(Tokenizer.source.index("\n"),"aq")

        while True:
            def isnumber(x):
                try:
                    int(x)
                    return True
                except ValueError:
                    return False
            
            #print(Tokenizer.posicao,len(Tokenizer.source))
            if Tokenizer.posicao > len(Tokenizer.source)-1:
                tipo = "EOF" 
                numero = 0
                identifier = ""
                Tokenizer.next = Token(tipo,int(numero))
                break
            

            elif isnumber((Tokenizer.source[Tokenizer.posicao])):
                numero += Tokenizer.source[Tokenizer.posicao]
                Tokenizer.posicao += 1
                tipo = "INT"
                if Tokenizer.posicao > len(Tokenizer.source)-1 or not isnumber((Tokenizer.source[Tokenizer.posicao])):
                    Tokenizer.next = Token(tipo,int(numero))
                    break

            
            elif Tokenizer.source[Tokenizer.posicao] == '"':
                Tokenizer.posicao+=1
                while Tokenizer.posicao<len(Tokenizer.source) and (Tokenizer.source[Tokenizer.posicao] != '"'):
                    #print(Tokenizer.source[Tokenizer.posicao],"aqui")
                    identifier+=Tokenizer.source[Tokenizer.posicao]
                    Tokenizer.posicao+=1
                if Tokenizer.source[Tokenizer.posicao] != '"':
                    raise Exception

                Tokenizer.posicao+=1
                #print(identifier,"identifier")
                Tokenizer.next = Token("STRING", identifier)
                break

            elif not isnumber((Tokenizer.source[Tokenizer.posicao])):
                while True:
                    identifier += Tokenizer.source[Tokenizer.posicao]
                    Tokenizer.posicao += 1
                    tipo = "ID"

                    if identifier == "Println":
                        #print("printtttt",identifier)
                        Tokenizer.next = Token("PRINT",identifier)
                        break
                    elif identifier == "if":
                        #print("printtttt")
                        Tokenizer.next = Token("IF",identifier)
                        break

                    elif Tokenizer.next.tipo == "VAR":
                        
                        resultante = Tokenizer.source[Tokenizer.posicao]
                        #print(identifier,"aquiii",resultante)
                        while resultante != "int" and resultante != "str" and resultante not in ["=",")","+","-","*","/","\n","&","|",">","<","{","}",".","i","s"]  :
                            resultante = ''.join(Tokenizer.source[Tokenizer.posicao+1:Tokenizer.posicao+4])
                           # print(resultante)
                            identifier += Tokenizer.source[Tokenizer.posicao]
                            Tokenizer.posicao += 1
                        #print("sai")
                        Tokenizer.next = Token("ID",identifier)
                        break

                    elif identifier == "int":
                        #print("printtttt")
                        Tokenizer.next = Token("INT",identifier)
                        break

                    elif identifier == "string":
                        #print("printtttt")
                        Tokenizer.next = Token("STRING",identifier)
                        break

                    elif identifier == "else":
                        #print("printtttt")
                        Tokenizer.next = Token("ELSE",identifier)
                        break
                    elif identifier == "Scanln":
                        #print("printtttt")
                        Tokenizer.next = Token("SCAN",identifier)
                        break
                    elif identifier == "for":
                        #print("printtttt")
                        Tokenizer.next = Token("FOR",identifier)
                        break
                    
                    elif identifier == "while":
                        #print("printtttt")
                        Tokenizer.next = Token("WHILE",identifier)
                        break

                    elif identifier == "var":
                        #print("printtttt")
                        Tokenizer.next = Token("VAR",identifier)
                        break
                    
                    elif (Tokenizer.source[Tokenizer.posicao]) in ["=",")","+","-","*","/","\n","&","|",">","<","{","}","."] :
                        Tokenizer.next = Token(tipo,identifier)
                        break
                    
                break    

            else:
                break

        #print(Tokenizer.next.tipo)
        return Tokenizer.next
    
class Parser :

    def __init__(self, _tokenizer : Tokenizer) :
        self.tokenizer = _tokenizer

    @staticmethod
    def parseTerm(_token : Token):

        resultado = Parser.parseFactor(_token)
        
        while Tokenizer.next.tipo == "VEZES" or Tokenizer.next.tipo == "DIVISAO":
            
            if Tokenizer.next.tipo == "VEZES":
                resultado = BinOp("VEZES",[resultado,Parser.parseFactor(Parser.tokenizer.selectnext())])

            elif Tokenizer.next.tipo == "DIVISAO":
                saida = Parser.parseFactor(Parser.tokenizer.selectnext())
                if saida == 0:
                    print(int("ola"))
                resultado = BinOp("DIVISAO",[resultado,saida])
            
            
        return resultado

        

    @staticmethod
    def parseExpression(_token : Token):
        #print(Tokenizer.next.tipo,Tokenizer.next.valor)
        resultado = Parser.parseTerm(_token)
        #print(Tokenizer.next.tipo,Tokenizer.next.valor,resultado)

        while Tokenizer.next.tipo == "MAIS" or Tokenizer.next.tipo == "MENOS" or Tokenizer.next.tipo == "CONCATENA":
            #print(Tokenizer.next.tipo,"tipo ")
            if Tokenizer.next.tipo == "MAIS":
                #print("entrei mais")
                resultado = BinOp("MAIS",[resultado,Parser.parseTerm(Parser.tokenizer.selectnext())])
            
            elif Tokenizer.next.tipo == "MENOS":
                resultado = BinOp("MENOS",[resultado,Parser.parseTerm(Parser.tokenizer.selectnext())])

            elif Tokenizer.next.tipo == "CONCATENA":
                #print("concatena",resultado)
                resultado = BinOp("CONCATENA",[resultado,Parser.parseFactor(Parser.tokenizer.selectnext())])


        return resultado

    @staticmethod
    def parseFactor(_token : Token):

        token = _token
        #print(token.tipo,"TIPO DO TOKEN")
        if token.tipo == "MAIS" :
            return UnOp("MAIS",[Parser.parseFactor(Parser.tokenizer.selectnext())])
        
        elif  token.tipo == "MENOS":
            return UnOp("MENOS",[Parser.parseFactor(Parser.tokenizer.selectnext())])
        
        elif  token.tipo == "STRING":
            #print("entrewww",token.valor)
            resultado =  StrVal(token.valor,[])
            token = Parser.tokenizer.selectnext()
            return resultado
        
        elif token.tipo == "NOT":
            return UnOp("NOT",[Parser.parseFactor(Parser.tokenizer.selectnext())])
        
        elif  token.tipo == "ID":
            #print("entrei no ID",Tokenizer.next.valor)
            Parser.tokenizer.selectnext()
            #print("entrei no ID",Tokenizer.next.tipo,token.valor)
            return Identifier(token.valor,[])

        elif token.tipo == "PARENTESES":
            #print("pare")
            resultado = Parser.BoolExpression(Parser.tokenizer.selectnext())
            if Tokenizer.next.tipo == "FECHA":
                token = Parser.tokenizer.selectnext()
            else:
                print(Tokenizer.next.tipo,Tokenizer.next.valor)
                print(int("ola"))
                

            return resultado    
            
        elif token.tipo == "INT":
            #print("tipo",token.tipo,token.valor,"valor")
            resultado = Intval(token.valor,[])
            token = Parser.tokenizer.selectnext()  
            #print(token.tipo,token.valor,"valorrr")

        elif token.tipo == "SCAN":
            if Parser.tokenizer.selectnext().tipo == "PARENTESES":
                # x = input()
                # if x in ["top spin","voleio","slice","flat","venceu"]:
                #     resultado = StrVal(x,[])
                # else:
                # print("toknnnnn",token.tipo)
                #     print(int("ola"))
                resultado = Scan(token.tipo,[])

                #resultado = Intval(int(x),[])
                #print(resultado,"namorallll",Tokenizer.next.tipo)
                if Parser.tokenizer.selectnext().tipo == "FECHA":
                    token = Parser.tokenizer.selectnext()
                    #print("toknnnnn",token.tipo)
                else:
                    print("toknnnnn",token.tipo)
                    print(int("ola"))

        else: 
            print("te peguei")
            print(Tokenizer.next.valor,Tokenizer.next.tipo,Tokenizer.selectnext().tipo,token.tipo)
        
        return resultado
    
    @staticmethod
    def BoolExpression(_token : Token):
        resultado = Parser.BoolTerm(_token)
        #print("TOKEN no BOOL",_token.tipo,_token.valor)
        while Tokenizer.next.tipo == "OU":
            #print("to no ou")
            resultado = BinOp("OU",[resultado,Parser.BoolTerm(Parser.tokenizer.selectnext())])

        return resultado
    
    @staticmethod
    def BoolTerm(_token : Token):
        resultado = Parser.RelExpr(_token)
        while Tokenizer.next.tipo == "E":
            #print("to no E")
            resultado = BinOp("E",[resultado,Parser.RelExpr(Parser.tokenizer.selectnext())])

        return resultado
    

    @staticmethod
    def RelExpr(_token : Token):
        resultado = Parser.parseExpression(_token)
        while Tokenizer.next.tipo in ["COMPARA IGUAL","MAIOR","MENOR"]:
            #print("entreiiii")
            if Tokenizer.next.tipo == "COMPARA IGUAL":
                return BinOp("COMPARA IGUAL",[resultado,Parser.RelExpr(Tokenizer.selectnext())])
            elif Tokenizer.next.tipo == "MAIOR":
                return BinOp("MAIOR",[resultado,Parser.RelExpr(Tokenizer.selectnext())])
            elif Tokenizer.next.tipo == "MENOR":
                return BinOp("MENOR",[resultado,Parser.RelExpr(Tokenizer.selectnext())])
            

            #resultado = BinOp("OU",[resultado,BoolTerm(Parser.tokenizer.selectnext())])
        #print(Tokenizer.next.tipo,"oooooo")
        return resultado

    @staticmethod
    def Block(_token : Token):
        lista = []
        #print(Tokenizer.next.valor,Tokenizer.next.tipo,"blockkkk")
        if _token.tipo == "ABRE CHAVE":
            #print("enteiiii")
            if Tokenizer.selectnext().tipo == "FIM":
                #print("entrei ouu n ???")
                lista.append(Parser.statement(Parser.tokenizer.selectnext()))
                #print(Tokenizer.next.valor,Tokenizer.next.tipo,"block")
                while Tokenizer.next.tipo != "FECHA CHAVE":
                   #print(Tokenizer.next.valor,Tokenizer.next.tipo,"block")
                    lista.append(Parser.statement(Tokenizer.next))
                #Parser.tokenizer.selectnext()
            #Parser.tokenizer.selectnext()
                    
            
        
        return Block(0, lista)

    @staticmethod
    def Program(_token : Token):
        lista = []
        lista.append(Parser.statement(_token))
        #print(Tokenizer.next.valor,Tokenizer.next.tipo)
        while Tokenizer.next.tipo != "EOF":
            #if Parser.tokenizer.selectnext().tipo == "EOF":
            #    break
            #print(Tokenizer.next.valor,Tokenizer.next.tipo,"block")
            lista.append(Parser.statement(Tokenizer.next))
        
        return Block(0, lista)
            
    @staticmethod
    def statement(_token : Token):

        token = _token

        if token.tipo == "FIM" :
           # print("FIM chegou")
            return NoOp("FIM",Parser.tokenizer.selectnext())
        
        elif  token.tipo == "VAR":
            if Parser.tokenizer.selectnext().tipo == "ID":
               # print(Tokenizer.next.valor,Tokenizer.next.tipo)
                id = Tokenizer.next.valor
                Parser.tokenizer.selectnext()
                #print(Tokenizer.next.valor,Tokenizer.next.tipo,"antes do if")
                if Tokenizer.next.tipo == "INT" or Tokenizer.next.tipo == "STRING":
                    tipo = Tokenizer.next.tipo
                    #print(Tokenizer.next.valor,Tokenizer.next.tipo,"depois do if")
                    if Parser.tokenizer.selectnext().tipo=="IGUAL":
                        return VarDec(id,[Parser.BoolExpression(Parser.tokenizer.selectnext()),Tipo(tipo,[])])
                    else:
                        #print(id,Tokenizer.next.valor,Tokenizer.next.tipo,"embaixo")
                        return VarDec(id,[Tipo(tipo,[]),Tipo(tipo,[])])

            else:
                raise SyntaxError    
            
        elif  token.tipo == "ID":
            #print(token.valor,token.tipo,"stat")
            analise = Parser.tokenizer.selectnext()
            #print(analise,analise.tipo,analise.valor)
            if analise.tipo == "IGUAL":
                #print(Tokenizer.next.valor,Tokenizer.next.tipo)
                resultado = Assign("IGUAL",[Identifier(token.valor,[]), Parser.BoolExpression(Parser.tokenizer.selectnext())])
                #print(Tokenizer.next.tipo,"tipoooo")
                if Tokenizer.next.tipo == "FIM":
                    #Parser.tokenizer.selectnext()
                    return resultado
                elif Tokenizer.next.tipo == 'EOF':
                    #print("eofffe")
                    return resultado
                else:
                    print(Tokenizer.next.tipo,"tipo",Tokenizer.next.valor)
                    raise SyntaxError("ERRADO")
                
            elif analise.tipo == "MAIS IGUAL":
                #print(Tokenizer.next.valor,Tokenizer.next.tipo,token.valor)
                resultado = Assign("IGUAL",[Identifier(token.valor,[]), BinOp("MAIS",[Parser.BoolExpression(token),Parser.BoolExpression(Tokenizer.next)])])
                #print(Tokenizer.next.tipo,"tipoooo")
                if Tokenizer.next.tipo == "FIM":
                    #Parser.tokenizer.selectnext()
                    return resultado
                elif Tokenizer.next.tipo == 'EOF':
                    #print("eofffe")
                    return resultado
                else:
                    print(Tokenizer.next.tipo,"tipo",Tokenizer.next.valor)
                    raise SyntaxError("ERRADO")

                    
            else:
                #print(Tokenizer.next.tipo)
                print(int("ola"))

        elif token.tipo == "PRINT":
            token = Parser.tokenizer.selectnext()
            #print(token.tipo,token.valor,"dentro do print")
            if token.tipo == "PARENTESES":
                resultado = Parser.BoolExpression(Parser.tokenizer.selectnext())
                #print(resultado,"namorallll",Tokenizer.next.tipo)
                if Tokenizer.next.tipo == "FECHA":
                    token = Parser.tokenizer.selectnext()
                    #print("toknnnnn",token.tipo)
                else:
                    print("toknnnnn",token.tipo)
                    print(int("ola"))

                return Print(0,[resultado])    
            
            else: 
                print(int("te peguei"))    
        
        elif token.tipo == "IF":
            #print("entrei no if ")
            #print(Tokenizer.next.tipo)
            condicao = Parser.BoolExpression(Parser.tokenizer.selectnext())
            #print(Tokenizer.next.tipo,"saida condiçao")
            bloco1 = Parser.Block(Tokenizer.next)
            bloco2 = NoOp("ELSE",[])
            if Parser.tokenizer.selectnext().tipo == "ELSE":
                #print("entrei else",Tokenizer.next.tipo)
                bloco2 = Parser.Block(Parser.tokenizer.selectnext())
                Parser.tokenizer.selectnext()
            elif Tokenizer.next.tipo == "FIM":
                Parser.tokenizer.selectnext()
            else:
                print(Tokenizer.next.valor,Tokenizer.next.tipo)
                raise SyntaxError("Erro no else")

            return If("If",[condicao,bloco1,bloco2])
        
        elif token.tipo == "WHILE":   
            #print(Tokenizer.next.tipo,"1")
            condicao = Parser.BoolExpression(Parser.tokenizer.selectnext()) 
            #print(Tokenizer.next.tipo,"2")
            conteudo = Parser.Block(Tokenizer.next)
            #print(Tokenizer.next.tipo,"3")
            if(Tokenizer.next.tipo == "FECHA CHAVE"):
                Parser.tokenizer.selectnext()

            return While("WHILE",[condicao,conteudo])


            
        
        elif token.tipo == "FOR":
            token = Parser.tokenizer.selectnext()
            if token.tipo == "ID":
            #print(token.valor,token.tipo,"stat")
                if Parser.tokenizer.selectnext().tipo == "IGUAL":
                    #print(Tokenizer.next.valor,Tokenizer.next.tipo)
                    init = Assign("IGUAL",[Identifier(token.valor,[]), Parser.BoolExpression(Parser.tokenizer.selectnext())])
                    #print(Tokenizer.next.tipo,"tipoooo")
                        
                else:
                    #print(Tokenizer.next.tipo)
                    print(int("ola"))

                if Tokenizer.next.tipo == "PONTO E VIRGULA":
                    condicao = Parser.BoolExpression(Parser.tokenizer.selectnext())
                    if Tokenizer.next.tipo == "PONTO E VIRGULA":
                        token = Parser.tokenizer.selectnext()
                        if token.tipo == "ID":
                        #print(token.valor,token.tipo,"stat")
                            if Parser.tokenizer.selectnext().tipo == "IGUAL":
                                #print(Tokenizer.next.valor,Tokenizer.next.tipo)
                                inc = Assign("IGUAL",[Identifier(token.valor,[]), Parser.BoolExpression(Parser.tokenizer.selectnext())])
                                conteudo = Parser.Block(Tokenizer.next)
                                Parser.tokenizer.selectnext()
                        

            return For("For",[init,condicao,inc,conteudo])    
        
        
        else: 
            print("te peguei aquiiii",Tokenizer.next.tipo,Tokenizer.next.valor)
            print(int("oa"))
        

        

    
    @staticmethod
    def run(code : str ):
        def tratamento(x):
            i = 0
            lista = []
            pattern = r'\d\s+\d'  
            if  re.findall(pattern, x):
                return print(int("ola"))
            while i < len(x):
                numeros = re.split(r'([+-])', x[i])
                #print(numeros,"numeri")
                lista = lista + numeros
                i += 1    
            numeros_sem_espacos = list(filter(lambda x: x.strip() != "" or x == "\n", lista))
            return numeros_sem_espacos
        
        Parser.tokenizer = Tokenizer(tratamento(PrePro.filter6(code)), 0)
        #print("llelle",PrePro.filter6(code),"filter2")
        #print(tratamento(PrePro.filter6(code)))
        #print("source",Parser.tokenizer.source)
        next = Parser.tokenizer.selectnext()
        resp = Parser.Program(next)
        if Tokenizer.next.tipo == 'EOF':
            return resp
        else:
            print(int("ola"))

        
class Node:

    def __init__(self, _value, _lista) :
        self.value = _value
        self.children = _lista
    def Evaluate():
        pass


class SymbolTable:
    dic = {}

    def getter(self,nome):
        if not (nome in SymbolTable.dic.keys()):
            print(int("ola"))
        #print(self.dic[nome])
        return self.dic[nome]
    
    def setter(self,nome,valor,tipo):
        self.dic[nome] = (valor,tipo)
        pass

class VarDec(Node):

    def Evaluate(self, simbolo : SymbolTable):
        #print(self.children[0].Evaluate(simbolo)[1],"vardec")
        if self.value in SymbolTable.dic.keys():
            print(int("já existe"))

        if len(self.children) == 1:
            #print("deu bom1")
            SymbolTable.setter(self.value, None,self.children[0],0)
        
        else:   
            #print(self.value,self.children[0].Evaluate(simbolo)[0],self.children[1].Evaluate(simbolo)[0]) 
            if self.children[0].Evaluate(simbolo)[1] == self.children[1].Evaluate(simbolo)[0]:
                #print("deu bom2")
                simbolo.setter(self.value, self.children[0].Evaluate(simbolo)[0],self.children[1].Evaluate(simbolo)[0])
        # else:
        #     raise Exception("errei na logica")


class Assign(Node):
    
    def Evaluate(self,simbolo : SymbolTable):
        # print(self.value,"evaluate")
        #print(self.children[1].Evaluate(simbolo)[1],"resul",self.children[0].Evaluate(simbolo)[1])
        eval0 = self.children[0].Evaluate(simbolo)[1]
        eval1 = self.children[1].Evaluate(simbolo)
        if eval1[1] != eval0:
            raise Exception
        simbolo.setter(self.children[0].value, eval1[0],eval1[1])

class Identifier(Node):

    def Evaluate(self,simbolo : SymbolTable):
        # print("abarro")
        return simbolo.getter(self.value)
    
class Print(Node):

    def Evaluate(self,simbolo : SymbolTable):
        print(self.children[0].Evaluate(simbolo)[0])
        return self.children[0].Evaluate(simbolo)[0]
    
class Scan(Node):

    def Evaluate(self,simbolo : SymbolTable):
        # print("TK NO SCANNNNN")
        x = input()
        if x in ["top spin","voleio","slice","flat","venceu"]:
            return (x,"STRING")
        else:
            raise Exception

        # return self.children[0].Evaluate(simbolo)[0]
    
class Block(Node):
    def Evaluate(self, simbolo : SymbolTable):
        for filho in self.children:
            filho.Evaluate(simbolo)

class If(Node):
    def Evaluate(self, simbolo : SymbolTable):
        #print(self.children,self.children[0].Evaluate(simbolo))
        if self.children[0].Evaluate(simbolo)[0]:
            return self.children[1].Evaluate(simbolo)

        else:
            return self.children[2].Evaluate(simbolo)
        
class For(Node):
    def Evaluate(self, simbolo : SymbolTable):
        self.children[0].Evaluate(simbolo)
        while self.children[1].Evaluate(simbolo)[0]:
            self.children[3].Evaluate(simbolo)
            self.children[2].Evaluate(simbolo)      

class While(Node):
    def Evaluate(self, simbolo : SymbolTable):
        #print(self.children[0].Evaluate(simbolo)[0],"cond while")
        while self.children[0].Evaluate(simbolo)[0]:
            #print(self.children[0].Evaluate(simbolo)[0],"cond while")
            self.children[1].Evaluate(simbolo)

class BinOp(Node):
    
    def Evaluate(self,simbolo : SymbolTable):
        resultado1 = self.children[0].Evaluate(simbolo)
        resultado2 = self.children[1].Evaluate(simbolo)

        resultado1_tipo =  resultado1[1]
        resultado2_tipo =  resultado2[1]
        
        if self.value == "MAIS" and (resultado1_tipo == "INT" and resultado2_tipo == "INT"):
            return (self.children[0].Evaluate(simbolo)[0] + self.children[1].Evaluate(simbolo)[0],resultado2_tipo) 
        
        elif self.value == "MENOS" and (resultado1_tipo == "INT" and resultado2_tipo == "INT"):
            return (self.children[0].Evaluate(simbolo)[0] - self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "VEZES" and (resultado1_tipo == "INT" and resultado2_tipo == "INT"):
            return (self.children[0].Evaluate(simbolo)[0] * self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "DIVISAO" and (resultado1_tipo == "INT" and resultado2_tipo == "INT"):
            return (self.children[0].Evaluate(simbolo)[0] // self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "MAIOR" and (resultado1_tipo == resultado2_tipo):
            if (self.children[0].Evaluate(simbolo)[0] > self.children[1].Evaluate(simbolo)[0]):
                return (1,resultado2_tipo)
            else:
                return (0,resultado2_tipo)
            #return (self.children[0].Evaluate(simbolo)[0] > self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "MENOR" and (resultado1_tipo == resultado2_tipo):
            if(self.children[0].Evaluate(simbolo)[0] < self.children[1].Evaluate(simbolo)[0]):
                return (1,resultado2_tipo)
            else:
                return (0,resultado2_tipo)
            #return (self.children[0].Evaluate(simbolo)[0] < self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "E" and (resultado1_tipo == "INT" and resultado2_tipo == "INT"):
            if (self.children[0].Evaluate(simbolo)[0] and self.children[1].Evaluate(simbolo)[0]):
                return (1,resultado2_tipo)
            else:
                return (0,resultado2_tipo)
            return (self.children[0].Evaluate(simbolo)[0] and self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "OU" and (resultado1_tipo == "INT" and resultado2_tipo == "INT"):
            if (self.children[0].Evaluate(simbolo)[0] or self.children[1].Evaluate(simbolo)[0]):
                return (1,resultado2_tipo)
            else:
                return (0,resultado2_tipo)
            return (self.children[0].Evaluate(simbolo)[0] or self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "COMPARA IGUAL" and (resultado1_tipo == resultado2_tipo) :
            if(self.children[0].Evaluate(simbolo)[0] == self.children[1].Evaluate(simbolo)[0]):
                return (1,resultado2_tipo)
            else:
                return (0,resultado2_tipo)
            return (self.children[0].Evaluate(simbolo)[0] == self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        elif self.value == "CONCATENA":
            if resultado1_tipo != "STRING" or resultado2_tipo != "STRING":
                #print(self.children[0].Evaluate(simbolo)[0],"teste")
                return (str(self.children[0].Evaluate(simbolo)[0]) + str(self.children[1].Evaluate(simbolo)[0]),"STRING")
            return (self.children[0].Evaluate(simbolo)[0] + self.children[1].Evaluate(simbolo)[0],resultado2_tipo)
        
        
        else:
            raise Exception
        
class UnOp(Node): 

    def Evaluate(self,simbolo : SymbolTable):
        if self.value == "MAIS":
            return (self.children[0].Evaluate(simbolo)[0],"INT")  
            
        elif self.value == "MENOS":
            return (- self.children[0].Evaluate(simbolo)[0],"INT")
        
        elif self.value == "NOT":
            return  (not self.children[0].Evaluate(simbolo)[0],"INT")
        
class Intval(Node): 

    def Evaluate(self, simbolo : SymbolTable):

        return (self.value,"INT")
    
class StrVal(Node):

    def Evaluate(self, simbolo : SymbolTable):
        return (self.value,"STRING")
    
class Tipo(Node): 

    def Evaluate(self, simbolo : SymbolTable):

        return (self.value,self.value)    

class NoOp(Node): 

    def Evaluate(self,simbolo : SymbolTable):
        
        pass




class PrePro:


    def filter6(codigo):
        with open(codigo, 'r') as arquivo_in:
            texto =arquivo_in.read()
            # Remove comentários de várias linhas (/* ... */)
            codigo = re.sub(r'/\*.*?\*/', '', texto, flags=re.DOTALL)

            # Remove comentários de linha única (// ...)
            codigo = re.sub(r'//.*', '', texto)

        return codigo

    def filter(arquivo_entrada):
        codigo_sem_comentarios = ""
        dentro_de_comentario_multilinha = False

        with open(arquivo_entrada, 'r') as arquivo_in:
            linhas = arquivo_in.readlines()
            for linha in linhas:
                linha = linha.strip()

                # Verificar se estamos dentro de um comentário de várias linhas
                if dentro_de_comentario_multilinha:
                    if '*/' in linha:
                        dentro_de_comentario_multilinha = False
                    continue
                elif '/*' in linha:
                    dentro_de_comentario_multilinha = True
                    if '*/' in linha:
                        linha = linha.split('*/', 1)[1]
                    else:
                        continue

                # Remover comentários de linha única
                if '//' in linha:
                    linha = linha.split('//', 1)[0]

                codigo_sem_comentarios += linha + '\n'

        return codigo_sem_comentarios


if __name__ == "__main__":

    raiz = Parser.run(sys.argv[1])
    raiz.Evaluate(SymbolTable())
    


