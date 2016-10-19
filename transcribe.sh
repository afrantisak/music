#!/usr/bin/env bash

/home/franta/Downloads/Cadence-0.8.1/Claudia &
sleep 1
ladish_control sload transcribe
sleep 1
ladish_control sstart
