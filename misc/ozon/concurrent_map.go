package main

import (
    "fmt"
    "sync"
    "time"
    "hash/fnv"
)

type SimpleConcurrentMap struct {
    data map[string]int
    // RWMutex vs Mutex: readers don't have to wait for each other; they only have to wait for writers holding the lock
    sync.RWMutex
}

func (scm *SimpleConcurrentMap) Read(key string) int {
    defer scm.RUnlock()

    scm.RLock()
    return scm.data[key]
}

func (scm *SimpleConcurrentMap) Write(key string, value int) {
    defer scm.Unlock()

    scm.Lock()
    scm.data[key] = value
}

type ShardedConcurrentMap []*SimpleConcurrentMap
var shardCount = 16

func InitShardedConcurrentMap() ShardedConcurrentMap {
    shcm := make(ShardedConcurrentMap, shardCount)
    for i := 0; i < shardCount; i++ {
        shcm[i] = &SimpleConcurrentMap{data: make(map[string]int)}
    }

    return shcm
}

func (shcm *ShardedConcurrentMap) GetShardNo(key string) int {
    h := fnv.New32a()
    h.Write([]byte(key))
    sum32 := h.Sum32()
    shardNo := sum32 % uint32(shardCount)
    return int(shardNo)
}

func (shcm ShardedConcurrentMap) Read(key string) int {
    shard := shcm[shcm.GetShardNo(key)]
    defer shard.RUnlock()

    shard.RLock()
    return shard.data[key]
}

func (shcm ShardedConcurrentMap) Write(key string, value int) {
    shard := shcm[shcm.GetShardNo(key)]
    defer shard.Unlock()

    shard.Lock()
    shard.data[key] = value
}

func GetKey(i int) string {
    return fmt.Sprintf("key_%d", i)
}

func SomeWriter(cache *SimpleConcurrentMap, i, j int) {
    cache.Write(GetKey(i), j)
}

func main () {
    cache := SimpleConcurrentMap{data: make(map[string]int)};
    for i := 1; i < 10; i++ {
        go SomeWriter(&cache, i, i)
    }
    time.Sleep(100 * time.Millisecond)
    for i := 1; i < 10; i++ {
        fmt.Println(i, cache.Read(GetKey(i)))
    }

    shardedCache := InitShardedConcurrentMap()
    for i := 1; i < 10; i++ {
        shardedCache.Write(GetKey(i), i)
    }
    time.Sleep(100 * time.Millisecond)
    for i := 1; i < 10; i++ {
        fmt.Println(i, shardedCache.Read(GetKey(i)))
    }
}

