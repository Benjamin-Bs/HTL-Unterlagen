# RSA

(Rivest-Shamir-Adlerman)

public key verfahren 

asymmetrisch weil man zwei Keys benutzt

## Formeln



C = M^(e) (mod n)            (e,n) ... public key

M = C^(d) (mod n)            (d,n) ... private key



1. n = p * q                      p,q ... Primzahlen
   φ(x) = (p-1) * (q-1)

2. ggT( e, φ(n) ) = 1       => e muss Teilerfremd sein

3. e * d = 1( mod φ(n) ) 
   
   

z.b. :

1. n = p * q = 13 * 7 = 91
   φ(n) = (p-1) * (q-1)= 12 * 6 = 72

2. e = 11 

3. python:     pow(11,-1,72) = 59
   probe:       (59 * 11) mod 72 = 1
   
   

M = 42

C = 42^(11)mod 91 = pow(42,11,91) = 35

M = 35^(59) mod 91 = pow(35, 59, 91) = 42
