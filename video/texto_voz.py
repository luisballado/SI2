
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'Los vants autónomos han revolucionado el monitoreo ambiental al proporcionar una forma eficiente y precisa de recopilar datos en áreas remotas o de difícil acceso. Estos drones pueden realizar vuelos programados para cartografiar terrenos, evaluar la calidad del aire, monitorear cambios climáticos y seguir patrones de migración de especies. Su capacidad para llegar a ubicaciones remotas sin interferir significativamente en el entorno natural los convierte en herramientas esenciales para la investigación ambiental y la conservación de la biodiversidad.'

text2 = 'En situaciones de desastre, los vants autónomos desempeñan un papel fundamental al proporcionar una respuesta rápida y eficiente. Estos drones pueden ser desplegados para evaluar daños, buscar sobrevivientes y coordinar esfuerzos de rescate. Su capacidad para acceder a áreas peligrosas o inaccesibles para los equipos de rescate tradicionales permite una toma de decisiones más informada y acelerada, mejorando así la eficacia de las operaciones de respuesta a desastres y en última instancia, salvando vidas.,,,,Los drones autónomos, también conocidos como Vehículos Aéreos No Tripulados (VANTS), representan una innovación significativa en la tecnología aérea. Estos dispositivos están equipados con sistemas avanzados de navegación y sensores que les permiten operar de manera independiente, sin intervención humana directa. La autonomía de los drones se extiende desde la planificación de vuelo hasta la ejecución de tareas específicas, lo que los hace valiosos en una variedad de aplicaciones.'
  
# Language in which you want to convert 
language = 'es'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
#myobj = gTTS(text=mytext, lang=language, slow=False)
myobj2 = gTTS(text=text2, lang=language, slow=False)

# Saving the converted audio in a mp3 file named 
# welcome  
#myobj.save("texto1.mp3")
myobj2.save("texto2.mp3")
