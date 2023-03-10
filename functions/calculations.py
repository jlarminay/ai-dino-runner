import os
from dotenv import load_dotenv

from functions.imageModifier import *

load_dotenv()
processingFolder = str(os.getenv('PROCESSING_FOLDER'))

def findObstacles(allObstacles, screenshot, resultImage=False):
  close1Distance = 10000
  close1Position = 0
  close2Distance = 10000
  close2Position = 0
  foundObstacles = []
  for obs in allObstacles:
    tmp = getPositionOfImage(obs[0], screenshot)
    if(len(tmp)>0):
      for ob in tmp:
        if(ob[0]-68 > 0):
          foundObstacles += [[ob, ob[0]-68]]
        # if((ob[0]-68 < closestObstacleDistance) and (ob[0]-68>0)):
        #   closestObstacleDistance = ob[0]-68
        #   closestObstaclePosition = ob[1]
      if(type(resultImage)!=bool):
        resultImage = generateSearchImage(obs[0], resultImage, obs[1])
  
  ## save image for found obstacles
  if(type(resultImage)!=bool):
    saveImage(resultImage, processingFolder+'obstacles.jpg')
  
  foundObstacles = sorted(foundObstacles, key=lambda l:l[1])
  
  # find closest object
  if(len(foundObstacles)>=1):
    close1Distance = foundObstacles[0][1]
    close1Position = foundObstacles[0][0][1]
  # find next closest
  if(len(foundObstacles)>=2):
    close2Distance = foundObstacles[1][1]
    close2Position = foundObstacles[1][0][1]

  return close1Distance, close1Position, close2Distance, close2Position