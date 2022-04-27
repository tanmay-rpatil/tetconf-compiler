# Comments tests
To test if comments interfere w

IP

```
sound = ON; //enables music
//speed = 1;
```

OP

```
music is enabled
but speed is unaffected
```

# Testing strings

Strings end as soon as a closing double quote is encountered.

By default, python regex match greedily, i.e. it will match till the last double quote found
 because the syntax `{"L",#106b77}, {"I",#106b77}` will give errors as it will try to greedily

IP

```
opening_msg = "this has double ", but gives error ";
closing_msg = "!@#$%^&*(QWERTYUIOPASDFGHJKLZXCVBNM)'/<>" 
pieces = [{"L",#106b77}, {"I",#106b77}];
```

OP

```
opening msg is not set, as string does not include quotes
closing msg is set
pieces L and I are set successfuly to the given colors
```

# Testing arrays

Arrays present a challenge to the parser, as there are these variations possible:

IP

```
board = []; //set to defaults, empty array
scoring = [0, 40]; //scoring upto 2 levels is set, above which defaults are taken 
pieces = [{"L",#FFFFFF}, {"I",#111111}]; //L and I pieces are allowed and colored
pieces = []; //default pieces
scoring = [1,"a"] 
```

OP

```
- Board dims are set to defaults
- scoring upto 2 levels is set, above which defaults are taken
- L and I pieces are allowed and colored
- Default pieces are set
- Scoring is not set. Only integers are allowed 
```

# Misc Tests

IP

```
[{"L",#ffffff}];
ghost = on;
```

OP

```
<OPEN_SQUARE> <OPEN_CURLY><STRING,"L"><COMMA><COLOR,#FFFFFF><NUMBER,0><CLOSE_CURLY> <CLOSE_SQUARE> <EOS>

<GHOST><RELOP,EQ><BOOL,1><EOS>
```