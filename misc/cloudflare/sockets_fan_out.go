// socket-client project main.go
package main
import (
        "fmt"
        "net"
)
const (
        SERVER_HOST = "localhost"
        SERVER_PORT = "9988"
        SERVER_TYPE = "tcp"
)

type SocketAReader struct {
    SocketA: net.Conn
    ChannelsB: map[int]chan []byte
}

func NewSocketAReader() {
    connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
    if err != nil {
        panic(err)
    }
    
    return SocketAReader{
        SocketA: connection
    }
}

func (s *SocketAReaader) FanOut() {
    func () {
       for {
            buffer := make([]byte, 1024)
            mLen, err := connection.Read(buffer)
            if err != nil {
                fmt.Println("Error reading:", err.Error())
                return
            }
            
            for _, channelB := range s.ChannelsB {
                channelB <- buffer
            }
       } 
    }()
}

func (s *SocketAReader) AddChannelB (id int, channelB chan []byte) {
    s.channelsB[id] = channelB
}

func (s *SocketAReader) DelChannelB (id int) {
    delete(s.channelsB, id)
}

func (s *SocketAReader) Close() {
    s.SocketA.Close()
} 

type ManagerBWorkers struct {
    WorkersChannels: map[int]chan struct{},
    AReader: SocketsAReader,
}

func NewManagerBWorkers () {
    // TODO
}

func StartWorker(connData connDataDescr) {
    go func () {
        // open socket B
        // ...
        
        chanB = make(chan, []bytes)
        
        
    } ()
}

func main() {
        // //establish connection
        // connection, err := net.Dial(SERVER_TYPE, SERVER_HOST+":"+SERVER_PORT)
        // if err != nil {
        //         panic(err)
        // }
        // ///send some data
        // _, err = connection.Write([]byte("Hello Server! Greetings."))
        // buffer := make([]byte, 1024)
        // mLen, err := connection.Read(buffer)
        // if err != nil {
        //         fmt.Println("Error reading:", err.Error())
        // }
        // fmt.Println("Received: ", string(buffer[:mLen]))
        // defer connection.Close()
}