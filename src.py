import os,json,urllib.request as UQ,random
E=os.environ["MAKEFUN_ENV_URL"]
def P(p,d):
 r=UQ.Request(E+p,data=json.dumps(d).encode(),headers={"Content-Type":"application/json"})
 return json.loads(UQ.urlopen(r).read())
B=[0]*128;TM=1;CR=0;EP=-1;HS=0;SC=0;PH=0;ND=0;AB=0;NB=95000;GH=[]
TT={};KL={};ST=[];HP=[];K={};CB={1:0,-1:0};NP={1:0,-1:0}
RG=random.Random(987123)
ZP={(p,s):RG.getrandbits(64) for p in range(-6,7) if p for s in range(128)}
ZS=RG.getrandbits(64);ZC=[RG.getrandbits(64) for _ in range(16)];ZE=[RG.getrandbits(64) for _ in range(8)]
V={1:100,2:320,3:330,4:500,5:950,6:0};PA=[0,0,6,14,28,48,80,0];FB=[0,2,4,6,6,4,2,0]
D8=[16,-16,1,-1,17,15,-17,-15];DN=[33,31,18,14,-14,-18,-31,-33];MATE=100000;INF=10**9
def ps(p,s):
 f=s&7;r=s>>4
 if p<0:r=7-r
 a=abs(p);c=min(f,7-f)+min(r,7-r)
 if a==1:return 100+PA[r]+FB[f]
 if a==2:return 320+5*c-8
 if a==3:return 330+3*c
 if a==4:return 500+FB[f]+(18 if r==6 else 0)
 if a==5:return 950+2*c
 return 0
def ct(p,s):return ps(p,s) if p>0 else -ps(p,s)
def KT(s,c):
 f=s&7;r=s>>4
 if c<0:r=7-r
 cc=min(f,7-f)+min(r,7-r)
 return 5*cc-12 if PH<2400 else 8-5*cc
def EV():
 e=SC+KT(K[1],1)-KT(K[-1],-1)+(25 if CB[1]>1 else 0)-(25 if CB[-1]>1 else 0)
 if PH>=2000:
  for c,sg in ((1,16),(-1,-16)):
   ks=K[c]
   for d in (sg-1,sg,sg+1):
    t=ks+d
    if not t&0x88 and B[t]==c:e+=7
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
   if not cap and not B[t]:
    if (t>>4)==pr:
     for q in (5,4,3,2):ap((s,t,q))
    else:
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
 global TM,CR,EP,HS,SC,PH
 if m is None:
  ST.append((m,0,0,CR,EP,HS,SC,PH,K[1],K[-1],CB[1],CB[-1],NP[1],NP[-1]))
  if EP>=0:HS^=ZE[EP&7]
  EP=-1;TM=-TM;HS^=ZS;HP.append(HS);return
 s,t,q=m;p=B[s];cap=B[t];ec=0
 if abs(p)==1 and t==EP and not cap and (s&7)!=(t&7):
  cap=B[t-16*TM];ec=1
 ST.append((m,cap,ec,CR,EP,HS,SC,PH,K[1],K[-1],CB[1],CB[-1],NP[1],NP[-1]))
 HS^=ZC[CR]
 if EP>=0:HS^=ZE[EP&7]
 HS^=ZP[(p,s)];SC-=ct(p,s)
 if cap:
  cs=t-16*TM if ec else t
  HS^=ZP[(cap,cs)];SC-=ct(cap,cs);B[cs]=0
  if abs(cap) in (2,3,4,5):PH-=V[abs(cap)];NP[1 if cap>0 else -1]-=V[abs(cap)]
  if abs(cap)==3:CB[1 if cap>0 else -1]-=1
 np=q*TM if q else p
 B[t]=np;B[s]=0;HS^=ZP[(np,t)];SC+=ct(np,t)
 if q:
  if q in (2,3,4,5):PH+=V[q];NP[TM]+=V[q]
  if q==3:CB[TM]+=1
 if abs(p)==6:
  K[TM]=t
  if abs(t-s)==2:
   rf,rt=(7,5) if t==6 else (0,3) if t==2 else (119,117) if t==118 else (112,115)
   rp=B[rf];HS^=ZP[(rp,rf)];SC-=ct(rp,rf);B[rt]=rp;B[rf]=0;HS^=ZP[(rp,rt)];SC+=ct(rp,rt)
 nc=CR
 if abs(p)==6:nc&=12 if TM>0 else 3
 if s==0 or t==0:nc&=~2
 if s==7 or t==7:nc&=~1
 if s==112 or t==112:nc&=~8
 if s==119 or t==119:nc&=~4
 CR=nc;HS^=ZC[CR]
 EP=(s+t)//2 if abs(p)==1 and abs(t-s)==32 else -1
 if EP>=0:HS^=ZE[EP&7]
 TM=-TM;HS^=ZS;HP.append(HS)
