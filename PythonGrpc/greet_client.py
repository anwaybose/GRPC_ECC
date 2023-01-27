import greet_pb2_grpc
import greet_pb2
import time
import grpc

import hashlib, secrets, binascii
import pickle

from python_crypto.utils import Crypto_Node

def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop chatting): ")

        if name == "":
            break

        hello_request = greet_pb2.HelloRequest(greeting = "Hello", name = name)
        yield hello_request
        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")
        print("5. Join Hello")
        print("6. Cert Hello")
        rpc_call = input("Which rpc would you like to make: ")
        print("A. ECC")
        print("B. RSA")
        rpc_encrypt = input("What Encryption")
        msg = input("What is the message?") #'Hello world \n\n what a good encryption'

        if rpc_encrypt == "A":
            privKey = secrets.randbelow(cn.curve.field.n)
            msg =  bytes(msg, 'utf-8')
            d_priv = pickle.dumps(privKey)
            d_key = pickle.dumps(privKey * cn.curve.g)
            pubKey = pickle.loads(d_key)
            encryptedMsg = cn.encrypt_ECC(msg, pubKey)
            enc_msg = pickle.dumps(encryptedMsg)
        elif rpc_encrypt == "B":
            KeyPair = cn.keyPair
            d_priv = pickle.dumps(KeyPair)
            pubKey = KeyPair.publickey()
            d_key = pubKey.exportKey('DER')
            encryptedMsg = cn.encrypt_RSA(msg, pubKey)
            enc_msg = pickle.dumps(encryptedMsg)

        


        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)
        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Received:")
                print(hello_reply)
        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

            print("ChattyClientSaysHello Response Received:")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("InteractingHello Response Received: ")
                print(response)
        elif rpc_call == "5":
            hello_request = greet_pb2.Hello_join_Request(greeting = enc_msg.decode(), name = rpc_encrypt, pub_key = d_key, priv_key = d_priv)
            hello_reply = stub.JoinHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)
        elif rpc_call == "6":
            hello_request = greet_pb2.Hello_cert_Request(greeting = "Bonjour", name = "YouTube", pub_key = "PUBLIC KEY")
            hello_reply = stub.CertHello(hello_request)
            print("SayHello Response Received:")
            print(hello_reply)

if __name__ == "__main__":
    cn = Crypto_Node()
    run()
