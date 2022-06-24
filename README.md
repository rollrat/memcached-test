# memcached-test

## how to build memaslap

```sh
# Check
https://medium.com/swlh/the-complete-guide-to-benchmark-the-performance-of-memcached-on-ubuntu-16-04-71edeaf6e740

sudo apt-get install libevent-dev gcc-9 g++-9
cd /usr/bin
mv gcc gcc-new
mv gcc-9 gcc
mv g++ g++-new
mv g++-9 g++

cd libmemcached-1.0.18
./configure  --prefix=/usr --enable-memaslap --with-pic

# Change Makefile
LDFLAGS = 
to
LDFLAGS = -L/lib64 -lpthread 

# Check
https://github.com/gentoo/gentoo/blob/master/dev-libs/libmemcached/files/libmemcached-1.0.18-gcc7.patch


sudo make
sudo make install
```

```sh
cd /usr/bin
mv g++ g++-9
mv g++-new g++
mv gcc gcc-9
mv gcc-new gcc
```

## test

```sh
strace -f memcached 2>&1 | egrep -i "socket|accept|connect|recv|send|read|write|poll|select|sockopt"
strace -f ./clients/memaslap -s 127.0.0.1:11211 -t 20s 2>&1 | egrep -i "socket|accept|connect|recv|send|read|write|poll|select|sockopt"
```

## netperf

```sh
strace -f netserver -D 2>&1 | egrep -i "socket|accept|connect|recv|send|read|write|poll|select|sockopt"
strace -f netperf -H 127.0.0.1 -t TCP_RR -l 1 2>&1 | egrep -i "socket|accept|connect|recv|send|read|write|poll|select|sockopt"
```
