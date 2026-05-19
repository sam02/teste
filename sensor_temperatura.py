"""Aplicação orientada a objeto para sensor de temperatura com envio via MQTT."""

from __future__ import annotations

import json
import random
import time
from dataclasses import dataclass
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


@dataclass
class ConfiguracaoMQTT:
    broker: str
    porta: int
    topico: str
    client_id: str = "sensor-temperatura-001"
    qos: int = 1


class SensorTemperatura:
    """Simula leituras de um sensor de temperatura."""

    def __init__(self, sensor_id: str, temp_min: float = 18.0, temp_max: float = 32.0) -> None:
        self.sensor_id = sensor_id
        self.temp_min = temp_min
        self.temp_max = temp_max

    def ler_temperatura(self) -> float:
        """Retorna uma temperatura simulada em graus Celsius."""
        return round(random.uniform(self.temp_min, self.temp_max), 2)

    def gerar_payload(self) -> str:
        """Gera o payload JSON com metadados da leitura."""
        dados = {
            "sensor_id": self.sensor_id,
            "temperatura_c": self.ler_temperatura(),
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        }
        return json.dumps(dados, ensure_ascii=False)


class PublicadorMQTT:
    """Encapsula o cliente MQTT para publicar mensagens."""

    def __init__(self, configuracao: ConfiguracaoMQTT) -> None:
        self.configuracao = configuracao
        self.cliente = mqtt.Client(client_id=configuracao.client_id)

    def conectar(self) -> None:
        self.cliente.connect(self.configuracao.broker, self.configuracao.porta)

    def publicar(self, mensagem: str) -> None:
        resultado = self.cliente.publish(self.configuracao.topico, mensagem, qos=self.configuracao.qos)
        resultado.wait_for_publish()

    def desconectar(self) -> None:
        self.cliente.disconnect()


class AplicacaoSensorTemperatura:
    """Orquestra leitura do sensor e envio periódico via MQTT."""

    def __init__(self, sensor: SensorTemperatura, publicador: PublicadorMQTT, intervalo_segundos: int = 5) -> None:
        self.sensor = sensor
        self.publicador = publicador
        self.intervalo_segundos = intervalo_segundos

    def executar(self) -> None:
        self.publicador.conectar()
        print("Conectado ao broker MQTT. Enviando leituras... (CTRL+C para parar)")

        try:
            while True:
                payload = self.sensor.gerar_payload()
                self.publicador.publicar(payload)
                print(f"Publicado no tópico '{self.publicador.configuracao.topico}': {payload}")
                time.sleep(self.intervalo_segundos)
        except KeyboardInterrupt:
            print("\nEncerrando aplicação.")
        finally:
            self.publicador.desconectar()


def main() -> None:
    configuracao = ConfiguracaoMQTT(
        broker="test.mosquitto.org",
        porta=1883,
        topico="casa/sala/temperatura",
    )

    sensor = SensorTemperatura(sensor_id="temp-001")
    publicador = PublicadorMQTT(configuracao)
    app = AplicacaoSensorTemperatura(sensor, publicador, intervalo_segundos=3)
    app.executar()


if __name__ == "__main__":
    main()
