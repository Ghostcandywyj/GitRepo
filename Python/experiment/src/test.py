#!/usr/bin python
#coding:utf-8
############################
#give some test function
############################

import time
import persist
import predict
import util
import logging
import os

# set log's localtion and level
logging.basicConfig(filename=os.path.join(os.getcwd(),'../log/test_log.txt'),level=logging.DEBUG,format='%(asctime)s-%(levelname)s:%(message)s')

#show mae and rmse trends of hybrid methods with different coefficients
def showErrorTrendWithDifferentCoeff_Hybrid(playlistDict,songDict):
  coeffs = [float(x) / 10 for x in range(0,11,1)]
  print coeffs
  maes = []
  rmses = []
  for coeff in coeffs:
    mae,rmse = MAEandRMSE(playlistDict,songDict,5,0,coeff)
    maes.append(mae)
    rmses.append(rmse)
    print mae,rmse
  plt.plot(coeffs,maes,label="MAE")
  plt.plot(coeffs,rmses,label="RMSE")
  plt.title("MAE and RMSE trends of Different Hybrid Coefficients")
  plt.xlabel("lambda")
  plt.ylabel("error")
  plt.legend(loc="upper right")
  plt.savefig("../img/hybrid.png")
  plt.show()

#show mae and rmse trends of cold-law methods with different coefficients
def showErrorTrendWithDifferentCoeff_ColdLaw(playlistDict,songDict):
  coeffs = [x / 10 for x in range(0,100,1)]
  maes = []
  rmses = []
  for coeff in coeffs:
    mae,rmse = MAEandRMSE(playlistDict,songDict,3,coeff)
    maes.append(mae)
    rmses.append(rmse)
  plt.plot(coeffs,maes,label="MAE")
  plt.plot(coeffs,rmses,label="RMSE")
  plt.title("MAE and RMSE trends of Different Cold Coefficients")
  plt.xlabel("coefficient")
  plt.ylabel("error")
  plt.legend(loc="upper right")
  plt.savefig("../img/coldlaw.png")
  plt.show()

#show weight trends of different coefficients
def showColdLawWithDifferentCoeff():
  coeffs = [0.25,0.5,0.75,1.0,5.0]
  x = range(0,20,1)
  for coeff in coeffs:
    weight = [1*math.pow(math.e,-1*coeff*delta) for delta in x]
    label = "coeff = %f" % coeff
    plt.plot(x,weight,label=label)
  plt.xlabel("time")
  plt.ylabel("weight")
  plt.title("Weight Trend of Cold Law with Different Coefficients")
  plt.legend(loc = "upper right")
  plt.savefig("../img/cold-law.png")
  plt.show()

#test traditional method
def testRecMethod(recType):
  start_time = time.time()
  songDict = persist.readSongFromFile()
  playlistDict = persist.readPlaylistFromFile()
  recDict = predict.getRecDict(playlistDict,songDict,recType)
  recall,precision,f1 = util.getTopNIndex(recDict,playlistDict)
  mae,rmse = util.getMAEandRMSE(recDict,playlistDict,songDict)
  if recType == 0:
    info = '################Most Similar####################'
  elif recType == 1:
    info = '################Average####################'
  elif recType == 2:
    info = '################Cold Law####################'
  elif recType == 3:
    info = '################Arima####################'
  elif recType == 4:
    info = '################Hybrid####################'
  else:
    info = '################Most Similar####################'
  print info
  logging.info(info)
  print 'Recall = ',recall
  logging.info('Recall = %f' % recall)
  print 'Precision = ',precision
  logging.info('Precision = %f' % precision)
  print 'F1-Score = ',f1
  logging.info('F1-Score = %f' % f1)
  print 'MAE = ',mae
  logging.info('MAE = %f' % mae)
  print 'RMSE = ',rmse
  logging.info('RMSE = %f' % rmse)
  print 'Average Consumed: %ds' % (time.time()-start_time)
  logging.info('Average Consumed: %ds' % (time.time()-start_time))

#test hamming dis
def testDisMethod():
  start_time = time.time()
  songDict = persist.readSongFromFile()
  playlistDict = persist.readPlaylistFromFile()
  recDict = predict.getRecDictOfDis(playlistDict,songDict)
  recall,precision,f1 = util.getTopNIndex(recDict,playlistDict)
  mae,rmse = util.getMAEandRMSE(recDict,playlistDict,songDict)
  print '################Dis####################'
  logging.info('################Dis####################')
  print 'Recall = ',recall
  logging.info('Recall = %f' % recall)
  print 'Precision = ',precision
  logging.info('Precision = %f' % precision)
  print 'F1-Score = ',f1
  logging.info('F1-Score = %f' % f1)
  print 'MAE = ',mae
  logging.info('MAE = %f' % mae)
  print 'RMSE = ',rmse
  logging.info('RMSE = %f' % rmse)
  print 'Average Consumed: %ds' % (time.time()-start_time)
  logging.info('Average Consumed: %ds' % (time.time()-start_time))

#test sd
def testSdMethod():
  start_time = time.time()
  songDict = persist.readSongFromFile()
  playlistDict = persist.readPlaylistFromFile()
  recDict = predict.getRecDictOfSd(playlistDict,songDict)
  recall,precision,f1 = util.getTopNIndex(recDict,playlistDict)
  mae,rmse = util.getMAEandRMSE(recDict,playlistDict,songDict)
  print '################Sd####################'
  logging.info('################Sd####################')
  print 'Recall = ',recall
  logging.info('Recall = %f' % recall)
  print 'Precision = ',precision
  logging.info('Precision = %f' % precision)
  print 'F1-Score = ',f1
  logging.info('F1-Score = %f' % f1)
  print 'MAE = ',mae
  logging.info('MAE = %f' % mae)
  print 'RMSE = ',rmse
  logging.info('RMSE = %f' % rmse)
  print 'Average Consumed: %ds' % (time.time()-start_time)
  logging.info('Average Consumed: %ds' % (time.time()-start_time))