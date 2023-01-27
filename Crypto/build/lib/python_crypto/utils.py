#!/usr/bin/env python

# libraries raries for ECC
from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii
import pickle
# loibraries for rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES

class Crypto_Node(object):
    def __init__(self):
        # generate ECC curve
        self.curve = registry.get_curve('brainpoolP256r1')
        # generate RSA keypair
        self.keyPair = RSA.generate(1024)


## ECC 
    def encrypt_AES_GCM(self, msg, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        return (ciphertext, aesCipher.nonce, authTag)

    def decrypt_AES_GCM(self, ciphertext, nonce, authTag, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext

    def ecc_point_to_256_bit_key(self, point):
        sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
        sha.update(int.to_bytes(point.y, 32, 'big'))
        return sha.digest()
    
    def encrypt_ECC(self, msg, pubKey):
        ciphertextPrivKey = secrets.randbelow(self.curve.field.n)
        sharedECCKey = ciphertextPrivKey * pubKey
        secretKey = self.ecc_point_to_256_bit_key(sharedECCKey)
        ciphertext, nonce, authTag = self.encrypt_AES_GCM(msg, secretKey)
        ciphertextPubKey = ciphertextPrivKey * self.curve.g
        return (ciphertext, nonce, authTag, ciphertextPubKey)

    def decrypt_ECC(self, encryptedMsg, privKey):
        (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
        sharedECCKey = privKey * ciphertextPubKey
        secretKey = self.ecc_point_to_256_bit_key(sharedECCKey)
        plaintext = self.decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
        return plaintext
    


## RSA
    '''
    def encrypt_AES_GCM(self, msg, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM)
        ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
        return (ciphertext, aesCipher.nonce, authTag)

    def decrypt_AES_GCM(self, ciphertext, nonce, authTag, secretKey):
        aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
        return plaintext
    '''

    def encrypt_RSA(self, msg, pubKey):
        encryptor = PKCS1_OAEP.new(pubKey)
        session_key = get_random_bytes(16)
        encryptedsk = encryptor.encrypt(session_key) # encrypt session key with 
        ciphertext, nonce, authTag = self.encrypt_AES_GCM(msg, session_key)

        return (ciphertext, nonce, authTag, encryptedsk)
        
    #def decrypt_RSA(self, encryptedMsg, keyPair):
    def decrypt_RSA(self, encryptedMsg):
        ciphertext, nonce, authTag, encryptedsk = encryptedMsg
        decryptor = PKCS1_OAEP.new(self.keyPair)
        session_key = decryptor.decrypt(encryptedsk)
        
        plaintext = self.decrypt_AES_GCM(ciphertext, nonce, authTag, session_key)
        return plaintext



if __name__ == "__main__" :
    crypto_node = Crypto_Node()