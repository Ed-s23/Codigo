// pines 
const int led2Pin = 2;
const int led3Pin = 3;
const int motIzq4Pin = 4;
const int motDer5Pin = 5;  

const int bot1Pin = 9;
const int bot2Pin = 8;
const int bot3Pin = 7;

int estadob1 = 0;
int despuesb1 = 0;
int estadob2 = 0;
int despuesb2 = 0;
int estadob3 = 0; 
//int despuesb3 = 0;

int accion = 0;
bool toggleState = false ;

void setup() {
  // put your setup code here, to run once:
  //ACCIONES DE PINES 
  pinMode(led2Pin, OUTPUT);//led1
  pinMode(led3Pin, OUTPUT);
  pinMode(motIzq4Pin, OUTPUT);//motor giro lado izquierdo 
  pinMode(motDer5Pin, OUTPUT);//motor giro lado derecho 
  pinMode(bot1Pin, INPUT);//boton1
  pinMode(bot2Pin, INPUT);//boton2
  pinMode(bot3Pin, INPUT);//boton3
}

void loop() {
  estadob1 = digitalRead(bot1Pin);
  estadob2 = digitalRead(bot2Pin);
  estadob3 = digitalRead(bot3Pin);

if (estadob1 == HIGH && despuesb1 == LOW) {
    toggleState = !toggleState;  // Cambia el estado del sistema
  }

    despuesb1 = estadob1;

if (toggleState){
    
    while (true){

      digitalWrite(led2Pin, HIGH );
      //ensendida de luz 
      digitalWrite(led3Pin, LOW );
      digitalWrite(led3Pin, LOW );
      delay(10000 );

      digitalWrite(motIzq4Pin, HIGH );  
      //encendida del motor 
      digitalWrite(motDer5Pin, LOW );
      delay(10000 );
    
    for (int o = 0; o < 5; o++) {
      digitalWrite(led3Pin, HIGH) ;   
      delay(1000);
      digitalWrite(led3Pin, LOW );
      delay(1000);
    }
      digitalWrite(led2Pin, LOW );  //ensendida de luz 
      digitalWrite(led3Pin, HIGH );
    //digitalWrite(led3Pin; LOW);
      delay(10000);

      digitalWrite(motIzq4Pin, LOW) ;  //encendida del motor 
      digitalWrite(motDer5Pin, HIGH) ;
      delay(10000);

    for (int o = 0; o < 5; o++ ) {
      digitalWrite(led3Pin, HIGH) ;   
      delay(1000);
      digitalWrite(led3Pin, LOW );
      delay(1000);
    }
  }
}else {
  digitalWrite(led2Pin, LOW ) ;
  digitalWrite(led3Pin, LOW ) ;
  digitalWrite(motIzq4Pin, LOW );
  digitalWrite(motDer5Pin, LOW );
}


  // put your main code here, to run repeatedly:

}
