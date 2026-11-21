\\ Independent PARI ray-class and minimal Weierstrass arithmetic.
\\ No global supported Galois correction or BSD theorem is claimed.
check(c,s)={if(!c,error(s));};
{
  bnf=bnfinit(y^2-y+2,1);
  check(bnfcertify(bnf)==1 && bnf.no==1,"uncertified K");
  ray=bnrinit(bnf,121,1);
  check(ray.cyc==[110,55],"unexpected ray class group");
  subgroup=mathnf(concat(11*matid(2),bnrisprincipal(ray,2,0)));
  check(subgroup==[11,0;0,1],"wrong anticyclotomic quotient");
  ratio=Mod(16,121)/Mod(-15,121);
  ellomega=lift(znlog(ratio^10,Mod(12,121)));
  scale=Mod(ellomega,11)/Mod(bnrisprincipal(ray,y,0)[1],11);
  data=[[743,27,-14,109],[127,-11,6,45]];
  for(i=1,2,
    q=data[i][1]; a=data[i][2]; b=data[i][3]; root=data[i][4];
    check(a^2+a*b+2*b^2==q && (root^2+7)%q==0,"bad split ideal");
    check(lift(Mod(a+b*(1+root)/2,q))==0,"wrong local prime orientation");
    ee=ellinit([1,-1,0,-79,289],q);
    n=ellcard(ee); tr=q+1-n;
    aa=Mod([0,-q;1,tr],11); order=1; bb=aa;
    while(bb!=matid(2),bb=bb*aa;order++;check(order<=132,"order bound"));
    ell=lift(scale*bnrisprincipal(ray,a+b*y,0)[1]);
    if(q==743,
      check(n==770 && tr==-26 && order==10 && ell==0,"wrong q743");
      print("FROBENIUS743 ",q," ",a," ",b," ",root," ",n," ",tr," ",order," ",ell," ",lift(Mod(order*ell,11)));
    ,
      check(n==143 && tr==-15 && order==10 && ell==4,"wrong q127");
      print("FROBENIUS127 ",q," ",a," ",b," ",root," ",n," ",tr," ",order," ",ell," ",lift(Mod(order*ell,11)));
    );
  );
  q=743; ee=ellinit([1,-1,0,-79,289],q);
  p1=[Mod(4,q),Mod(3,q)];p2=[Mod(5,q),Mod(-2,q)];
  xx=ellsub(ee,p2,ellmul(ee,p1,2));
  tt=ellmul(ee,p1,70);ww=ellmul(ee,xx,70);
  check(#tt==2 && #ww==2 && ellmul(ee,tt,11)==[0],"bad q743 11 torsion");
  check(ellmul(ee,p2,70)==[0] && ww==ellmul(ee,tt,9),"wrong q743 Kummer");
  print("KUMMER743 ",lift(4*tt[1]-1)," ",lift(8*tt[2]+4*tt[1])," ",lift(4*ww[1]-1)," ",lift(8*ww[2]+4*ww[1])," 9");
}
quit;
