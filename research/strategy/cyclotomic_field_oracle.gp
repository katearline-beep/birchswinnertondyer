\\ Independent PARI/GP field-theoretic check (no Kato element computed).
\\ Unique real cyclic degree 11 subfield of cyclotomic conductor 121.
F=polsubcyclo(121,11);
if(poldegree(F)!=11,error("wrong degree for first Z11 cyclotomic layer"));
if(nfdisc(F)!=11^20,error(Str("wrong field discriminant ",nfdisc(F))));
if(polsturm(F)!=11,error("first cyclotomic layer is not totally real"));
G=polsubcyclo(23,11);
if(poldegree(G)!=11,error("wrong degree for previous real period field"));
if(nfdisc(G)!=23^10,error(Str("wrong prior field discriminant ",nfdisc(G))));
print(Str("PASS PARI C11: first cyclotomic Z11 layer has degree 11 and disc ",nfdisc(F)));
print(Str("PASS PARI C11: previous Q(zeta23)^+ has disc ",nfdisc(G)));
print("PASS PARI C11: field discriminants differ despite identical abstract Gal groups");
quit;
