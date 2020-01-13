#!/bin/bash

# echo 'Try to install conda for environment management'
#pip install conda
#echo 'Done installing conda.'

#echo 'Create environment for FACEID:'
#conda create -n faceid-test python=3.6 -y

#echo 'Eval'
#eval "$(conda shell.bash hook)"
#conda activate faceid-test

echo 'Trying to install face_recognition'
pip install cmake face_recognition opencv-python pyzbar requests imutils Pillow

echo 'Everything is installed!'
echo ''
echo ''
echo '********************************************************'
echo ''
echo 'Please use this environment: conda activate faceid-test'
echo 'Navigate to: cd src/controller'
echo 'Start programm with: python3 Controller.py'
echo ''
echo '********************************************************'
echo ''
echo ''