import os,json,urllib.request as UQ,random
E=os.environ["MAKEFUN_ENV_URL"]
def P(p,d):
 r=UQ.Request(E+p,data=json.dumps(d).encode(),headers={"Content-Type":"application/json"})
 return json.loads(UQ.urlopen(r).read())
B=[0]*128;TM=1;CR=0;EP=-1;HS=0;SCM=0;SCE=0;PHU=0;ND=0;AB=0;NB=95000;GH=[]
TT={};KL={};ST=[];HP=[];K={};CB={1:0,-1:0};NP={1:0,-1:0}
PC={1:[0]*8,-1:[0]*8};RK={};HH={1:{},-1:{}}
RG=random.Random(987123)
ZP={(p,s):RG.getrandbits(64) for p in range(-6,7) if p for s in range(128)}
ZS=RG.getrandbits(64);ZC=[RG.getrandbits(64) for _ in range(16)];ZE=[RG.getrandbits(64) for _ in range(8)]
V={1:100,2:320,3:330,4:500,5:950,6:0};PW={2:1,3:1,4:2,5:4}
D8=[16,-16,1,-1,17,15,-17,-15];DN=[33,31,18,14,-14,-18,-31,-33];MATE=100000;INF=10**9
def _tables():
 ADV_M=[0,0,6,14,26,44,70,0];ADV_E=[0,0,10,22,40,64,100,0];FIL=[-4,-2,2,6,6,2,-2,-4]
 KGF=[18,24,6,-14,-14,6,24,18]
 PM={a:[0]*128 for a in range(7)};PE={a:[0]*128 for a in range(7)}
 for s in range(128):
  if s&0x88:continue
  f=s&7;r=s>>4;c=min(f,7-f)+min(r,7-r)
  PM[1][s]=100+ADV_M[r]+FIL[f];PE[1][s]=112+ADV_E[r]+FIL[f]//2
  PM[2][s]=304+9*c+(8 if r in (4,5) and c>=3 else 0);PE[2][s]=310+7*c
  PM[3][s]=330+5*c+2*min(f,7-f);PE[3][s]=345+4*c
  PM[4][s]=500+3*min(f,7-f)+(18 if r==6 else 0);PE[4][s]=525+3*c
  PM[5][s]=950+3*c-(10 if r<=1 else 0);PE[5][s]=1000+5*c
  PM[6][s]=KGF[f]-16*r+(4 if r==0 else 0);PE[6][s]=-50+13*c
 return PM,PE
PMG,PEG=_tables()
def ps2(p,s):
 idx=s if p>0 else s^112
 return PMG[abs(p)][idx],PEG[abs(p)][idx]
