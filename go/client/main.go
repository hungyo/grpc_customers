package main

import (
        "log"
        "os"

        "golang.org/x/net/context"
        "google.golang.org/grpc"
        pb "google.golang.org/grpc/examples/helloworld/helloworld"
)

const (
        address     = "localhost:50051"
        defaultName = "list"
)

func main() {
        // Set up a connection to the server.
        conn, err := grpc.Dial(address, grpc.WithInsecure())
        if err != nil {
                log.Fatalf("did not connect: %v", err)
        }
        defer conn.Close()
        c := pb.NewGreeterClient(conn)

        // Contact the server and print out its response.
        name := defaultName
        if len(os.Args) < 1 {
                name = defaultName
        } else if os.Args[1] == "delete" {
                name = os.Args[1] + " " +  os.Args[2]
        } else {
                name = os.Args[1]
        }
        //if os.Args[1] != "delete"{
        //      r, err := c.SayHello(context.Background(), &pb.HelloRequest{Name: name+" "+os.Args[2]})
        //}else {
        r, err := c.SayHello(context.Background(), &pb.HelloRequest{Name: name})
        //}
        if err != nil {
                log.Fatalf("could not greet: %v", err)
        }
        log.Printf("The rgistered customers are : %s", r.Message)
}
