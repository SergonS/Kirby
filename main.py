from Sly.lexer import KLexer
from Sly.parser import KParser
from VM.VirtualMachine import VirtualMachine

if __name__ == '__main__':
        K_lexer = KLexer()
        K_parser = KParser()

        # To read from file
        f_name = "fibonacci.txt"
        file = open(f_name, 'r') 
        f = file.read()

        res = K_parser.parse(K_lexer.tokenize(f))
        K_parser.quads.printQuads()
        print("Console output:")
        vm = VirtualMachine(K_parser.parseData(), K_parser.quads.counter_temps)


        
