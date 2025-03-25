Here’s the corrected text in a copy-ready format:  

---

Let's use RSA-1 for encryption and RSA-2 for digital signatures.  

### **Key Generation:**  
- When SU creates an account, SYS generates RSA-1.  
  - SYS gives SU his public key (RSA-1).  
  - SYS keeps his private key (RSA-1).  
- SU generates RSA-2.  
  - SU keeps his private key (RSA-2).  
  - SU gives his public key (RSA-2) to SYS.  

This means:  
- SYS has **private key (RSA-1), public key (RSA-1), and public key (RSA-2)**.  
- SU has **public key (RSA-1), private key (RSA-2), and public key (RSA-1)**.  

### **Workflow:**  

#### **Input:**  
1. SU creates a digital signature using private key (RSA-2).  
2. SU encrypts the input using public key (RSA-1).  
3. SU sends both the encrypted input and digital signature to SYS.  
4. SYS decrypts the input using private key (RSA-1).  
5. SYS verifies the signature using public key (RSA-2).  

#### **Output:**  
1. SYS creates a digital signature using private key (RSA-1).  
2. SYS encrypts the output using public key (RSA-2).  
3. SYS sends both the encrypted output and digital signature to SU.  
4. SU decrypts the output using private key (RSA-2).  
5. SU verifies the signature using public key (RSA-1).  

### **Man-in-the-Middle Prevention:**  
- Public key sharing is the vulnerable step where MITM can occur.  
- **Solution:**  
  - RSA-1 is fixed, created by SYS only once, and shared with SU only once.  
  - RSA-2 is fixed, created by SU only once, and shared with SYS only once.  
  - To securely exchange these public keys, use a trusted third party.  
  - Once exchanged securely, no MITM attack is possible.  