def EV():
 ph=PHU
 e=(SCM*ph+SCE*(24-ph))//24
 for c in (1,-1):
  if CB[c]>1:e+=c*((20*ph+36*(24-ph))//24)
  for f in range(8):
   n=PC[c][f]
   if n>1:e-=c*(n-1)*((12*ph+18*(24-ph))//24)
   elif n==1 and (f==0 or PC[c][f-1]==0) and (f==7 or PC[c][f+1]==0):e-=c*((10*ph+14*(24-ph))//24)
  ks=K[c]
  for d in ((17,16,15) if c>0 else (-17,-16,-15)):
   t=ks+d
   if not t&0x88 and B[t]==c:e+=c*6*ph//24
 for s,c in RK.items():
  f=s&7
  if PC[1][f]+PC[-1][f]==0:e+=c*((16*ph+10*(24-ph))//24)
  elif PC[c][f]==0:e+=c*((8*ph+6*(24-ph))//24)
 if PHU<=5:
  for c in (1,-1):
   if NP[c]>=500 and NP[-c]==0:
    lk=K[-c];lf=lk&7;lr=lk>>4
    corner=max(abs(2*lf-7),abs(2*lr-7))
    kd=abs((K[c]&7)-lf)+abs((K[c]>>4)-lr)
    e+=c*(corner*3+(14-kd)*2)
 return e if TM>0 else -e
def AT(s,by):
 for d in ((-15,-17) if by>0 else (15,17)):
  t=s+d
  if not t&0x88 and B[t]==by:return 1
 for d in DN:
  t=s+d
  if not t&0x88 and B[t]==2*by:return 1
 for d in D8:
  t=s+d
  if not t&0x88 and B[t]==6*by:return 1
 for ds,tt in ((D8[4:],(3,5)),(D8[:4],(4,5))):
  for d in ds:
   t=s+d
   while not t&0x88:
    p=B[t]
    if p:
     if abs(p) in tt and (p>0)==(by>0):return 1
     break
    t+=d
 return 0
def GN(cap=0):
 ms=[];ap=ms.append
 for s in range(128):
  if s&0x88:continue
  p=B[s]
  if not p or (p>0)!=(TM>0):continue
  a=abs(p);r=s>>4
  if a==1:
   dr=16*TM;pr=7 if TM>0 else 0;sr=1 if TM>0 else 6;t=s+dr
   if not B[t]:
    if (t>>4)==pr:
     for q in (5,4,3,2):ap((s,t,q))
    elif not cap:
     ap((s,t,0))
     if r==sr and not B[s+2*dr]:ap((s,s+2*dr,0))
   for d in (dr-1,dr+1):
    t=s+d
    if t&0x88:continue
    q=B[t]
    if q and (q>0)!=(TM>0):
     if (t>>4)==pr:
      for x in (5,4,3,2):ap((s,t,x))
     else:ap((s,t,0))
    elif t==EP:ap((s,t,0))
  elif a in (2,6):
   for d in (DN if a==2 else D8):
    t=s+d
    if t&0x88:continue
    q=B[t]
    if not q:
     if not cap:ap((s,t,0))
    elif (q>0)!=(TM>0):ap((s,t,0))
  else:
   for d in (D8[4:] if a==3 else D8[:4] if a==4 else D8):
    t=s+d
    while not t&0x88:
     q=B[t]
     if not q:
      if not cap:ap((s,t,0))
     else:
      if (q>0)!=(TM>0):ap((s,t,0))
      break
     t+=d
 if not cap:
  if TM>0:
   if CR&1 and not B[5] and not B[6] and not AT(4,-1) and not AT(5,-1) and not AT(6,-1):ap((4,6,0))
   if CR&2 and not B[3] and not B[2] and not B[1] and not AT(4,-1) and not AT(3,-1) and not AT(2,-1):ap((4,2,0))
  else:
   if CR&4 and not B[117] and not B[118] and not AT(116,1) and not AT(117,1) and not AT(118,1):ap((116,118,0))
   if CR&8 and not B[115] and not B[114] and not B[113] and not AT(116,1) and not AT(115,1) and not AT(114,1):ap((116,114,0))
 return ms
def MK(m):
 global TM,CR,EP,HS,SCM,SCE,PHU
 if m is None:
  ST.append((m,0,0,CR,EP,HS,SCM,SCE,PHU,K[1],K[-1],CB[1],CB[-1],NP[1],NP[-1]))
  if EP>=0:HS^=ZE[EP&7]
  EP=-1;TM=-TM;HS^=ZS;HP.append(HS);return
 s,t,q=m;p=B[s];cap=B[t];ec=0
 if abs(p)==1 and t==EP and not cap and (s&7)!=(t&7):
  cap=B[t-16*TM];ec=1
 ST.append((m,cap,ec,CR,EP,HS,SCM,SCE,PHU,K[1],K[-1],CB[1],CB[-1],NP[1],NP[-1]))
 HS^=ZC[CR]
 if EP>=0:HS^=ZE[EP&7]
 m1,e1=ps2(p,s);sg=1 if p>0 else -1;SCM-=sg*m1;SCE-=sg*e1;HS^=ZP[(p,s)]
 if cap:
  cs=t-16*TM if ec else t
  m1,e1=ps2(cap,cs);sg2=1 if cap>0 else -1;SCM-=sg2*m1;SCE-=sg2*e1;HS^=ZP[(cap,cs)];B[cs]=0
  ac=abs(cap)
  if ac in (2,3,4,5):PHU-=PW[ac];NP[sg2]-=V[ac]
  if ac==3:CB[sg2]-=1
  if ac==1:PC[sg2][cs&7]-=1
  if ac==4:RK.pop(cs,None)
 np=q*TM if q else p
 B[t]=np;B[s]=0;HS^=ZP[(np,t)]
 m1,e1=ps2(np,t);SCM+=TM*m1;SCE+=TM*e1
 if abs(p)==1:
  PC[TM][s&7]-=1
  if not q:PC[TM][t&7]+=1
 if q:
  if q in (2,3,4,5):PHU+=PW[q];NP[TM]+=V[q]
  if q==3:CB[TM]+=1
  if q==4:RK[t]=TM
 if abs(p)==4:RK.pop(s,None);RK[t]=TM
 if abs(p)==6:
  K[TM]=t
  if abs(t-s)==2:
   rf,rt=(7,5) if t==6 else (0,3) if t==2 else (119,117) if t==118 else (112,115)
   rp=B[rf];HS^=ZP[(rp,rf)];m1,e1=ps2(rp,rf);SCM-=TM*m1;SCE-=TM*e1;B[rt]=rp;B[rf]=0;HS^=ZP[(rp,rt)];m1,e1=ps2(rp,rt);SCM+=TM*m1;SCE+=TM*e1
   RK.pop(rf,None);RK[rt]=TM
 nc=CR
 if abs(p)==6:nc&=12 if TM>0 else 3
 if s==0 or t==0:nc&=~2
 if s==7 or t==7:nc&=~1
 if s==112 or t==112:nc&=~8
 if s==119 or t==119:nc&=~4
 CR=nc;HS^=ZC[CR]
 EP=-1
 if abs(p)==1 and abs(t-s)==32:
  for u in (t-1,t+1):
   if not u&0x88 and (u>>4)==(t>>4) and B[u]==-TM:EP=(s+t)//2
 if EP>=0:HS^=ZE[EP&7]
 TM=-TM;HS^=ZS;HP.append(HS)
def UN():
 global TM,CR,EP,HS,SCM,SCE,PHU
 m,cap,ec,cr,ep,hs,sm,se,ph,kw,kb,cw,cb2,nw,nb2=ST.pop()
 TM=-TM;CR,EP,HS,SCM,SCE,PHU=cr,ep,hs,sm,se,ph
 K[1],K[-1]=kw,kb;CB[1],CB[-1]=cw,cb2;NP[1],NP[-1]=nw,nb2;HP.pop()
 if m is None:return
 s,t,q=m;p=B[t]
 if q:p=TM
 B[s]=p
 if abs(p)==6 and abs(t-s)==2:
  rf,rt=(7,5) if t==6 else (0,3) if t==2 else (119,117) if t==118 else (112,115)
  B[rf]=B[rt];B[rt]=0;RK.pop(rt,None);RK[rf]=TM
 if q==4:RK.pop(t,None)
 elif abs(p)==4:RK.pop(t,None);RK[s]=TM
 if cap:
  cs=t-16*TM if ec else t
  if abs(cap)==4:RK[cs]=-TM
  if abs(cap)==1:PC[-TM][cs&7]+=1
 if abs(p)==1:
  if not q:PC[TM][t&7]-=1
  PC[TM][s&7]+=1
 if ec:B[t]=0;B[t-16*TM]=cap
 elif cap:B[t]=cap
 else:B[t]=0
def QS(a,b,ply):
 global ND,AB
 if AB:return 0
 ND+=1
 if ND>NB:AB=1;return 0
 inch=AT(K[TM],-TM)
 if inch:ms=GN()
 else:
  if ply>16:return EV()
  st=EV()
  if st>=b:return st
  if st>a:a=st
  ms=GN(1)
 ms.sort(key=lambda m:(10*V[abs(B[m[1]])]-V[abs(B[m[0]])]) if B[m[1]] else 900 if m[1]==EP else V[m[2]]*10 if m[2] else 0,reverse=True)
 legal=0
 for m in ms:
  if not inch and not m[2] and B[m[1]] and st+V[abs(B[m[1]])]+150<=a:continue
  MK(m)
  if AT(K[-TM],TM):UN();continue
  legal+=1;v=-QS(-b,-a,ply+1);UN()
  if AB:return 0
  if v>=b:return v
  if v>a:a=v
 if inch and not legal:return -MATE+ply
 return a
def SR(d,a,b,ply):
 global ND,AB
 if AB:return 0
 if d<=0:return QS(a,b,ply)
 ND+=1
 if ND>NB:AB=1;return 0
 if ply>0 and HS in HP[:-1]:return 0
 inch=AT(K[TM],-TM)
 if inch:d+=1
 a0,b0=a,b;ttm=None;ent=TT.get(HS)
 if ent:
  td,tf,tv,tm2=ent;ttm=tm2
  if td>=d:
   if tf==0:return tv
   if tf==1 and tv>=b:return tv
   if tf==2 and tv<=a:return tv
 if d>=3 and not inch and b<MATE-1000 and NP[TM]>=330:
  MK(None);v=-SR(d-1-(2 if d<7 else 3),-b,-b+1,ply+1);UN()
  if AB:return 0
  if v>=b:return v
 fut=0
 if d<=2 and not inch and b-a<=1:
  se=EV()
  if se+150*d<=a:fut=1
 ms=GN()
 hh=HH[TM]
 def key(m):
  if m==ttm:return 10**7
  s,t,q=m;cp=B[t]
  if cp:return 100000+10*V[abs(cp)]-V[abs(B[s])]//20
  if q:return 90000+V[q]
  if m in KL.get(ply,()):return 80000
  return hh.get((s,t),0)
 ms.sort(key=key,reverse=True);best=-INF;bm=None;legal=0
 for i,m in enumerate(ms):
  iscap=1 if B[m[1]] or (abs(B[m[0]])==1 and m[1]==EP) else 0
  if fut and legal>=1 and not iscap and not m[2]:continue
  MK(m)
  if AT(K[-TM],TM):UN();continue
  legal+=1
  if legal==1:v=-SR(d-1,-b,-a,ply+1)
  else:
   rd=d-1
   if d>=3 and i>=3 and not inch and not iscap and not m[2]:
    rd=d-2-(1 if i>=9 else 0)
   v=-SR(rd,-a-1,-a,ply+1)
   if v>a and rd<d-1:v=-SR(d-1,-a-1,-a,ply+1)
   if v>a and v<b:v=-SR(d-1,-b,-a,ply+1)
  UN()
  if AB:return 0
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:
   if not iscap and not m[2]:
    KL[ply]=[m]+[x for x in KL.get(ply,[]) if x!=m][:1]
    hh[(m[0],m[1])]=hh.get((m[0],m[1]),0)+d*d
   break
 if not legal:return -MATE+ply if inch else 0
 TT[HS]=(d,2 if best<=a0 else 1 if best>=b0 else 0,best,bm)
 return best
def PF(fen):
 global TM,CR,EP,HS,SCM,SCE,PHU
 B[:]=[0]*128;SCM=0;SCE=0;PHU=0;CB[1]=CB[-1]=0;NP[1]=NP[-1]=0
 PC[1][:]=[0]*8;PC[-1][:]=[0]*8;RK.clear()
 pt=fen.split();rows=pt[0].split('/');mp={'p':1,'n':2,'b':3,'r':4,'q':5,'k':6}
 for i,row in enumerate(rows):
  r=7-i;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    p=mp[ch.lower()]*(1 if ch.isupper() else -1);s=r*16+f;B[s]=p;f+=1;sg=1 if p>0 else -1
    m1,e1=ps2(p,s);SCM+=sg*m1;SCE+=sg*e1
    if abs(p)==6:K[sg]=s
    else:
     if abs(p) in (2,3,4,5):PHU+=PW[abs(p)];NP[sg]+=V[abs(p)]
     if abs(p)==3:CB[sg]+=1
     if abs(p)==1:PC[sg][s&7]+=1
     if abs(p)==4:RK[s]=sg
 TM=1 if pt[1]=='w' else -1;CR=0
 for ch,bit in (('K',1),('Q',2),('k',4),('q',8)):
  if ch in pt[2]:CR|=bit
 EP=-1
 if pt[3]!='-':EP=(int(pt[3][1])-1)*16+ord(pt[3][0])-97
 HS=0
 for s in range(128):
  if B[s]:HS^=ZP[(B[s],s)]
 HS^=ZC[CR]
 if EP>=0:HS^=ZE[EP&7]
 if TM<0:HS^=ZS
 HP.clear();HP.extend(GH);HP.append(HS)
PM={5:'q',4:'r',3:'b',2:'n'}
def UC(m):
 s,t,q=m;u=chr(97+(s&7))+str((s>>4)+1)+chr(97+(t&7))+str((t>>4)+1)
 return u+PM[q] if q else u
def BM(fen):
 global ND,AB
 PF(fen);ND=0;AB=0
 if len(TT)>300000:TT.clear()
 ms=[]
 for m in GN():
  MK(m)
  if not AT(K[-TM],TM):ms.append(m)
  UN()
 if not ms:return None
 if len(ms)==1:return UC(ms[0])
 ms.sort(key=lambda m:(10*V[abs(B[m[1]])]-V[abs(B[m[0]])]) if B[m[1]] else 0,reverse=True)
 scored=[(0,m) for m in ms]
 best=ms[0]
 for d in range(1,40):
  a=-INF;cb=None;ns=[]
  for sc,m in scored:
   MK(m);v=-SR(d-1,-INF,-a,1) if cb is not None else -SR(d-1,-INF,INF,1);UN()
   if AB:break
   ns.append((v,m))
   if cb is None or v>a:a=v;cb=m
  if AB:break
  scored=sorted(ns,key=lambda x:-x[0]);best=cb
  if a>MATE-1000:break
 return UC(best)
LG=0
while True:
 g=P('/game',{})
 if g.get('status')=='done':break
 while g.get('status')=='your_move':
  if g['game']!=LG:LG=g['game'];GH.clear()
  mv=BM(g['fen']);GH.append(HS);lm=g.get('legal_moves') or []
  if mv not in lm and lm:mv=lm[0]
  g=P('/move',{'game':g['game'],'move':mv})
 if g.get('status')=='done':break