def UN():
 global TM,CR,EP,HS,SC,PH
 m,cap,ec,cr,ep,hs,sc,ph,kw,kb,cw,cb2,nw,nb2=ST.pop()
 TM=-TM;CR,EP,HS,SC,PH=cr,ep,hs,sc,ph
 K[1],K[-1]=kw,kb;CB[1],CB[-1]=cw,cb2;NP[1],NP[-1]=nw,nb2;HP.pop()
 if m is None:return
 s,t,q=m;p=B[t]
 if q:p=TM
 B[s]=p
 if abs(p)==6 and abs(t-s)==2:
  rf,rt=(7,5) if t==6 else (0,3) if t==2 else (119,117) if t==118 else (112,115)
  B[rf]=B[rt];B[rt]=0
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
  if ply>14:return EV()
  st=EV()
  if st>=b:return st
  if st>a:a=st
  ms=GN(1)
 ms.sort(key=lambda m:(10*V[abs(B[m[1]])]-V[abs(B[m[0]])]) if B[m[1]] else 900 if m[1]==EP else V[m[2]] if m[2] else 0,reverse=True)
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
 if d>=3 and not inch and b<MATE-1000 and NP[TM]>0:
  MK(None);v=-SR(d-3,-b,-b+1,ply+1);UN()
  if AB:return 0
  if v>=b:return v
 ms=GN()
 def key(m):
  if m==ttm:return 10**7
  s,t,q=m;cp=B[t]
  if cp:return 100000+10*V[abs(cp)]-V[abs(B[s])]//20
  if q:return 90000+V[q]
  if m in KL.get(ply,()):return 80000
  return 0
 ms.sort(key=key,reverse=True);best=-INF;bm=None;legal=0
 for i,m in enumerate(ms):
  iscap=1 if B[m[1]] or (abs(B[m[0]])==1 and m[1]==EP) else 0
  MK(m)
  if AT(K[-TM],TM):UN();continue
  legal+=1
  if legal==1:v=-SR(d-1,-b,-a,ply+1)
  else:
   rd=d-2 if (d>=3 and i>=3 and not inch and not iscap and not m[2]) else d-1
   v=-SR(rd,-a-1,-a,ply+1)
   if v>a and rd<d-1:v=-SR(d-1,-a-1,-a,ply+1)
   if v>a and v<b:v=-SR(d-1,-b,-a,ply+1)
  UN()
  if AB:return 0
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:
   KL[ply]=[m]+[x for x in KL.get(ply,[]) if x!=m][:1];break
 if not legal:return -MATE+ply if inch else 0
 TT[HS]=(d,2 if best<=a0 else 1 if best>=b0 else 0,best,bm)
 return best
def PF(fen):
 global TM,CR,EP,HS,SC,PH
 B[:]=[0]*128;SC=0;PH=0;CB[1]=CB[-1]=0;NP[1]=NP[-1]=0
 pt=fen.split();rows=pt[0].split('/');mp={'p':1,'n':2,'b':3,'r':4,'q':5,'k':6}
 for i,row in enumerate(rows):
  r=7-i;f=0
  for ch in row:
   if ch.isdigit():f+=int(ch)
   else:
    p=mp[ch.lower()]*(1 if ch.isupper() else -1);s=r*16+f;B[s]=p;f+=1;sg=1 if p>0 else -1
    if abs(p)==6:K[sg]=s
    else:
     SC+=ct(p,s)
     if abs(p) in (2,3,4,5):PH+=V[abs(p)];NP[sg]+=V[abs(p)]
     if abs(p)==3:CB[sg]+=1
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
 best=ms[0]
 for d in range(1,40):
  a=-INF;cb=None
  for m in ms:
   MK(m);v=-SR(d-1,-INF,-a,1) if cb is not None else -SR(d-1,-INF,INF,1);UN()
   if AB:break
   if cb is None or v>a:a=v;cb=m
  if AB:break
  best=cb;ms.remove(cb);ms.insert(0,cb)
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
