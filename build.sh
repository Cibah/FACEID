#!/bin/bash
cp -fr src/ ./debian_package/opt/faceid/
cp faceid.py ./debian_package/opt/faceid/
dpkg-deb -b ./debian_package faceid.deb
