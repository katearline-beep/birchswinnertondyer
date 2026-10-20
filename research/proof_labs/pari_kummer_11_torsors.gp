\\ Independent maintained-library multiplication and division polynomials.
print_coefficients(tag,p)={print1(tag," ");for(i=0,poldegree(p),if(i,print1(","));print1(polcoef(p,i)));print();};
e=ellinit([0,0,0,-1267,17230]);
v=ellxn(e,11);ps11=elldivpol(e,11);
print_coefficients("PHI",v[1]);
print_coefficients("PSI",ps11);
print_coefficients("DEN",v[2]);
quit;
