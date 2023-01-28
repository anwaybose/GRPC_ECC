from concurrent import futures
import time

import grpc
import greet_pb2
import greet_pb2_grpc

import hashlib, secrets, binascii
import pickle

from Crypto.PublicKey import RSA

from python_crypto.utils import Crypto_Node

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply
    
    def ParrotSaysHello(self, request, context):
        print("ParrotSaysHello Request Made:")
        print(request)

        for i in range(3):
            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)

    def ChattyClientSaysHello(self, request_iterator, context):
        delayed_reply = greet_pb2.DelayedReply()
        for request in request_iterator:
            print("ChattyClientSaysHello Request Made:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

    def InteractingHello(self, request_iterator, context):
        for request in request_iterator:
            print("InteractingHello Request Made:")
            print(request)

            hello_reply = greet_pb2.HelloReply()
            hello_reply.message = f"{request.greeting} {request.name}"

            yield hello_reply

    def JoinHello(self, request, context):
        print("SayHello Request Made:")
        #print(request)
        hello_reply = greet_pb2.HelloReply()
        # packet = f"{request.greeting} {request.name} {request.pub_key}"
        if request.name == "A":
            d_key = request.pub_key # bytes(request.pub_key, 'utf-8')
            pubKey = pickle.loads(d_key)
            privKey = pickle.loads(request.Priv_key)
            #msg = bytes(request.greeting, 'utf-8')
            msg = request.message
            decryptedMsg = cn.decrypt_ECC(msg, privKey)
            Msg = decryptedMsg.decode('utf-8')
        elif request.name == "B":
            keypair = RSA.importKey(request.Priv_key)
            #msg = bytes(request.greeting, 'utf-8')
            msg = request.message
            decryptedMsg = cn.decrypt_RSA(msg, keypair)
            Msg = decryptedMsg.decode('utf-8')

        hello_reply.message = f"{Msg}"

        return hello_reply
    
    def CertHello(self, request, context):
        print("SayHello Request Made:")
        print(request)
        hello_reply = greet_pb2.HelloReply()
        hello_reply.message = f"{request.greeting} {request.name} {request.pub_key}"

        return hello_reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    cn = Crypto_Node()
    serve()