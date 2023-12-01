from vpython import *
#Web VPython 2.6


scene.autoscale = False
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=500,shininess=0)

SUN=sphere( texture="https://i.imgur.com/PWnSJQd.jpeg",flipx = False , shininess = 10,radius=10 )

FirstPlanet=sphere(pos= vector (0,0,23), texture="https://i.imgur.com/Mwsa16j.jpeg",flipx = False , shininess = 0 , radius=1.31, make_trail=True )

SecondPlanet=sphere(pos= vector (0,0,43), texture="https://i.imgur.com/tJV7qzf.png",flipx = False , shininess = 0 , radius=0.54, make_trail=True )

ThirdPlanet=sphere(pos= vector (0,0,63), texture="https://i.imgur.com/02Kt4gy.jpeg",flipx = False , shininess = 0 , radius=1.95, make_trail=True )

FouthPlanet=sphere(pos= vector (0,0,123), texture="https://upload.wikimedia.org/wikipedia/commons/6/62/Kepler-62f_in_Celestia.png",flipx = False , shininess = 0 , radius=1.61, make_trail=True )

FifthPlanet=sphere(pos= vector (0,0,183), texture="https://i.imgur.com/zoqIFOpb.jpg",flipx = False , shininess = 0 , radius=1.41, make_trail=True )

framerate= 40

omegaOne= 2*3.14/100

omegaTwo= 2*3.14/124

omegaThree= 2*3.14/182

omegaFour= 2*3.14/1224

omegaFive= 2*3.14/2673

while True :
    
    rate(framerate)
    
    FirstPlanet.rotate( angle = omegaOne , axis= vector(0,1,0), origin = vector(0,0,0))
    
    SecondPlanet.rotate( angle = omegaTwo , axis= vector(0,1,0), origin = vector(0,0,0))
    
    ThirdPlanet.rotate( angle = omegaThree , axis= vector(0,1,0), origin = vector(0,0,0))
    
    FouthPlanet.rotate( angle = omegaFour , axis= vector(0,1,0), origin = vector(0,0,0))
     
    FifthPlanet.rotate( angle = omegaFive , axis= vector(0,1,0), origin = vector(0,0,0))
    
    
    
    
    
