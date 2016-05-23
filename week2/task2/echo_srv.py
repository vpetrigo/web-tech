#!/usr/bin/env python3
# coding=utf-8

import socket
import select

def interpret_buffer(buf) -> str:
    return buf.decode().rstrip()

def server_loop(server_sock) -> None:
    incoming_con = [server_sock]

    while True:
        ready_rd, *not_used = select.select(incoming_con, [], [])
        print(ready_rd)

        for cl in ready_rd:
            if cl == server_sock:
                (conn, addr) = server_sock.accept()
                conn.setblocking(False)
                incoming_con.append(conn)
            else:
                buf = cl.recv(1024)

                if not buf or interpret_buffer(buf) == "close":
                    cl.shutdown(socket.SHUT_RDWR)
                    cl.close()
                    incoming_con.remove(cl)
                else:
                    conn.send(buf)



def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.bind((str(socket.INADDR_ANY), 2222))
    sock.listen()

    server_loop(sock)

    sock.close()

if __name__ == "__main__":
    main()
