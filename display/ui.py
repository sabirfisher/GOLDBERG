import sys
import os
import os
print(os.path.dirname(__file__)) # Directory of current working directory, not __file__   # Append the correct path

from display.print import displayText

def GOLDBERG():
    gbUI = """
                                         ;                                                              
                :                        ED.                                                            
               t#,                       E#Wi                               ,;                          
      .Gt     ;##W.                i     E###G.        .                  f#i   j.                   .Gt
     j#W:    :#L:WE               LE     E#fD#W;       Ef.              .E#t    EW,                 j#W:
   ;K#f     .KG  ,#D             L#E     E#t t##L      E#Wi            i#W,     E##j              ;K#f  
 .G#D.      EE    ;#f           G#W.     E#t  .E#K,    E#K#D:         L#D.      E###D.          .G#D.   
j#K;       f#.     t#i         D#K.      E#t    j##f   E#t,E#f.     :K#Wfff;    E#jG#W;        j#K;     
,K#f   ,GD;  :#G     GK         E#K.       E#t    :E#K:  E#WEE##Wt    i##WLLLLt   E#t t##f     ,K#f   ,GD;
 j#Wi   E#t   ;#L   LW.       .E#E.        E#t   t##L    E##Ei;;;;.    .E#L       E#t  :K#E:    j#Wi   E#t
  .G#D: E#t    t#f f#:       .K#E          E#t .D#W;     E#DWWt          f#E:     E#KDDDD###i    .G#D: E#t
    ,K#fK#t     f#D#;       .K#D           E#tiW#G.      E#t f#K;         ,WW;    E#f,t#Wi,,,      ,K#fK#t
      j###t      G#t       .W#G            E#K##i        E#Dfff##E,        .D#;   E#t  ;#W:          j###t
       .G#t       t       :W##########Wt   E##D.         jLLLLLLLLL;         tt   DWi   ,KK:          .G#t
         ;;               :,,,,,,,,,,,,,.  E#t                                                          ;;
                                           L:                                                             
    """
    displayText(gbUI, speed=0.01)  # Speed is faster, adjust this value as desired.

if __name__ == "__main__":
    GOLDBERG()
