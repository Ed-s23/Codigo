// Pines
const int ledPin = 2; //led
const int motIzqPin = 4; // giro dereco 
const int motDerPin = 5; // giro izquierdo 

const int bot1Pin = 9; //boton1
const int bot2Pin = 8; //boton2
const int bot3Pin = 7; //boton3

bool sistemaActivo = false; // Estado del sistema (activado/desactivado)
bool direccionMotor = true; // Controla de dirección del motor

void setup() {
  // Configuración de pines
  pinMode(ledPin, OUTPUT);   
  pinMode(motIzqPin, OUTPUT); 
  pinMode(motDerPin, OUTPUT); 
  pinMode(bot1Pin, INPUT);    
  pinMode(bot2Pin, INPUT);    
  pinMode(bot3Pin, INPUT);   
}

void loop() {
  // Leer el estado de los botones
  int estadob1 = digitalRead(bot1Pin);
  int estadob2 = digitalRead(bot2Pin);
  int estadob3 = digitalRead(bot3Pin);

  //  si los botones 1 y 2 están presionados se prende
  if (estadob1 == HIGH && estadob2 == HIGH) {
    sistemaActivo = true;
  }

  // apagar si el botón 3 está presionado
  if (estadob3 == HIGH) {
    sistemaActivo = false;
    apagarSistema(); // Apagar 
  }

  // Ejecutar el ciclo continuo si el sistema está activo
  while (sistemaActivo) {
    // Giro derecho
    digitalWrite(motIzqPin, direccionMotor ? HIGH : LOW);
    digitalWrite(motDerPin, direccionMotor ? LOW : HIGH);
    digitalWrite(ledPin, HIGH); // LED encendido fijo durante el giro
    esperaConInterrupcion(10000); // Esperar 10 segundos

    // Detener el motor y realizar parpadeo del LED durante 3 segundos
    digitalWrite(motIzqPin, LOW);
    digitalWrite(motDerPin, LOW);
    for (int i = 0; i < 6; i++) { // 6 parpadeos 
      if (digitalRead(bot3Pin) == HIGH) { // Verificar si se presiona el botón 3
        sistemaActivo = false;
        apagarSistema(); 
        return;
      }
      digitalWrite(ledPin, HIGH);
      delay(250);
      digitalWrite(ledPin, LOW);
      delay(250);
    }

    // giro izquierdo
    direccionMotor = !direccionMotor;
  }
}

// apagado
void apagarSistema() {
  digitalWrite(motIzqPin, LOW);
  digitalWrite(motDerPin, LOW);
  digitalWrite(ledPin, LOW);
}

// Función para esperar con posibilidad de interrupción
void esperaConInterrupcion(unsigned long tiempoMs) {
  unsigned long tiempoInicio = millis();
  while (millis() - tiempoInicio < tiempoMs) {
    if (digitalRead(bot3Pin) == HIGH) { 
      sistemaActivo = false;
      apagarSistema(); 
      return;
    }
  }
}
