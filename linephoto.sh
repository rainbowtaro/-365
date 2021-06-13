#!/bin/bash
# -*- coding: utf-8 -*-
#日付とファイル名を生成
date=$(date +"%m.%d")
photo_file="/home/pi/デスクトップ/寝癖365/picture/${date}.jpg"
token="********************************:"
#解像度の設定
raspistill -w 1280 -h 1024 -br 60 -o $photo_file
#写真を撮影
curl -X POST -H "Authorization: Bearer ${token}" -F "message = ${date}" -F "imageFile=@${photo_file}" https://notify-api.line.me/api/notify

/usr/bin/python3 /home/pi/デスクトップ/寝癖365/GM365.py
