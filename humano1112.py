print("Act 9 clase humano")
print("Melanie Vega Renteria mat: 22308051281112")
# zona de class
class humano1112:
    # zona de atributos
    edad=17
    genero="Femenino"
    estatura=1.67
    fecha_nacimiento="02/02/2007"
    color_cabello="cafe"
    peso="50kg"
    edadd=17
    generoo="Femenino"
    estaturaa=1.60
    fecha_nacimientoo="29/08/2007"
    color_cabelloo="cafe"
    pesoo="60kg"
    # zona de funciones dentro de la clase
    def correr1112(self,n):
        print(f"{n} está corriendo")
    def comer1112(self,n):
        print(f"{n} está comiendo")
    def jugar1112(self,n):
        print(f"{n} está jugando")
    def caminar1112(self,n):
        print(f"{n} está caminando")
    def musica1112(self,n):
        print(f"{n} está escuchando musica")    
# zona de creacion de objetos
Mel=humano1112()
dorle=humano1112()
#zona de usar objetos
print("------Resultados para mel-------")
print(f"edad: {Mel.edad}")
print(f"genero: {Mel.genero}")
print(f"estatura: {Mel.estatura}")
print(f"fecha de nacimiento: {Mel.fecha_nacimiento}")
print(f"color de cabello: {Mel.color_cabello}")
print(f"peso: {Mel.peso}")
dorle.correr1112("mel")
dorle.comer1112("mel")
dorle.jugar1112("mel")
dorle.caminar1112("mel")
dorle.musica1112("mel")
print("-----Resultados para dorle------") 
print(f"edad: {dorle.edadd}")
print(f"genero: {dorle.generoo}")
print(f"estatura: {dorle.estaturaa}")
print(f"fecha de nacimiento: {dorle.fecha_nacimientoo}")
print(f"color de cabello: {dorle.color_cabelloo}")
print(f"peso: {dorle.pesoo}")
Mel.correr1112("dorle")
Mel.comer1112("dorle")
Mel.jugar1112("dorle")
Mel.caminar1112("dorle")
Mel.musica1112("dorle")
Mel.correr1112("dorle")