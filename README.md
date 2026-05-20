# Sensor de Temperatura com MQTT (POO em Python)

Aplicação orientada a objeto que simula um sensor de temperatura, publica leituras em um tópico MQTT e emite alerta para temperaturas acima de 30°C.

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


## Alerta de temperatura

O payload enviado agora inclui o campo `alerta_temp_alta`. Quando a leitura ultrapassa `30.0°C`, esse campo fica `true` e uma mensagem de alerta é exibida no terminal.
