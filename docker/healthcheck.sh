#!/bin/sh
wget --no-verbose --tries=1 --spider http://localhost:5000/health || exit 1 