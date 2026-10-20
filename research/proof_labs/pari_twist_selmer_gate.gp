\\ Exact local prerequisites and SMALL-CURVE modular-symbol twisting control.
\\ Deliberately does not initialize modular symbols at focal conductor234446.
E0=ellinit([1,-1,0,-79,289]); Et=ellminimalmodel(elltwist(E0,-7));
if(Et[1..5]!=[1,-1,0,-3880,-91372],error("minimal twist"));
G=ellglobalred(Et);if(G[1]!=11487854 || G[3]!=2,error("conductor/Tamagawa"));
if(vector(3,i,elllocalred(Et,[2,7,117223][i])[4])!=[2,1,1],error("local Tam"));
print("TWISTINPUT ",G[1]," ",G[3]," ",ellcard(ellinit(Et,11))," ",ellcard(ellinit(Et,3389)));
E=ellinit([0,0,1,-1,0]); T=ellminimalmodel(elltwist(E,-7));
[M,s]=msfromell(E,-1);[Mt,st]=msfromell(T,1);[Mp,sp]=msfromell(E,1);
for(a=1,6,v=sum(b=1,6,kronecker(-7,b)*mseval(M,s,[oo,a/13+b/7]));w=mseval(Mt,st,[oo,a/13]);bad=sum(b=1,6,kronecker(-7,b)*mseval(Mp,sp,[oo,a/13+b/7]));if(v!=w || v==bad,error("symbol twisting/sign control"));print("TWISTCONTROL ",a," ",v," ",w," ",bad));
print("PASS PARI Session34 exact small-curve symbol control");
