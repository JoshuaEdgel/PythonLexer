import re
#Joshua Edgel
#11/1/2021
search_file = 'Input.txt'
output = open('Output.txt', "a")

#lex = re.compile("((?:\\\1)|(?:[0-9]+\2)|(?:=\3)|(?:int\4)|(?:string\5)|(?:\.\6)|(?:\"[a-zA-Z0-9\s]*\"\7)|(?:Print\8)|(?:[a-zA-z]+[a-zA-z0-9]*\9))")

with open(search_file, 'r') as sf:
    #the long regular expression of the language
    reg_ex = re.compile("((?:\/[a-zA-Z0-9\s]*)|(?:[0-9]+)|(?:=)|(?:int)|(?:string)|(?:\.)|(?:\"[a-zA-Z0-9\s]*\")|(?:Print)|(?:[a-zA-z]+[a-zA-z0-9]*)|(?:[\+\-\*\%]))")
    #individual parts of the language
    comment = '(?:\/[a-zA-Z\s0-9]*)'
    intt = '(?:int)'
    Print = '(?:Print)'
    string = '(?:string)'
    ident = '(?:[a-zA-z]+[a-zA-z0-9]*)'
    equals = '(?:=)'
    intval = '(?:[0-9]+)'
    sstring = '(?:\"[a-zA-Z0-9\s]*\")'
    period = '(?:\.)'
    oper = '(?:[\+\-\*\%])'

    for line in sf:
        m = re.findall(reg_ex, line)
        #grabs the lines that have something written in the code in them
        if m:
            #jankily searches the line for the specific type of value's in it
            for item in m:
                if re.match(comment, item):
                    #For some reason if my lexer allows for the comments to have spaces. It prints the results on two lines. 
                    output.write("Value : "+item+" , Type: Keyword , Description: Produces a comment\n")
                elif re.match(intt, item):
                    output.write("Value : "+item+" , Type: Keyword , Description: Defining a Integer\n")
                elif re.match(Print, item):
                    output.write("Value : "+item+" , Type: Keyword , Description: Printing in the console\n")
                elif re.match(string, item):
                    output.write("Value : "+item+" , Type: Keyword , Description: Defining a String\n")
                elif re.match(ident, item):
                    output.write("Value : "+item+" , Type: ID\n")
                elif re.match(equals, item):
                    output.write("Value : "+item+" , Type: Assignemnt\n") 
                elif re.match(intval, item):
                    output.write("Value : "+item+" , Type : Integer\n") 
                elif re.match(sstring, item):
                    output.write("Value : "+item+" , Type: String\n") 
                elif re.match(period, item):
                    output.write("Value : "+item+" , Type: EndOfStatement\n") 
                elif re.match(oper, item):
                    output.write("Value : "+item+" , Type: Operator\n") 
output.close()