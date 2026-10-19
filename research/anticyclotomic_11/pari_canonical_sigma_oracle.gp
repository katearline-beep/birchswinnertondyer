\p 30
\\ Independent sigma-parameter oracle through PARI's ellpadics2.
\\ IMPORTANT: symbolic series u=E2/12, while PARI returns
\\ s2=b2/12-E2/12. Thus u=b2/12-s2; they are NOT the same parameter.
E = ellinit([1,-1,0,-79,289]);
s11 = ellpadics2(E,11,5);
v11 = lift(Mod(lift(s11),11^2));
if(v11 != 4, error(Str("PARI target s2 mismatch: ",v11)));
E211 = lift(Mod(-3-12*v11,121));
if(E211 != 70, error(Str("PARI target E2 mismatch: ",E211)));
u11 = lift(Mod(E211,121)/Mod(12,121));
if(u11 != 26, error(Str("PARI target symbolic sigma u mismatch: ",u11)));
print("PASS PARI C-0013 s2=4 E2=70 u=26 modulo 121");
\\ Published MST E37/p5 example has b2=0 and u=6, hence s2=-u=19.
E37 = ellinit([0,0,1,-1,0]);
s5 = ellpadics2(E37,5,4);
v5 = lift(Mod(lift(s5),25));
if(v5 != 19, error(Str("PARI E37 s2 mismatch: ",v5)));
u5 = lift(-Mod(v5,25));
if(u5 != 6, error(Str("PARI E37 sigma u mismatch: ",u5)));
print("PASS PARI E37 p5 s2=19 u=6 modulo 25");
print("NONCLAIM: independent sigma/E2 confirmation only; no independent global height or BSD proof");
quit;
