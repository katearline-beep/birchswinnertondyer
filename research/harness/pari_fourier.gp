\\ Completely independent PARI ellan oracle for E / Q
\\ Minimal model E: y^2+xy=x^3-x^2-79x+289.
E=ellinit([1,-1,0,-79,289]);
a=ellan(E,2000);
for(n=1,2000,print(a[n]));
quit;
