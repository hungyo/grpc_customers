"""The Python implementation of the GRPC customerList server."""

from concurrent import futures
import time

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


cust_list=[]
#custs= "The customers are : "
#custss=" The registered customers are : "
def ListCustomer(request, context):
        print("*********Sending the list of the registered customers**********")
        custss=" "
        for i in range(len(cust_list)):
                custss=custss+" "+cust_list[i]
        return custss
        #return customer_pb2.Customers(message='Hello, %s!' % request.name)

def DelCustomer(request, context):
        if request.name.split(" ")[1] not in cust_list:
                print(request.name.split(" ")[1], " is not registered!!So can't delete!!")
        else :
                print("Deleting the customer ",request.name.split(" ")[1] )
                cust_list.remove(request.name.split(" ")[1])
        return ListCustomer(request, context)

def AddCust(request, context):
        global custss
        if request.name in cust_list:
                print("Customer ",request.name," is already added!!")
        else :
                print("Adding ",request.name)
                cust_list.append(request.name)
        #print("*****Current registered customers****")
        return ListCustomer(request, context)

class Greeter(helloworld_pb2_grpc.GreeterServicer):

  def SayHello(self, request, context):
    if request.name=="list":
                icust=ListCustomer(request, context)
                return helloworld_pb2.HelloReply(message='%s!' % icust)
    elif request.name.split(" ")[0]=="delete":
                cust=DelCustomer(request, context)
                return helloworld_pb2.HelloReply(message='%s!' % cust)
    else :
                cust=AddCust(request, context)
                return helloworld_pb2.HelloReply(message='%s!' % cust)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
