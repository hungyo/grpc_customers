"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import sys
import helloworld_pb2
import helloworld_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = helloworld_pb2_grpc.GreeterStub(channel)
  print ("Argument passed is : ",sys.argv[1])
  if sys.argv[1]=="list":
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='list'))
  elif sys.argv[1]=="delete" :
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='delete '+sys.argv[2]))
  else :
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=sys.argv[1]))
  print("The registerd customers are : ",response.message)
  #response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))


if __name__ == '__main__':
  run()
