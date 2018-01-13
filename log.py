#!/usr/bin/env python3
'''
This file is to learn about log more detail.
'''
import logging

logging.basicConfig(level=logging.INFO)


def test_log():
    logging.info('I come from logger module!')


if __name__ == '__main__':

    test_log()
