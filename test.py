import spi

text = \
'''
PROGRAM Part12;
VAR
   a : INTEGER;

PROCEDURE P1;
VAR
   a : REAL;
   k : INTEGER;

   PROCEDURE P2;
   VAR
      a, z : INTEGER;
   BEGIN {P2}
      z := 777;
   END;  {P2}

BEGIN {P1}

END;  {P1}

BEGIN {Part12}
   a := 10;
END.  {Part12}
'''

lexer = spi.Lexer(text)
parser = spi.Parser(lexer)
tree = parser.parse()
symtab_builder = spi.SymbolTableBuilder()
symtab_builder.visit(tree)
print(symtab_builder.symtab)

interpreter = spi.Interpreter(tree)
result = interpreter.interpret()
print(interpreter.GLOBAL_MEMORY )