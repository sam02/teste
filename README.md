# Sensor de Temperatura com MQTT (POO em Python)

Aplicação orientada a objeto que simula um sensor de temperatura e publica leituras em um tópico MQTT.

## Estrutura

- `ConfiguracaoMQTT`: dados de conexão do broker.
- `SensorTemperatura`: simula leitura e monta payload JSON.
- `PublicadorMQTT`: encapsula conexão e publicação MQTT.
- `AplicacaoSensorTemperatura`: executa ciclo de leitura/publicação.

## Como executar

1. Crie um ambiente virtual (opcional):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Execute:

```bash
python sensor_temperatura.py
```

Por padrão, o broker usado é `test.mosquitto.org`, porta `1883`, tópico `casa/sala/temperatura`.
