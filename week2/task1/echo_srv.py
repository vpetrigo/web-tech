#!/usr/bin/env python3
# coding=utf-8

import socket

def interpret_buffer(buf) -> str:
    return buf.decode().rstrip()

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((str(socket.INADDR_ANY), 2222))
    sock.listen()

    (conn, addr) = sock.accept()

    while conn:
        buf = conn.recv(1024)

        # read until getting "close" msg or buffer is not empty
        if not buf or interpret_buffer(buf) == "close":
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
            break
        conn.send(buf)

    sock.close()

if __name__ == "__main__":
    main()
