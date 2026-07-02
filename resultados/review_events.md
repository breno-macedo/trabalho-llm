# Alertas para triagem da 2a camada (LLM)
Faixa normal = [p10, p90] dos fluxos LEGITIMOS (treino). Decida: ATAQUE REAL ou FALSO POSITIVO (trafego legitimo).

## Alerta 0
- 1a camada previu: **Bots** (confianca 0.73); prob: {'Bots': 0.73, 'Normal Traffic': 0.269, 'Web Attacks': 0.0}
  - Destination Port: 12750.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 255.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 1
- 1a camada previu: **DoS** (confianca 1.0); prob: {'DoS': 1.0, 'Normal Traffic': 0.0, 'Web Attacks': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 367.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 343.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 235.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 52.43 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 997.33 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 2319.0 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 4415.27 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 2
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 3
- 1a camada previu: **DoS** (confianca 1.0); prob: {'DoS': 1.0, 'Normal Traffic': 0.0, 'Web Attacks': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 616.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 308.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 235.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 88.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 939.31 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 1932.5 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 2181.01 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 4
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 5
- 1a camada previu: **Web Attacks** (confianca 0.996); prob: {'Web Attacks': 0.996, 'Normal Traffic': 0.002, 'DoS': 0.002}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 383.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 383.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 235.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 95.75 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 94.12 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 92.5 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 185.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 6
- 1a camada previu: **Port Scanning** (confianca 0.984); prob: {'Port Scanning': 0.984, 'Normal Traffic': 0.016, 'Bots': 0.0}
  - Destination Port: 8021.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 7
- 1a camada previu: **DoS** (confianca 0.739); prob: {'DoS': 0.739, 'Normal Traffic': 0.251, 'DDoS': 0.006}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 18.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -1.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 3.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 8
- 1a camada previu: **DDoS** (confianca 0.998); prob: {'DDoS': 0.998, 'Normal Traffic': 0.002, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 30.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -1.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 7.2 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 9
- 1a camada previu: **Bots** (confianca 0.905); prob: {'Bots': 0.905, 'Normal Traffic': 0.095, 'Port Scanning': 0.0}
  - Destination Port: 50522.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 256.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 10
- 1a camada previu: **Bots** (confianca 0.841); prob: {'Bots': 0.841, 'Normal Traffic': 0.159, 'Port Scanning': 0.0}
  - Destination Port: 59356.0 (normal ~80.0, faixa 53.0..51790.9) -> ACIMA do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 320.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 11
- 1a camada previu: **Bots** (confianca 0.999); prob: {'Bots': 0.999, 'Normal Traffic': 0.001, 'Port Scanning': 0.0}
  - Destination Port: 8080.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 207.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 195.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 237.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 51.75 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 48.71 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 44.67 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 72.23 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 12
- 1a camada previu: **Web Attacks** (confianca 0.982); prob: {'Web Attacks': 0.982, 'Normal Traffic': 0.015, 'DoS': 0.002}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 11584.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 13
- 1a camada previu: **DoS** (confianca 0.651); prob: {'DoS': 0.651, 'Normal Traffic': 0.339, 'Port Scanning': 0.004}
  - Destination Port: 443.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 18.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 1120.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 6.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 14
- 1a camada previu: **Bots** (confianca 0.997); prob: {'Bots': 0.997, 'Normal Traffic': 0.002, 'Port Scanning': 0.001}
  - Destination Port: 8080.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 28.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 15
- 1a camada previu: **Bots** (confianca 0.999); prob: {'Bots': 0.999, 'Normal Traffic': 0.001, 'Port Scanning': 0.0}
  - Destination Port: 8080.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 207.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 195.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 237.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 51.75 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 48.71 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 44.67 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 72.23 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 16
- 1a camada previu: **DoS** (confianca 0.62); prob: {'DoS': 0.62, 'Normal Traffic': 0.373, 'DDoS': 0.003}
  - Destination Port: 1205.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -1.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 3.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 17
- 1a camada previu: **Port Scanning** (confianca 0.975); prob: {'Port Scanning': 0.975, 'Normal Traffic': 0.025, 'DoS': 0.0}
  - Destination Port: 1947.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 2.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 5.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 18
- 1a camada previu: **Bots** (confianca 0.945); prob: {'Bots': 0.945, 'Normal Traffic': 0.055, 'Port Scanning': 0.0}
  - Destination Port: 20288.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 257.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 19
- 1a camada previu: **DoS** (confianca 0.936); prob: {'DoS': 0.936, 'Normal Traffic': 0.061, 'Port Scanning': 0.001}
  - Destination Port: 443.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 18.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 135.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.8 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 20
- 1a camada previu: **Port Scanning** (confianca 1.0); prob: {'Port Scanning': 1.0, 'Normal Traffic': 0.0, 'DoS': 0.0}
  - Destination Port: 1244.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 40.0 (normal ~20.0, faixa 20.0..32.0) -> ACIMA do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 21
- 1a camada previu: **DoS** (confianca 0.956); prob: {'DoS': 0.956, 'Normal Traffic': 0.041, 'Web Attacks': 0.001}
  - Destination Port: 443.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 123.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 22
- 1a camada previu: **Brute Force** (confianca 1.0); prob: {'Brute Force': 1.0, 'Normal Traffic': 0.0, 'Web Attacks': 0.0}
  - Destination Port: 22.0 (normal ~80.0, faixa 53.0..51790.9) -> ABAIXO do normal
  - Total Length of Fwd Packets: 2008.0 (normal ~70.0, faixa 0.0..1257.2) -> ACIMA do normal
  - Fwd Packet Length Max: 640.0 (normal ~41.0, faixa -0.0..559.4) -> ACIMA do normal
  - Init_Win_bytes_backward: 247.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 95.62 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 89.68 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 85.78 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 220.24 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 23
- 1a camada previu: **Bots** (confianca 0.917); prob: {'Bots': 0.917, 'Normal Traffic': 0.083, 'Port Scanning': 0.0}
  - Destination Port: 51799.0 (normal ~80.0, faixa 53.0..51790.9) -> ACIMA do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 256.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 24
- 1a camada previu: **DoS** (confianca 0.595); prob: {'DoS': 0.595, 'Normal Traffic': 0.272, 'Web Attacks': 0.076}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -1.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 25
- 1a camada previu: **Bots** (confianca 0.997); prob: {'Bots': 0.997, 'Normal Traffic': 0.002, 'Port Scanning': 0.001}
  - Destination Port: 8080.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 28.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 26
- 1a camada previu: **DoS** (confianca 1.0); prob: {'DoS': 1.0, 'Normal Traffic': 0.0, 'Web Attacks': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 1143.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 373.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 235.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 114.3 (normal ~38.0, faixa 0.0..101.88) -> ACIMA do normal
  - Average Packet Size: 749.65 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 1656.43 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 2120.73 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 27
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 28
- 1a camada previu: **Bots** (confianca 0.943); prob: {'Bots': 0.943, 'Normal Traffic': 0.056, 'Port Scanning': 0.0}
  - Destination Port: 51529.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 254.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 29
- 1a camada previu: **DDoS** (confianca 1.0); prob: {'DDoS': 1.0, 'DoS': 0.0, 'Normal Traffic': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 56.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 20.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 229.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 7.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 897.62 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 2321.4 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 3327.77 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 30
- 1a camada previu: **Port Scanning** (confianca 0.981); prob: {'Port Scanning': 0.981, 'Normal Traffic': 0.019, 'Bots': 0.0}
  - Destination Port: 17988.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 31
- 1a camada previu: **DDoS** (confianca 1.0); prob: {'DDoS': 1.0, 'Normal Traffic': 0.0, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 24.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -1.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 7.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 32
- 1a camada previu: **DoS** (confianca 0.396); prob: {'DoS': 0.396, 'Web Attacks': 0.307, 'Brute Force': 0.163}
  - Destination Port: 443.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 275.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 224.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 110.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 45.83 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 41.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 35.2 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 62.83 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 33
- 1a camada previu: **DDoS** (confianca 0.802); prob: {'DDoS': 0.802, 'Normal Traffic': 0.188, 'DoS': 0.006}
  - Destination Port: 443.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 12.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -1.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 34
- 1a camada previu: **DDoS** (confianca 1.0); prob: {'DDoS': 1.0, 'Port Scanning': 0.0, 'Normal Traffic': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 26.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 20.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 229.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 8.67 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 1453.37 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 2320.2 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 3668.9 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 35
- 1a camada previu: **Brute Force** (confianca 0.999); prob: {'Brute Force': 0.999, 'Normal Traffic': 0.001, 'Web Attacks': 0.0}
  - Destination Port: 21.0 (normal ~80.0, faixa 53.0..51790.9) -> ABAIXO do normal
  - Total Length of Fwd Packets: 109.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 26.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 227.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 12.11 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 12.37 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 12.53 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 14.55 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 36
- 1a camada previu: **Brute Force** (confianca 0.999); prob: {'Brute Force': 0.999, 'Normal Traffic': 0.0, 'Web Attacks': 0.0}
  - Destination Port: 21.0 (normal ~80.0, faixa 53.0..51790.9) -> ABAIXO do normal
  - Total Length of Fwd Packets: 100.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 20.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 227.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 11.11 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 12.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 12.53 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 14.55 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 37
- 1a camada previu: **Port Scanning** (confianca 1.0); prob: {'Port Scanning': 1.0, 'Normal Traffic': 0.0, 'DoS': 0.0}
  - Destination Port: 5900.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 40.0 (normal ~20.0, faixa 20.0..32.0) -> ACIMA do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 38
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 39
- 1a camada previu: **Port Scanning** (confianca 0.963); prob: {'Port Scanning': 0.963, 'Normal Traffic': 0.037, 'DoS': 0.0}
  - Destination Port: 211.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 40
- 1a camada previu: **Port Scanning** (confianca 0.972); prob: {'Port Scanning': 0.972, 'Normal Traffic': 0.028, 'Bots': 0.0}
  - Destination Port: 40193.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 41
- 1a camada previu: **Bots** (confianca 0.918); prob: {'Bots': 0.918, 'Normal Traffic': 0.082, 'Port Scanning': 0.0}
  - Destination Port: 51276.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 256.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 42
- 1a camada previu: **Port Scanning** (confianca 0.969); prob: {'Port Scanning': 0.969, 'Normal Traffic': 0.031, 'DoS': 0.0}
  - Destination Port: 1524.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 43
- 1a camada previu: **Port Scanning** (confianca 1.0); prob: {'Port Scanning': 1.0, 'Normal Traffic': 0.0, 'DoS': 0.0}
  - Destination Port: 19315.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 40.0 (normal ~20.0, faixa 20.0..32.0) -> ACIMA do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 44
- 1a camada previu: **Bots** (confianca 0.945); prob: {'Bots': 0.945, 'Normal Traffic': 0.055, 'Port Scanning': 0.0}
  - Destination Port: 51366.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 258.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 45
- 1a camada previu: **Brute Force** (confianca 0.503); prob: {'Brute Force': 0.503, 'Web Attacks': 0.288, 'Normal Traffic': 0.197}
  - Destination Port: 22.0 (normal ~80.0, faixa 53.0..51790.9) -> ABAIXO do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 243.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 46
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 47
- 1a camada previu: **Web Attacks** (confianca 0.915); prob: {'Web Attacks': 0.915, 'DoS': 0.078, 'Normal Traffic': 0.007}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 1425.0 (normal ~70.0, faixa 0.0..1257.2) -> ACIMA do normal
  - Fwd Packet Length Max: 475.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 235.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 203.57 (normal ~38.0, faixa 0.0..101.88) -> ACIMA do normal
  - Average Packet Size: 412.5 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 705.0 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 1254.72 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 48
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 26847.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 49
- 1a camada previu: **Bots** (confianca 0.999); prob: {'Bots': 0.999, 'Normal Traffic': 0.001, 'Port Scanning': 0.0}
  - Destination Port: 8080.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 210.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 198.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 237.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 52.5 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 49.14 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 44.67 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 72.23 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 50
- 1a camada previu: **DDoS** (confianca 1.0); prob: {'DDoS': 1.0, 'Normal Traffic': 0.0, 'Port Scanning': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 62.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 20.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 229.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.89 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 778.33 (normal ~76.5, faixa 3.0..335.49) -> ACIMA do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 1934.5 (normal ~77.75, faixa -0.0..453.4) -> ACIMA do normal
  - Bwd Packet Length Std: 2538.92 (normal ~-0.0, faixa -0.0..637.22) -> ACIMA do normal

## Alerta 51
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 52
- 1a camada previu: **Brute Force** (confianca 1.0); prob: {'Brute Force': 1.0, 'Normal Traffic': 0.0, 'Web Attacks': 0.0}
  - Destination Port: 22.0 (normal ~80.0, faixa 53.0..51790.9) -> ABAIXO do normal
  - Total Length of Fwd Packets: 2008.0 (normal ~70.0, faixa 0.0..1257.2) -> ACIMA do normal
  - Fwd Packet Length Max: 640.0 (normal ~41.0, faixa -0.0..559.4) -> ACIMA do normal
  - Init_Win_bytes_backward: 247.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 95.62 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 89.68 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 85.78 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 220.24 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 53
- 1a camada previu: **Port Scanning** (confianca 0.967); prob: {'Port Scanning': 0.967, 'Normal Traffic': 0.033, 'DoS': 0.0}
  - Destination Port: 264.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 54
- 1a camada previu: **Brute Force** (confianca 0.999); prob: {'Brute Force': 0.999, 'Normal Traffic': 0.001, 'Web Attacks': 0.0}
  - Destination Port: 21.0 (normal ~80.0, faixa 53.0..51790.9) -> ABAIXO do normal
  - Total Length of Fwd Packets: 106.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 26.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 227.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 11.78 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 12.25 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 12.53 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 14.55 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 55
- 1a camada previu: **Web Attacks** (confianca 0.526); prob: {'Web Attacks': 0.526, 'Normal Traffic': 0.469, 'DoS': 0.004}
  - Destination Port: 443.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 2626.0 (normal ~70.0, faixa 0.0..1257.2) -> ACIMA do normal
  - Fwd Packet Length Max: 1050.0 (normal ~41.0, faixa -0.0..559.4) -> ACIMA do normal
  - Init_Win_bytes_backward: 8.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 291.78 (normal ~38.0, faixa 0.0..101.88) -> ACIMA do normal
  - Average Packet Size: 292.19 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 292.71 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: 455.87 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 56
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.001, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 57
- 1a camada previu: **Web Attacks** (confianca 0.996); prob: {'Web Attacks': 0.996, 'Normal Traffic': 0.003, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 28960.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 58
- 1a camada previu: **Web Attacks** (confianca 0.999); prob: {'Web Attacks': 0.999, 'Normal Traffic': 0.0, 'DoS': 0.0}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 26847.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: -0.0 (normal ~76.5, faixa 3.0..335.49) -> ABAIXO do normal
  - min_seg_size_forward: 32.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: -0.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: -0.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 59
- 1a camada previu: **Bots** (confianca 0.894); prob: {'Bots': 0.894, 'Normal Traffic': 0.091, 'Port Scanning': 0.014}
  - Destination Port: 80.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 913.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 60
- 1a camada previu: **Port Scanning** (confianca 0.988); prob: {'Port Scanning': 0.988, 'Normal Traffic': 0.012, 'Bots': 0.0}
  - Destination Port: 1720.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 4.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 2.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 2.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 4.5 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 24.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 61
- 1a camada previu: **Port Scanning** (confianca 1.0); prob: {'Port Scanning': 1.0, 'Normal Traffic': 0.0, 'DoS': 0.0}
  - Destination Port: 1148.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 0.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: -0.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: -0.0 (normal ~-1.0, faixa -1.0..980.0) -> dentro do normal
  - Fwd Packet Length Mean: 0.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 3.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 40.0 (normal ~20.0, faixa 20.0..32.0) -> ACIMA do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

## Alerta 62
- 1a camada previu: **Bots** (confianca 0.908); prob: {'Bots': 0.908, 'Normal Traffic': 0.092, 'Port Scanning': 0.0}
  - Destination Port: 9943.0 (normal ~80.0, faixa 53.0..51790.9) -> dentro do normal
  - Total Length of Fwd Packets: 6.0 (normal ~70.0, faixa 0.0..1257.2) -> dentro do normal
  - Fwd Packet Length Max: 6.0 (normal ~41.0, faixa -0.0..559.4) -> dentro do normal
  - Init_Win_bytes_backward: 16425.0 (normal ~-1.0, faixa -1.0..980.0) -> ACIMA do normal
  - Fwd Packet Length Mean: 6.0 (normal ~38.0, faixa 0.0..101.88) -> dentro do normal
  - Average Packet Size: 9.0 (normal ~76.5, faixa 3.0..335.49) -> dentro do normal
  - min_seg_size_forward: 20.0 (normal ~20.0, faixa 20.0..32.0) -> dentro do normal
  - Bwd Packet Length Min: 6.0 (normal ~6.0, faixa -0.0..138.0) -> dentro do normal
  - Bwd Packet Length Mean: 6.0 (normal ~77.75, faixa -0.0..453.4) -> dentro do normal
  - Bwd Packet Length Std: -0.0 (normal ~-0.0, faixa -0.0..637.22) -> dentro do normal

