\\ Numeric diagnostics ONLY: no exact zero or BSD claim.
\\ Original rank-four curve and independent rank-two control 389a1.
E=ellinit([1,-1,0,-79,289]);
C=ellinit([0,1,1,-2,0]);
default(realprecision,40);
z2=ellL1(E,2);
z4=ellL1(E,4);
c2=ellL1(C,2);
if(abs(c2)<1,error(Str("rank-2 control curvature unexpected ",c2)));
print(Str("PASS rank-two control ellL1(C,2)=",c2));
print(Str("NUMERIC E234446_L2_40digits=",z2));
print(Str("NUMERIC E234446_L4_40digits=",z4));
default(realprecision,90);
v2=ellL1(E,2);
v4=ellL1(E,4);
print(Str("NUMERIC E234446_L2_90digits=",v2));
print(Str("NUMERIC E234446_L4_90digits=",v4));
print("PASS central derivative exploratory diagnostics computed; no mathematical zero inferred");
quit;
