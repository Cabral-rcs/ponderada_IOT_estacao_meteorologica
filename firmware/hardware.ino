#include "DHT.h" // Biblioteca

#define DHTPIN 1 // Pino do sensor
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE); // Inicialização

// Variáveis de controle para o Millis()
unsigned long tempoAnterior = 0;
const long intervalo = 5000; // 5 segundos

// Setup
void setup() {
  Serial.begin(9600);
  dht.begin();
}

// Loop
void loop() {

  unsigned long tempoAtual = millis();

  // Executa a cada 5 segundos
  if (tempoAtual - tempoAnterior >= intervalo) {
    tempoAnterior = tempoAtual;

    // Leitura dos sensores
    float temp = dht.readTemperature();
    float umid = dht.readHumidity();

    // Exibição das leituras
    if (!isnan(temp) && !isnan(umid)) {
      Serial.print("{");
      Serial.print("\"temperatura\":"); Serial.print(temp);
      Serial.print(",\"umidade\":"); Serial.print(umid);
      Serial.println("}");
    }
  }
}