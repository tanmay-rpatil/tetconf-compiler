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
 because the syntax `{"L",#106b77}, {"I",#106b77}` will give errors as it will try to greedyly


IP

```
opening_msg = "this has double ", but gives rr ";
closing_msg = "!@#$%^&*(QWERTYUIOPASDFGHJKLZXCVBNM)'/<>" 
```

OP

```
opening msg is not set, as string does not include quotes
```

The Following are invalid tokens

```
"invalid_token 
```

# Testing assignments

IP

```
rotate = "K_UP"; 

rotate = 0; //should tokenize, but later phase may report errors

scoring = [0, 40];

pieces = [{"L",#FFFFFF}, {"I",#111111}];
```

OP

```
<ROTATE><RELOP,EQ><STRING,"K_UP"><EOS>

<ROTATE><RELOP,EQ><NUMBER,0><EOS><COMMENT>

<SCORING><RELOP,EQ><OPEN_SQUARE><NUMBER,0><COMMA><NUMBER,0><COMMA><CLOSE_SQUARE><EOS>

<PCS><RELOP,EQ> <OPEN_SQUARE> <OPEN_CURLY><STRING,"L"><COMMA><COLOR,#FFFFFF><NUMBER,0><CLOSE_CURLY><COMMA> <OPEN_CURLY><STRING,"I"><COMMA><COLOR,#111111><CLOSE_CURLY>  <CLOSE_SQUARE> <EOS>
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