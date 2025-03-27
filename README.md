### **Technique 2: Hybrid AES + RSA for Encryption and Digital Signatures**  

#### **Key Generation:**  
- When SU creates an account, SYS generates RSA-1.  
  - SYS gives SU its public key (RSA-1).  
  - SYS keeps its private key (RSA-1).  
- SU generates RSA-2.  
  - SU keeps its private key (RSA-2).  
  - SU gives its public key (RSA-2) to SYS.  

This means:  
- **SYS has:** private key (RSA-1), public key (RSA-1), and public key (RSA-2).  
- **SU has:** public key (RSA-1), private key (RSA-2), and public key (RSA-2).  

---

### **Workflow:**  

#### **Input:**  
1. SU encrypts the input using AES. Then, SU encrypts the AES key using the public key (RSA-1).  
2. SU creates a digital signature using its private key (RSA-2) on the AES-encrypted data and the RSA-1 encrypted key.  
3. SU sends the AES-encrypted input, RSA-1 encrypted key, and digital signature to SYS.  
4. SYS verifies the signature using SU’s public key (RSA-2).  
5. SYS decrypts the AES key using its private key (RSA-1).  
6. SYS decrypts the input using the recovered AES key.  

#### **Output:**  
1. SYS encrypts the output using AES. Then, SYS encrypts the AES key using SU’s public key (RSA-2).  
2. SYS creates a digital signature using its private key (RSA-1) on the AES-encrypted output and the RSA-2 encrypted key.  
3. SYS sends the AES-encrypted output, RSA-2 encrypted key, and digital signature to SU.  
4. SU verifies the signature using SYS’s public key (RSA-1).  
5. SU decrypts the AES key using its private key (RSA-2).  
6. SU decrypts the output using the recovered AES key.  

---

### **Man-in-the-Middle (MITM) Prevention:**  
- Public key sharing is the vulnerable step where MITM attacks can occur.  
- **Solution:**  
  - RSA-1 is fixed, created by SYS only once, and shared with SU only once.  
  - RSA-2 is fixed, created by SU only once, and shared with SYS only once.  
  - A trusted third party should be used to securely exchange these public keys.  
  - Once securely exchanged, no MITM attack is possible.  
