#!/usr/bin/env python3
# coding=utf-8


def separate_vals(input_str: str, delimiter: str) -> bytes:
    q_vals = input_str.split(delimiter)

    return "\r\n".join(q_vals).encode()


def app(env, start_response):
    """
        Application for the WSGI server
    """
    resp = separate_vals(env["QUERY_STRING"], "&")

    status = "200 OK"
    response_headers = [
            ("Content-type", "text/plain"),
            ("Content-Length", str(len(resp)))
            ]
    start_response(status, response_headers)

    yield resp
