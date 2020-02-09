package main

import (
    "fmt"
    "strconv"
)

type IPAddr [4]byte

// TODO: Add a "String() string" method to IPAddr.
func (ipaddr IPAddr) String1() string {
    return fmt.Sprintf(
        "%v.%v.%v.%v",
        ipaddr[0], ipaddr[0], ipaddr[0], ipaddr[0],
    )
}

func (ipaddr IPAddr) String() string {
    var ipaddrStr string
    for i, octet := range ipaddr {
        ipaddrStr += strconv.FormatInt(int64(octet), 10)
        if i < (len(ipaddr) - 1) {
            ipaddrStr += "."
        }
    }
    return ipaddrStr
}

func main() {
    hosts := map[string]IPAddr{
        "loopback":  {127, 0, 0, 1},
        "googleDNS": {8, 8, 8, 8},
    }
    for name, ip := range hosts {
        fmt.Printf("%v: %v\n", name, ip)
    }
}
