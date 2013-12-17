#!/usr/bin python
#coding:utf-8
############################
#give some useful function
############################

import math

#getHammingDict
def getHammingDict(topicDict,baseDict):
  hammingDict = {}
  for topic in topicDict.keys():
    delta = topicDict[key] - baseDict[key]
    if delta >= 0:
      hammingDict[topic] = 1
    else:
      hammingDict[key] = 0
  return hammingDict

#calculate hamming distance of two signal vector
def hammingDis(sigDict1,sigDict2):
  count = 0
  for key in sigDict1.keys():
    if sigDict1[key] != sigDict2[key]:
      count = count + 1
  return count

#calculate cosine similarity of two distribution
#input are two topic dicts
#output is the cosine similarity
def cosineSim(topicDict1,topicDict2):
  dotProduct = 0
  dictPower1 = 0
  dictPower2 = 0
  for key in topicDict1.keys():
    if key not in topicDict2:
      print '%d is not in another dict...' % key
      return
    else:
      dotProduct = dotProduct + topicDict1[key] * topicDict2[key]
      dictPower1 = dictPower1 + topicDict1[key]**2
      dictPower2 = dictPower2 + topicDict2[key]**2
  similarity = dotProduct / (math.sqrt(dictPower1) * math.sqrt(dictPower2))
  return similarity

#calculate KL distance of two distribution
#input are two topic dicts
#output is the cosine similarity
def KLDis(topicDict1,topicDict2):
  distance = 0
  for key in topicDict1.keys():
    if key not in topicDict2:
      print '%d is not in another dict...' % key
      return
    else:
      pro1 = topicDict1[key]
      pro2 = topicDict2[key]
      distance = distance + pro1 * math.log(pro1 / pro2)
  return distance

#calculate KL similarity of two distribution
#input are two topic dicts
#output is the cosine similarity
def KLSim(topicDict1,topicDict2):
  dis1 = KLDis(topicDict1,topicDict2)
  dis2 = KLDis(topicDict2,topicDict1)
  return (dis1 + dis2) / 2.0

#calculate recall,preision and F1-Score
def getTopNIndex(recDict,playlistDict):
  hit = 0
  testNum = len(playlistDict)
  recNum = 0
  for pid in playlistDict.keys():
    playlist = playlistDict[pid]
    lastSid = playlist.getLastSid()
    recList = recDict[pid]
    recNum = recNum + len(recList)
    if lastSid in recList:
      hit = hit + 1
  recall = float(hit * 1.0) / testNum
  precision = float(hit * 1.0) / recNum
  f1 = 2 * ((recall * precision) / (recall + precision))
  return recall,precision,f1

#calculate mae and rmse
def getMAEandRMSE(recDict,playlistDict,songDict):
  mae = 0
  rmse = 0
  testNum = len(playlistDict)
  for pid in playlistDict.keys():
    playlist = playlistDict[pid]
    lastSid = playlist.getLastSid()
    tarDict = songDict[lastSid].getTopicDict()
    recList = recDict[pid]
    recNum = len(recList)
    totalError = 0
    for i in range(0,recNum):
      recSid = recList[i]
      recDict = songDict[recSid].getTopicDict()
      recError = KLSim(recDict,tarDict)
      totalError = totalError + recError
    avgError = float(totalError*1.0) / recNum
    mae = mae + math.fabs(avgError)
    rmse = rmse + avgError**2
  mae = mae / testNum
  rmse = rmse / (testNum - 1)
  rmse = math.sqrt(rmse)
  return mae,rmse
