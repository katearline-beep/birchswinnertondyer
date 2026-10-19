\p 30
\\ Independent canonical sigma coefficient via PARI/GP's unit-Frobenius slope,
\\ *not* the AI-authored rational formal-series recurrence.
\\ PARI manual: ellpadics2 is the unique c such that canonical sigma is integral,
\\ and c = b2/12 - E2/12. Same minimal invariant differential as MST.
E = ellinit([1,-1,0,-79,289]);
s11 = ellpadics2(E,11,5);
v11 = lift(Mod(lift(s11),11^2));
if(v11 != 26, error(Str("PARI C-0013 c11 mismatch: ",v11)));
print("PASS PARI canonical sigma C-0013: c11 = 26 modulo 121");
\\ Independent published MST conductor-37/p=5 second-digit control.
E37 = ellinit([0,0,1,-1,0]);
s5 = ellpadics2(E37,5,4);
v5 = lift(Mod(lift(s5),5^2));
if(v5 != 6, error(Str("PARI published E37 c5 mismatch: ",v5)));
print("PASS PARI MST E37 canonical sigma: c5 = 6 modulo 25");
\\ p-adic Eisenstein E2 = b2-12c; b2=-3 on the target minimal model.
if(lift(Mod(-3 - 12*v11,121)) != 48, error("PARI E2 congruence mismatch"));
print("PASS PARI E2 = 48 modulo 121; no K-global height or BSD implication");
quit;
