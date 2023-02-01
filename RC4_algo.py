#RC4 or Rivest Cipher 4
def initial(K): #initialising 
 S=[] 
 T=[]
 for _ in range(256): 
 
  S.append(_)#Assumed S of 256 length and contains all element from 0 to 256
  T.append(K[_%(len(K))]) #keylen =len(Key)
 return S,T

def permutation(S,T):
 j=0 #permutaion
 for _ in range(256):
  j=(j+S[_]+T[_])%256
  S[j],S[_]=S[_],S[j]
 return S

def stream_gen(S):
 i=0
 j=0
 k=[] #Not to be confused with key , it is stream
 while len(k)<8: #Generated stream of 8 elements but can be increased.
  i=(i+1)%256
  j=(j+S[i])%256
  S[j],S[i]=S[i],S[j]
  t=(S[i]+S[j])%256
  k.append(S[t])
 return k

def encryption(P,k): #Encrypting Plain text
 Z=[P[_]^k[_] for _ in range(len(P))] #XORing stream and plain text
 return Z

P=[1,2,3,4,2,1,9,8]#Plain text
K=[1,7,9,4,3,6,9,5,6,3,2,3,7] #Key
S,T=initial(K)
S2=permutation(S,T)
k=stream_gen(S2)
print(k) #Printing stream 
e=encryption(P,k)
print(e) #Printing encrypted msg